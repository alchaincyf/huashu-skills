#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
# ]
# ///
"""
Generate images for WeChat Official Account (公众号) articles using Gemini 3 Pro Image API.

Supports multiple aspect ratios:
  --aspect cover    → 2.35:1 (900x383, 头条封面)
  --aspect wide     → 16:9 (1920x1080, 正文宽图)
  --aspect standard → 4:3 (1440x1080, 正文方图)
  --aspect square   → 1:1 (1080x1080, 方图)

Default: 2K resolution.

Usage:
    uv run generate_image.py --prompt "description" --filename "output.png" [--aspect cover|wide|standard|square] [--resolution 1K|2K|4K]
    uv run generate_image.py --prompt "edit instructions" --filename "output.png" --input-image "input.png"
"""

import argparse
import os
import sys
from pathlib import Path

# Aspect ratio presets for WeChat
ASPECT_PRESETS = {
    "cover": {"ratio": "2.35:1", "pixels": "1800x766", "desc": "头条封面 ultra-wide landscape"},
    "wide": {"ratio": "16:9", "pixels": "1920x1080", "desc": "正文宽图 landscape"},
    "standard": {"ratio": "4:3", "pixels": "1440x1080", "desc": "正文方图 landscape"},
    "square": {"ratio": "1:1", "pixels": "1080x1080", "desc": "方图"},
}


def get_api_key(provided_key: str | None) -> str | None:
    """Get API key from argument first, then environment."""
    if provided_key:
        return provided_key
    return os.environ.get("GEMINI_API_KEY")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for WeChat (公众号) using Gemini 3 Pro Image"
    )
    parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="Image description/prompt"
    )
    parser.add_argument(
        "--filename", "-f",
        required=True,
        help="Output filename (e.g., wechat-cover.png)"
    )
    parser.add_argument(
        "--input-image", "-i",
        help="Optional input image path for editing/modification"
    )
    parser.add_argument(
        "--aspect", "-a",
        choices=["cover", "wide", "standard", "square"],
        default="wide",
        help="Aspect ratio preset: cover (2.35:1), wide (16:9, default), standard (4:3), square (1:1)"
    )
    parser.add_argument(
        "--resolution", "-r",
        choices=["1K", "2K", "4K"],
        default="2K",
        help="Output resolution: 1K, 2K (default), or 4K"
    )
    parser.add_argument(
        "--api-key", "-k",
        help="Gemini API key (overrides GEMINI_API_KEY env var)"
    )

    args = parser.parse_args()

    # Get API key
    api_key = get_api_key(args.api_key)
    if not api_key:
        print("Error: No API key provided.", file=sys.stderr)
        print("Please either:", file=sys.stderr)
        print("  1. Provide --api-key argument", file=sys.stderr)
        print("  2. Set GEMINI_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)

    # Import here after checking API key to avoid slow import on error
    from google import genai
    from google.genai import types
    from PIL import Image as PILImage

    # Initialise client
    client = genai.Client(api_key=api_key)

    # Set up output path
    output_path = Path(args.filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Get aspect ratio info
    aspect = ASPECT_PRESETS[args.aspect]

    # Load input image if provided
    input_image = None
    output_resolution = args.resolution
    if args.input_image:
        try:
            input_image = PILImage.open(args.input_image)
            print(f"Loaded input image: {args.input_image}")

            if args.resolution == "2K":  # Default value
                width, height = input_image.size
                max_dim = max(width, height)
                if max_dim >= 3000:
                    output_resolution = "4K"
                elif max_dim >= 1500:
                    output_resolution = "2K"
                else:
                    output_resolution = "1K"
                print(f"Auto-detected resolution: {output_resolution} (from input {width}x{height})")
        except Exception as e:
            print(f"Error loading input image: {e}", file=sys.stderr)
            sys.exit(1)

    # Build contents (image first if editing, prompt only if generating)
    if input_image:
        contents = [input_image, args.prompt]
        print(f"Editing image with resolution {output_resolution}...")
    else:
        contents = args.prompt
        print(f"Generating WeChat image ({aspect['desc']}, {aspect['ratio']}) with resolution {output_resolution}...")

    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(
                    image_size=output_resolution
                )
            )
        )

        # Process response and convert to PNG
        image_saved = False
        for part in response.parts:
            if part.text is not None:
                print(f"Model response: {part.text}")
            elif part.inline_data is not None:
                from io import BytesIO

                image_data = part.inline_data.data
                if isinstance(image_data, str):
                    import base64
                    image_data = base64.b64decode(image_data)

                image = PILImage.open(BytesIO(image_data))

                # Ensure RGB mode for PNG
                if image.mode == 'RGBA':
                    rgb_image = PILImage.new('RGB', image.size, (255, 255, 255))
                    rgb_image.paste(image, mask=image.split()[3])
                    rgb_image.save(str(output_path), 'PNG')
                elif image.mode == 'RGB':
                    image.save(str(output_path), 'PNG')
                else:
                    image.convert('RGB').save(str(output_path), 'PNG')
                image_saved = True

        if image_saved:
            full_path = output_path.resolve()
            print(f"\nImage saved: {full_path}")

            # Report image dimensions and check aspect ratio
            saved_img = PILImage.open(str(output_path))
            w, h = saved_img.size
            actual_ratio = w / h

            # Calculate expected ratio from preset
            ratio_parts = aspect["ratio"].split(":")
            expected_ratio = float(ratio_parts[0]) / float(ratio_parts[1])

            print(f"Dimensions: {w}x{h} (ratio: {actual_ratio:.2f}, expected {aspect['ratio']} = {expected_ratio:.2f})")
            if abs(actual_ratio - expected_ratio) > 0.15:
                print(f"⚠️  Warning: Image ratio {actual_ratio:.2f} differs from expected {aspect['ratio']} ({expected_ratio:.2f}). Consider regenerating.")

            # Special warning for cover safe zone
            if args.aspect == "cover":
                print(f"📌 Cover safe zone reminder: Core content must be within the center {h}x{h} square area for WeChat Moments cropping.")
        else:
            print("Error: No image was generated in the response.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error generating image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
