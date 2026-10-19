
"""
GearsBot World Image Generator

Generate reusable ground images for robotics lessons using Pillow.

Example:
    python generate_world.py --preset color-test --output 07_color_sensor/worlds/color_test.png
"""

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw


# Available world presets.
PRESETS = {
    "color-test": "Three colored patches for testing a color sensor.",
}


def create_color_test(draw, width, height):
    """
    Draw a simple arena with red, green, and blue patches.

    Args:
        draw: Pillow drawing object.
        width: Image width in pixels.
        height: Image height in pixels.
    """
    colors = ["#E53935", "#43A047", "#1E88E5"]

    # Reserve space around and between the color patches.
    margin_x = width * 0.08
    gap = width * 0.06

    patch_width = (width - 2 * margin_x - 2 * gap) / 3
    patch_height = height * 0.45

    top = (height - patch_height) / 2
    bottom = top + patch_height

    # Draw three equally sized color patches.
    for index, color in enumerate(colors):
        left = margin_x + index * (patch_width + gap)
        right = left + patch_width

        draw.rectangle(
            (round(left), round(top), round(right), round(bottom)),
            fill=color,
        )


def generate_world(preset, width, height, background, output):
    """
    Generate a world image using the selected preset.

    Args:
        preset: Name of the world preset.
        width: Image width in pixels.
        height: Image height in pixels.
        background: Background color.
        output: Destination path of the PNG file.
    """
    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)

    if preset == "color-test":
        create_color_test(draw, width, height)

    # Create the output folder if it does not exist.
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image.save(output_path, format="PNG")

    print(f"World preset: {preset}")
    print(f"Image size: {width} x {height}")
    print(f"Saved to: {output_path.resolve()}")


def main():
    """Read command-line arguments and generate the world image."""
    parser = argparse.ArgumentParser(
        description="Generate custom ground images for GearsBot.",
    )

    parser.add_argument(
        "--preset",
        choices=PRESETS.keys(),
        default="color-test",
        help="World layout to generate (default: color-test).",
    )

    parser.add_argument(
        "--width",
        type=int,
        default=1200,
        help="Image width in pixels (default: 1200).",
    )

    parser.add_argument(
        "--height",
        type=int,
        default=800,
        help="Image height in pixels (default: 800).",
    )

    parser.add_argument(
        "--background",
        default="white",
        help="Background color (default: white).",
    )

    parser.add_argument(
        "--output",
        default="world.png",
        help="Output PNG path (default: world.png).",
    )

    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="Display available world presets and exit.",
    )

    args = parser.parse_args()

    if args.list_presets:
        print("Available world presets:")

        for name, description in PRESETS.items():
            print(f"  {name}: {description}")

        return

    if args.width <= 0 or args.height <= 0:
        parser.error("Image dimensions must be positive integers.")

    if args.width < 300 or args.height < 200:
        parser.error("Minimum image dimensions are 300 x 200 pixels.")

    try:
        background = ImageColor.getrgb(args.background)
    except ValueError:
        parser.error("Invalid background color.")

    generate_world(
        preset=args.preset,
        width=args.width,
        height=args.height,
        background=background,
        output=args.output,
    )


if __name__ == "__main__":
    main()
