#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
#     "requests>=2.31.0",
# ]
# ///
"""Generate images for WeChat articles with Gemini or Atlas Cloud.

Gemini remains the default provider. Atlas Cloud is opt-in via
``--provider atlas`` and uses its asynchronous image generation API.

Usage:
    uv run generate_image.py --prompt "description" --filename output.png
    uv run generate_image.py --provider atlas --prompt "description" --filename output.png
    uv run generate_image.py --prompt "edit instructions" --filename output.png --input-image input.png
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Any

ASPECT_PRESETS = {
    "cover": {
        "ratio": "2.35:1",
        "atlas_ratio": "21:9",
        "pixels": "1800x766",
        "desc": "头条封面 ultra-wide landscape",
    },
    "wide": {
        "ratio": "16:9",
        "atlas_ratio": "16:9",
        "pixels": "1920x1080",
        "desc": "正文宽图 landscape",
    },
    "standard": {
        "ratio": "4:3",
        "atlas_ratio": "4:3",
        "pixels": "1440x1080",
        "desc": "正文方图 landscape",
    },
    "square": {
        "ratio": "1:1",
        "atlas_ratio": "1:1",
        "pixels": "1080x1080",
        "desc": "方图",
    },
}

GEMINI_DEFAULT_MODEL = "gemini-3-pro-image-preview"
ATLAS_TEXT_MODEL = "google/nano-banana-2/text-to-image"
ATLAS_EDIT_MODEL = "google/nano-banana-2/edit"
ATLAS_MEDIA_API_BASE = "https://api.atlascloud.ai/api/v1"
ATLAS_MAX_IMAGE_BYTES = 25 * 1024 * 1024
ATLAS_POLL_ATTEMPTS = 120
ATLAS_POLL_INTERVAL_SECONDS = 3
ATLAS_GET_RETRY_DELAYS = (1, 2, 4)


def get_api_key(provider: str, provided_key: str | None) -> str | None:
    """Get the selected provider's API key without changing default behavior."""
    if provided_key:
        return provided_key
    if provider == "atlas":
        return os.environ.get("ATLASCLOUD_API_KEY") or os.environ.get(
            "ATLAS_CLOUD_API_KEY"
        )
    return os.environ.get("GEMINI_API_KEY")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate images for WeChat (公众号) using Gemini or Atlas Cloud"
    )
    parser.add_argument(
        "--prompt", "-p", required=True, help="Image description/prompt"
    )
    parser.add_argument(
        "--filename",
        "-f",
        required=True,
        help="Output filename (e.g. wechat-cover.png)",
    )
    parser.add_argument(
        "--input-image", "-i", help="Optional input image path for editing/modification"
    )
    parser.add_argument(
        "--aspect",
        "-a",
        choices=list(ASPECT_PRESETS),
        default="wide",
        help="Aspect preset: cover, wide (default), standard, or square",
    )
    parser.add_argument(
        "--resolution",
        "-r",
        choices=["1K", "2K", "4K"],
        default="2K",
        help="Output resolution: 1K, 2K (default), or 4K",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "atlas"],
        default="gemini",
        help="Image provider (default: gemini)",
    )
    parser.add_argument(
        "--api-key",
        "-k",
        help="Provider API key (overrides GEMINI_API_KEY or ATLASCLOUD_API_KEY)",
    )
    return parser.parse_args(argv)


def response_data(response: Any, action: str) -> dict[str, Any]:
    """Validate an Atlas API response and return its data object."""
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") not in (None, 200):
        raise RuntimeError(
            f"Atlas {action} failed: {payload.get('message', 'unknown error')}"
        )
    data = payload.get("data")
    if not isinstance(data, dict):
        raise RuntimeError(f"Atlas {action} returned no data")
    return data


def atlas_prediction_get(session: Any, url: str, headers: dict[str, str]) -> Any:
    """GET a prediction with bounded backoff for transient failures only."""
    for delay in (*ATLAS_GET_RETRY_DELAYS, None):
        try:
            response = session.get(url, headers=headers, timeout=30)
        except session.exceptions.RequestException:
            if delay is None:
                raise
        else:
            if response.status_code != 429 and response.status_code < 500:
                response.raise_for_status()
                return response
            if delay is None:
                response.raise_for_status()
        if delay is not None:
            time.sleep(delay)
    raise RuntimeError("Atlas prediction request exhausted retries")


def atlas_upload_image(
    session: Any, base_url: str, headers: dict[str, str], input_path: Path
) -> str:
    """Upload an edit input once; Atlas uploads are temporary generation inputs."""
    with input_path.open("rb") as image_file:
        response = session.post(
            f"{base_url}/model/uploadMedia",
            headers=headers,
            files={"file": (input_path.name, image_file)},
            timeout=60,
        )
    data = response_data(response, "upload")
    download_url = data.get("download_url")
    if not isinstance(download_url, str) or not download_url:
        raise RuntimeError("Atlas upload returned no download URL")
    return download_url


def atlas_generate(
    *,
    api_key: str,
    prompt: str,
    aspect: dict[str, str],
    resolution: str,
    input_path: Path | None,
    session: Any | None = None,
    base_url: str | None = None,
) -> bytes:
    """Submit one Atlas task, poll it, and download the generated image."""
    if session is None:
        import requests

        session = requests

    base_url = (
        base_url or os.environ.get("ATLAS_MEDIA_API_BASE") or ATLAS_MEDIA_API_BASE
    ).rstrip("/")
    auth_headers = {"Authorization": f"Bearer {api_key}"}
    payload: dict[str, Any] = {
        "model": ATLAS_EDIT_MODEL if input_path is not None else ATLAS_TEXT_MODEL,
        "prompt": prompt,
        "aspect_ratio": aspect["atlas_ratio"],
        "resolution": resolution.lower(),
    }

    if input_path is not None:
        payload["images"] = [
            atlas_upload_image(session, base_url, auth_headers, input_path)
        ]

    # Generation POST is intentionally issued exactly once to avoid duplicate billing.
    response = session.post(
        f"{base_url}/model/generateImage",
        headers={**auth_headers, "Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    prediction_id = response_data(response, "submission").get("id")
    if not isinstance(prediction_id, str) or not prediction_id:
        raise RuntimeError("Atlas submission returned no prediction ID")

    prediction_url = f"{base_url}/model/prediction/{prediction_id}"
    output_url: str | None = None
    for _ in range(ATLAS_POLL_ATTEMPTS):
        time.sleep(ATLAS_POLL_INTERVAL_SECONDS)
        result = response_data(
            atlas_prediction_get(session, prediction_url, auth_headers), "prediction"
        )
        status = str(result.get("status", "unknown")).lower()
        if status in ("completed", "succeeded"):
            outputs = result.get("outputs") or result.get("output") or []
            if isinstance(outputs, str):
                outputs = [outputs]
            if isinstance(outputs, list) and outputs and isinstance(outputs[0], str):
                output_url = outputs[0]
                break
            raise RuntimeError("Atlas prediction completed without an image URL")
        if status == "failed":
            raise RuntimeError(
                f"Atlas generation failed: {result.get('error', 'unknown error')}"
            )
        print(f"Atlas status: {status}...")
    else:
        raise TimeoutError("Atlas generation timed out")

    # Output download is a single GET; only prediction GETs are retried.
    image_response = session.get(output_url, timeout=60)
    image_response.raise_for_status()
    image_bytes = image_response.content
    if not image_bytes or len(image_bytes) > ATLAS_MAX_IMAGE_BYTES:
        raise RuntimeError("Atlas output image is empty or exceeds 25 MiB")
    return image_bytes


def gemini_generate(
    *,
    api_key: str,
    prompt: str,
    resolution: str,
    input_image: Any | None,
) -> bytes:
    """Run the existing Gemini generation path and return image bytes."""
    from google import genai
    from google.genai import types

    base_url = os.environ.get("GEMINI_BASE_URL")
    if base_url:
        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(base_url=base_url),
        )
    else:
        client = genai.Client(api_key=api_key)

    contents = [input_image, prompt] if input_image is not None else prompt
    response = client.models.generate_content(
        model=GEMINI_DEFAULT_MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(image_size=resolution),
        ),
    )

    image_data = None
    for part in response.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            image_data = part.inline_data.data
            if isinstance(image_data, str):
                import base64

                image_data = base64.b64decode(image_data)
    if image_data is None:
        raise RuntimeError("Gemini response contained no image")
    return image_data


def save_png(image_bytes: bytes, output_path: Path) -> tuple[int, int]:
    """Validate provider output with Pillow and save a normalized PNG."""
    from PIL import Image as PILImage

    with PILImage.open(BytesIO(image_bytes)) as image:
        image.load()
        if image.mode == "RGBA":
            rgb_image = PILImage.new("RGB", image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.getchannel("A"))
        elif image.mode == "RGB":
            rgb_image = image.copy()
        else:
            rgb_image = image.convert("RGB")
        rgb_image.save(output_path, "PNG")
        return rgb_image.size


def report_result(
    output_path: Path, aspect: dict[str, str], dimensions: tuple[int, int]
) -> None:
    full_path = output_path.resolve()
    width, height = dimensions
    actual_ratio = width / height
    ratio_parts = aspect["ratio"].split(":")
    expected_ratio = float(ratio_parts[0]) / float(ratio_parts[1])

    print(f"\nImage saved: {full_path}")
    print(
        f"Dimensions: {width}x{height} (ratio: {actual_ratio:.2f}, "
        f"expected {aspect['ratio']} = {expected_ratio:.2f})"
    )
    if abs(actual_ratio - expected_ratio) > 0.15:
        print(
            f"Warning: Image ratio {actual_ratio:.2f} differs from expected "
            f"{aspect['ratio']} ({expected_ratio:.2f}). Consider regenerating."
        )
    if aspect["ratio"] == "2.35:1":
        print(
            f"Cover safe zone reminder: keep core content within the center "
            f"{height}x{height} square area."
        )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    api_key = get_api_key(args.provider, args.api_key)
    if not api_key:
        env_name = (
            "ATLASCLOUD_API_KEY" if args.provider == "atlas" else "GEMINI_API_KEY"
        )
        print(
            f"Error: No API key provided. Set {env_name} or pass --api-key.",
            file=sys.stderr,
        )
        return 1

    output_path = Path(args.filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    aspect = ASPECT_PRESETS[args.aspect]
    input_path = Path(args.input_image) if args.input_image else None
    input_image = None
    output_resolution = args.resolution

    try:
        if input_path is not None:
            from PIL import Image as PILImage

            input_image = PILImage.open(input_path)
            print(f"Loaded input image: {input_path}")
            if args.resolution == "2K":
                width, height = input_image.size
                max_dim = max(width, height)
                output_resolution = (
                    "4K" if max_dim >= 3000 else "2K" if max_dim >= 1500 else "1K"
                )
                print(
                    f"Auto-detected resolution: {output_resolution} "
                    f"(from input {width}x{height})"
                )

        action = "Editing" if input_path is not None else "Generating"
        print(
            f"{action} WeChat image with {args.provider} "
            f"({aspect['desc']}, {aspect['ratio']}) at {output_resolution}..."
        )

        if args.provider == "atlas":
            image_bytes = atlas_generate(
                api_key=api_key,
                prompt=args.prompt,
                aspect=aspect,
                resolution=output_resolution,
                input_path=input_path,
            )
        else:
            image_bytes = gemini_generate(
                api_key=api_key,
                prompt=args.prompt,
                resolution=output_resolution,
                input_image=input_image,
            )

        dimensions = save_png(image_bytes, output_path)
        report_result(output_path, aspect, dimensions)
        return 0
    except Exception as exc:
        print(f"Error generating image: {exc}", file=sys.stderr)
        return 1
    finally:
        if input_image is not None:
            input_image.close()


if __name__ == "__main__":
    raise SystemExit(main())
