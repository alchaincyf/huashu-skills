#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
#     "httpx[socks]",
# ]
# ///
"""
Generate images for Xiaohongshu (小红书) posts using Gemini 3 Pro Image API.

Default: 3:4 portrait, 2K resolution (optimal for 小红书).

Usage:
    uv run generate_image.py --prompt "image description" --filename "output.png" [--resolution 1K|2K|4K] [--api-key KEY]
    uv run generate_image.py --prompt "editing instructions" --filename "output.png" --input-image "input.png"
    uv run generate_image.py --prompt "create meme with these" --filename "out.png" -i "ref1.png" -i "ref2.png"
"""

import argparse
import os
import sys
from pathlib import Path


def get_api_key(provided_key: str | None) -> str | None:
    """Get API key from argument first, then environment."""
    if provided_key:
        return provided_key
    return os.environ.get("GEMINI_API_KEY")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for Xiaohongshu (小红书) using Gemini 3 Pro Image"
    )
    parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="Image description/prompt"
    )
    parser.add_argument(
        "--filename", "-f",
        required=True,
        help="Output filename (e.g., xhs-cover.png)"
    )
    parser.add_argument(
        "--input-image", "-i",
        action="append",
        help="Input image path(s) for reference/editing. Can be used multiple times: -i img1.png -i img2.png"
    )
    parser.add_argument(
        "--resolution", "-r",
        choices=["1K", "2K", "4K"],
        default="2K",
        help="Output resolution: 1K, 2K (default for XHS), or 4K"
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

    # Load input images if provided
    input_images = []
    output_resolution = args.resolution
    if args.input_image:
        for img_path in args.input_image:
            try:
                img = PILImage.open(img_path)
                input_images.append(img)
                print(f"Loaded input image: {img_path} ({img.size[0]}x{img.size[1]})")
            except Exception as e:
                print(f"Error loading input image {img_path}: {e}", file=sys.stderr)
                sys.exit(1)

        # Auto-detect resolution from the largest input image
        if args.resolution == "2K":  # Default value for XHS
            max_dim = max(max(img.size) for img in input_images)
            if max_dim >= 3000:
                output_resolution = "4K"
            elif max_dim >= 1500:
                output_resolution = "2K"
            else:
                output_resolution = "1K"
            print(f"Auto-detected resolution: {output_resolution}")

    # Build contents (images first if editing, prompt only if generating)
    if input_images:
        contents = [*input_images, args.prompt]
        print(f"Generating with {len(input_images)} reference image(s), resolution {output_resolution}...")
    else:
        contents = args.prompt
        print(f"Generating XHS image (3:4 portrait) with resolution {output_resolution}...")

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

            # Report image dimensions
            saved_img = PILImage.open(str(output_path))
            w, h = saved_img.size
            ratio = w / h
            expected_ratio = 3 / 4  # 0.75
            print(f"Dimensions: {w}x{h} (ratio: {ratio:.2f}, expected 3:4 = {expected_ratio:.2f})")
            if abs(ratio - expected_ratio) > 0.1:
                print(f"⚠️  Warning: Image ratio {ratio:.2f} differs from expected 3:4 ({expected_ratio:.2f}). Consider regenerating.")
        else:
            print("Error: No image was generated in the response.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error generating image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
