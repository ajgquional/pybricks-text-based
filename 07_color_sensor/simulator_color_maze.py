
"""
Color Maze - GearsBot Simulator

Navigate the maze by following colored markers.

World:
    color_maze_world.json

Color instructions:
    Blue  -> Turn left.
    Green -> Turn right.
    Red   -> Stop.
"""

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56
AXLE_TRACK = 152
DRIVE_SPEED = 150
EXIT_DISTANCE = 250  # Distance to move after turning (mm).

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)

# for fine-tuning of the robot's movement
robot.settings(straight_speed=DRIVE_SPEED, straight_acceleration=500, turn_rate=100, turn_acceleration=200)

print("Starting Color Maze!")

while True:
    robot.drive(DRIVE_SPEED, 0)  # Keep moving forward.

    # Wait until the robot detects a navigation color.
    while color_sensor.color() not in (Color.BLUE, Color.GREEN, Color.RED):
        wait(20)

    robot.stop()  # Stop before following the color instruction.

    detected_color = color_sensor.color()

    if detected_color == Color.BLUE:
        print("Blue detected: Turn left.")
        robot.turn(-95)
        robot.straight(EXIT_DISTANCE)

    elif detected_color == Color.GREEN:
        print("Green detected: Turn right.")
        robot.turn(95)
        robot.straight(EXIT_DISTANCE)

    elif detected_color == Color.RED:
        print("Red detected: Mission complete!")
        break

robot.stop()
print("Color Maze finished!")
