
"""
Line Follower - GearsBot Simulator

Follow the right edge of a black line using reflected
light intensity and conditional statements.

World: Line Following Challenges
Challenge: Simple Curves
"""

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Wheel diameter in millimeters.
AXLE_TRACK = 152  # Distance between wheels in millimeters.

DRIVE_SPEED = 100  # Forward speed in millimeters per second.
TURN_RATE = 60  # Steering rate in degrees per second.

BLACK_REFLECTION = 10  # Estimated reflection of the black line.
WHITE_REFLECTION = 90  # Estimated reflection of the white floor.

# Calculate the threshold between black and white.
THRESHOLD = (BLACK_REFLECTION + WHITE_REFLECTION) / 2

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)

robot.settings(
    straight_speed=100,
    straight_acceleration=300,
    turn_rate=90,
    turn_acceleration=180,
)

print("Starting Line Follower!")
print("Reflection threshold:", THRESHOLD)

while True:
    # Measure the reflected light intensity.
    reflection = color_sensor.reflection()

    if reflection < THRESHOLD:
        # Dark surface detected: steer right.
        robot.drive(DRIVE_SPEED, TURN_RATE)

    else:
        # Light surface detected: steer left.
        robot.drive(DRIVE_SPEED, -TURN_RATE)

    wait(20)
