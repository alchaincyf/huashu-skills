#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
# ]
# ///
"""
Gemini 3 Pro/Flash video analysis tool.

Usage:
    uv run analyze_video.py --video "video.mp4" --prompt "summarize this video"
    uv run analyze_video.py --video "https://youtube.com/watch?v=ID" --prompt "describe key moments"
    uv run analyze_video.py --video "video.mp4" --prompt "generate SRT subtitles" --output subs.srt
"""

import argparse
import os
import sys
import time
from pathlib import Path


MODELS = {
    "pro": "gemini-3-pro-preview",
    "flash": "gemini-3-flash-preview",
}

RESOLUTIONS = {
    "low": "media_resolution_low",
    "medium": "media_resolution_medium",
    "high": "media_resolution_high",
}


def get_api_key(provided_key: str | None) -> str | None:
    if provided_key:
        return provided_key
    return os.environ.get("GEMINI_API_KEY")


def is_youtube_url(video_path: str) -> bool:
    return any(domain in video_path for domain in [
        "youtube.com", "youtu.be", "youtube-nocookie.com"
    ])


def is_url(video_path: str) -> bool:
    return video_path.startswith("http://") or video_path.startswith("https://")


def get_file_size_mb(file_path: str) -> float:
    return Path(file_path).stat().st_size / (1024 * 1024)


def upload_and_wait(client, file_path: str) -> object:
    """Upload video via File API and wait for processing."""
    print(f"Uploading: {file_path}", file=sys.stderr)
    video_file = client.files.upload(file=file_path)
    print(f"Upload complete: {video_file.name}", file=sys.stderr)

    while not video_file.state or video_file.state.name != "ACTIVE":
        print(f"  Processing... ({video_file.state})", file=sys.stderr)
        time.sleep(5)
        video_file = client.files.get(name=video_file.name)

    print("Video ready for analysis", file=sys.stderr)
    return video_file


def main():
    parser = argparse.ArgumentParser(
        description="Analyze video using Gemini 3 Pro/Flash"
    )
    parser.add_argument(
        "--video", "-v", required=True,
        help="Video file path or YouTube URL"
    )
    parser.add_argument(
        "--prompt", "-p", required=True,
        help="Analysis prompt"
    )
    parser.add_argument(
        "--model", "-m", choices=["pro", "flash"], default="pro",
        help="Model: pro (default, better) or flash (cheaper, has free tier)"
    )
    parser.add_argument(
        "--resolution", "-r", choices=["low", "medium", "high"], default="medium",
        help="Video resolution: low (save tokens), medium (default), high (read text)"
    )
    parser.add_argument(
        "--start", type=int, default=None,
        help="Start time in seconds (for clipping)"
    )
    parser.add_argument(
        "--end", type=int, default=None,
        help="End time in seconds (for clipping)"
    )
    parser.add_argument(
        "--fps", type=float, default=None,
        help="Custom FPS (default 1.0, use 0.5 for long videos)"
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="Save output to file (e.g., subtitles.srt)"
    )
    parser.add_argument(
        "--api-key", "-k", default=None,
        help="Gemini API key (overrides GEMINI_API_KEY env var)"
    )

    args = parser.parse_args()

    api_key = get_api_key(args.api_key)
    if not api_key:
        print("Error: No API key. Set GEMINI_API_KEY or use --api-key", file=sys.stderr)
        sys.exit(1)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_id = MODELS[args.model]

    # Build config
    config_kwargs = {}
    if args.resolution:
        config_kwargs["media_resolution"] = RESOLUTIONS[args.resolution]

    config = types.GenerateContentConfig(**config_kwargs) if config_kwargs else None

    # Build content parts
    parts = []

    if is_youtube_url(args.video):
        # YouTube URL - direct input
        print(f"Analyzing YouTube video: {args.video}", file=sys.stderr)
        part_kwargs = {
            "file_data": types.FileData(file_uri=args.video)
        }
        if args.start is not None or args.end is not None or args.fps is not None:
            video_meta = {}
            if args.start is not None:
                video_meta["start_offset"] = f"{args.start}s"
            if args.end is not None:
                video_meta["end_offset"] = f"{args.end}s"
            if args.fps is not None:
                video_meta["fps"] = args.fps
            part_kwargs["video_metadata"] = types.VideoMetadata(**video_meta)
        parts.append(types.Part(**part_kwargs))

    elif is_url(args.video):
        # Other URL
        print(f"Analyzing video URL: {args.video}", file=sys.stderr)
        parts.append(types.Part(
            file_data=types.FileData(file_uri=args.video)
        ))

    else:
        # Local file
        file_path = args.video
        if not Path(file_path).exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)

        file_size = get_file_size_mb(file_path)
        print(f"Video file: {file_path} ({file_size:.1f} MB)", file=sys.stderr)

        if file_size <= 20:
            # Inline upload for small files
            print("Using inline upload (< 20MB)", file=sys.stderr)
            video_bytes = open(file_path, "rb").read()

            # Detect MIME type
            ext = Path(file_path).suffix.lower()
            mime_map = {
                ".mp4": "video/mp4", ".mov": "video/mov",
                ".avi": "video/avi", ".webm": "video/webm",
                ".wmv": "video/wmv", ".mpg": "video/mpg",
                ".mpeg": "video/mpeg", ".flv": "video/x-flv",
                ".3gp": "video/3gpp",
            }
            mime_type = mime_map.get(ext, "video/mp4")

            parts.append(types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type=mime_type)
            ))
        else:
            # File API for large files
            video_file = upload_and_wait(client, file_path)
            part_kwargs = {
                "file_data": types.FileData(file_uri=video_file.uri)
            }
            if args.start is not None or args.end is not None or args.fps is not None:
                video_meta = {}
                if args.start is not None:
                    video_meta["start_offset"] = f"{args.start}s"
                if args.end is not None:
                    video_meta["end_offset"] = f"{args.end}s"
                if args.fps is not None:
                    video_meta["fps"] = args.fps
                part_kwargs["video_metadata"] = types.VideoMetadata(**video_meta)
            parts.append(types.Part(**part_kwargs))

    # Add text prompt
    parts.append(types.Part(text=args.prompt))

    # Call API
    print(f"Analyzing with {model_id}...", file=sys.stderr)
    try:
        generate_kwargs = {
            "model": model_id,
            "contents": types.Content(parts=parts),
        }
        if config:
            generate_kwargs["config"] = config

        response = client.models.generate_content(**generate_kwargs)
        result = response.text

        # Output
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(result, encoding="utf-8")
            print(f"\nResult saved to: {output_path.resolve()}", file=sys.stderr)
        else:
            print(result)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
