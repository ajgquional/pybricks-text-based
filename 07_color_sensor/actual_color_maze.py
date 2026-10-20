
"""
Color Command Maze - Actual LEGO SPIKE Prime

Navigate a maze by following colored ground markers.

Color instructions:
    Blue  -> Turn left.
    Green -> Turn right.
    Red   -> Stop.

Hub status light:
    Green  -> Moving forward.
    Yellow -> Turning left.
    Orange -> Turning right.
    Red    -> Mission completed.

Hardware:
    Left Motor: Port A
    Right Motor: Port B
    Color Sensor: Port C
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Wheel diameter in millimeters.
AXLE_TRACK = 152  # Distance between wheels in millimeters.

DRIVE_SPEED = 200  # Forward speed in millimeters per second.
EXIT_DISTANCE = 250  # Distance traveled after turning (mm).

hub = PrimeHub()  # Initialize the SPIKE Prime Hub.
left_motor = Motor(Port.A)  # Initialize the left motor.
right_motor = Motor(Port.B)  # Initialize the right motor.
color_sensor = ColorSensor(Port.C)  # Initialize the Color Sensor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)

robot.settings(
    straight_speed=DRIVE_SPEED,
    straight_acceleration=300,
    turn_rate=90,
    turn_acceleration=180,
)  # Configure straight and turning movements.

print("Starting Color Maze!")

while True:
    hub.light.on(Color.GREEN)  # Green indicates forward movement.
    robot.drive(DRIVE_SPEED, 0)  # Keep moving forward.

    # Wait until the robot detects a navigation color.
    while color_sensor.color() not in (Color.BLUE, Color.GREEN, Color.RED):
        wait(20)

    robot.stop()  # Stop before following the color instruction.

    detected_color = color_sensor.color()

    if detected_color == Color.BLUE:
        print("Blue detected: Turn left.")
        hub.light.on(Color.YELLOW)  # Yellow indicates a left turn.
        robot.turn(-95)
        robot.straight(EXIT_DISTANCE)

    elif detected_color == Color.GREEN:
        print("Green detected: Turn right.")
        hub.light.on(Color.ORANGE)  # Orange indicates a right turn.
        robot.turn(95)
        robot.straight(EXIT_DISTANCE)

    elif detected_color == Color.RED:
        print("Red detected: Mission complete!")
        break

robot.stop()  # Ensure the robot stops.
hub.light.on(Color.RED)  # Red indicates mission completion.

print("Color Maze finished!")
