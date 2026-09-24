import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).parents[1] / "scripts" / "generate_image.py"
SPEC = importlib.util.spec_from_file_location("generate_image", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FakeRequestException(Exception):
    pass


class FakeResponse:
    def __init__(self, *, payload=None, status_code=200, content=b""):
        self._payload = payload
        self.status_code = status_code
        self.content = content

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise FakeRequestException(f"HTTP {self.status_code}")


class FakeSession:
    class exceptions:
        RequestException = FakeRequestException

    def __init__(self, *, post_responses, get_responses):
        self.post_responses = list(post_responses)
        self.get_responses = list(get_responses)
        self.post_calls = []
        self.get_calls = []

    def post(self, url, **kwargs):
        self.post_calls.append((url, kwargs))
        return self.post_responses.pop(0)

    def get(self, url, **kwargs):
        self.get_calls.append((url, kwargs))
        return self.get_responses.pop(0)


class GenerateImageTests(unittest.TestCase):
    def test_gemini_remains_the_default_provider(self):
        args = MODULE.parse_args(["--prompt", "p", "--filename", "out.png"])
        self.assertEqual(args.provider, "gemini")

    def test_atlas_key_uses_atlas_environment_only(self):
        with mock.patch.dict(
            os.environ,
            {"ATLASCLOUD_API_KEY": "atlas-key", "GEMINI_API_KEY": "gemini-key"},
            clear=True,
        ):
            self.assertEqual(MODULE.get_api_key("atlas", None), "atlas-key")
            self.assertEqual(MODULE.get_api_key("gemini", None), "gemini-key")

    @mock.patch.object(MODULE.time, "sleep")
    def test_atlas_submits_once_and_retries_prediction_get(self, sleep):
        session = FakeSession(
            post_responses=[
                FakeResponse(payload={"code": 200, "data": {"id": "prediction-1"}})
            ],
            get_responses=[
                FakeResponse(status_code=503),
                FakeResponse(payload={"code": 200, "data": {"status": "processing"}}),
                FakeResponse(
                    payload={
                        "code": 200,
                        "data": {
                            "status": "completed",
                            "outputs": ["https://cdn.example/output.png"],
                        },
                    }
                ),
                FakeResponse(content=b"image-bytes"),
            ],
        )

        result = MODULE.atlas_generate(
            api_key="secret",
            prompt="A poster",
            aspect=MODULE.ASPECT_PRESETS["wide"],
            resolution="2K",
            input_path=None,
            session=session,
            base_url="https://atlas.example/api/v1",
        )

        self.assertEqual(result, b"image-bytes")
        self.assertEqual(len(session.post_calls), 1)
        _, submit_kwargs = session.post_calls[0]
        self.assertEqual(
            submit_kwargs["json"],
            {
                "model": MODULE.ATLAS_TEXT_MODEL,
                "prompt": "A poster",
                "aspect_ratio": "16:9",
                "resolution": "2k",
            },
        )
        self.assertEqual(len(session.get_calls), 4)
        self.assertIn(mock.call(1), sleep.call_args_list)

    @mock.patch.object(MODULE.time, "sleep")
    def test_atlas_edit_uploads_input_once(self, _sleep):
        session = FakeSession(
            post_responses=[
                FakeResponse(
                    payload={
                        "code": 200,
                        "data": {"download_url": "https://uploads.example/input.png"},
                    }
                ),
                FakeResponse(payload={"code": 200, "data": {"id": "prediction-2"}}),
            ],
            get_responses=[
                FakeResponse(
                    payload={
                        "code": 200,
                        "data": {
                            "status": "completed",
                            "outputs": ["https://cdn.example/edited.png"],
                        },
                    }
                ),
                FakeResponse(content=b"edited-image"),
            ],
        )

        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "input.png"
            input_path.write_bytes(b"input")
            result = MODULE.atlas_generate(
                api_key="secret",
                prompt="Edit it",
                aspect=MODULE.ASPECT_PRESETS["square"],
                resolution="1K",
                input_path=input_path,
                session=session,
                base_url="https://atlas.example/api/v1",
            )

        self.assertEqual(result, b"edited-image")
        self.assertEqual(len(session.post_calls), 2)
        upload_url, upload_kwargs = session.post_calls[0]
        self.assertTrue(upload_url.endswith("/model/uploadMedia"))
        self.assertIn("file", upload_kwargs["files"])
        _, submit_kwargs = session.post_calls[1]
        self.assertEqual(submit_kwargs["json"]["model"], MODULE.ATLAS_EDIT_MODEL)
        self.assertEqual(
            submit_kwargs["json"]["images"],
            ["https://uploads.example/input.png"],
        )

    @mock.patch.object(MODULE.time, "sleep")
    def test_prediction_get_does_not_retry_client_errors(self, sleep):
        session = FakeSession(
            post_responses=[],
            get_responses=[FakeResponse(status_code=401)],
        )

        with self.assertRaises(FakeRequestException):
            MODULE.atlas_prediction_get(
                session,
                "https://atlas.example/api/v1/model/prediction/prediction-3",
                {"Authorization": "test-value"},
            )

        self.assertEqual(len(session.get_calls), 1)
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
