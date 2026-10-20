
"""
GearsBot World Image Generator

Generate reusable ground images for robotics lessons using Pillow.

Examples:
    python generate_world.py --preset color-test --output color_test.png
    python generate_world.py --preset color-stop --output color_stop.png
"""

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw


# Available world presets.
PRESETS = {
    "color-test": "Three colored patches for testing a color sensor.",
    "color-stop": "Straight driving arena with a red stopping zone.",
    "color-maze": "Square arena with color-controlled navigation markers.",
}


def create_color_test(draw, width, height):
    """
    Draw an arena with red, green, and blue patches.

    Args:
        draw: Pillow drawing object.
        width: Image width in pixels.
        height: Image height in pixels.
    """
    colors = ["#E53935", "#43A047", "#1E88E5"]

    margin_x = width * 0.08
    gap = width * 0.06

    patch_width = (width - 2 * margin_x - 2 * gap) / 3
    patch_height = height * 0.45

    top = (height - patch_height) / 2
    bottom = top + patch_height

    for index, color in enumerate(colors):
        left = margin_x + index * (patch_width + gap)
        right = left + patch_width

        draw.rectangle(
            (round(left), round(top), round(right), round(bottom)),
            fill=color,
        )


def create_color_stop(draw, width, height):
    """
    Draw a straight driving arena with a red strip near the top.

    The robot should start near the bottom of the image and
    travel upward until its color sensor detects red.

    Args:
        draw: Pillow drawing object.
        width: Image width in pixels.
        height: Image height in pixels.
    """
    margin_x = width * 0.08
    margin_y = height * 0.08

    # Draw the light-gray driving surface.
    draw.rectangle(
        (
            round(margin_x),
            round(margin_y),
            round(width - margin_x),
            round(height - margin_y),
        ),
        fill="#F1F1F1",
    )

    # Draw the red stopping zone near the top.
    red_top = height * 0.14
    red_bottom = height * 0.30

    draw.rectangle(
        (
            round(margin_x),
            round(red_top),
            round(width - margin_x),
            round(red_bottom),
        ),
        fill="#E53935",
    )



def create_color_maze(draw, width, height):
    """
    Draw a color-command maze with rectangular markers.

    The robot starts near the bottom center, facing upward.

    Navigation sequence:
        Blue  -> Turn left.
        Green -> Turn right.
        Green -> Turn right.
        Blue  -> Turn left.
        Red   -> Stop.

    The markers are narrow in the direction of travel
    and wider across the robot's path.

    Args:
        draw: Pillow drawing object.
        width: Image width in pixels.
        height: Image height in pixels.
    """
    colors = {
        "blue": "#1E88E5",
        "green": "#43A047",
        "red": "#E53935",
    }

    # Marker positions from the original Color Maze.
    # Each tuple contains (x, y, color, incoming direction).
    markers = [
        (0.50, 0.75, "blue", "vertical"),
        (0.20, 0.75, "green", "horizontal"),
        (0.20, 0.40, "green", "vertical"),
        (0.80, 0.40, "blue", "horizontal"),
        (0.80, 0.16, "red", "vertical"),
    ]

    # Marker dimensions relative to the image size.
    marker_width = min(width, height) * 0.10
    marker_thickness = min(width, height) * 0.025

    for x_fraction, y_fraction, color, direction in markers:
        center_x = width * x_fraction
        center_y = height * y_fraction

        # Orient each marker across the incoming robot path.
        if direction == "vertical":
            half_width = marker_width / 2
            half_height = marker_thickness / 2
        else:
            half_width = marker_thickness / 2
            half_height = marker_width / 2

        draw.rectangle(
            (
                round(center_x - half_width),
                round(center_y - half_height),
                round(center_x + half_width),
                round(center_y + half_height),
            ),
            fill=colors[color],
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

    elif preset == "color-stop":
        create_color_stop(draw, width, height)

    elif preset == "color-maze":
        create_color_maze(draw, width, height)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image.save(output_path, format="PNG")

    print(f"World preset: {preset}")
    print(f"Image size: {width} x {height}")
    print(f"Saved to: {output_path.resolve()}")


def main():
    """Read CLI arguments and generate the selected world image."""
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
