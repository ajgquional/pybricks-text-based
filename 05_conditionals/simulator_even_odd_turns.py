"""
Even and Odd Turns in the GearsBot Simulator

This program combines loops and conditionals. The robot alternates
its local turn rate depending on whether the repetition number
is odd or even.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
DRIVE_SPEED = 200  # Forward speed in millimeters per second.
TURN_RATE = 45  # Turning rate in degrees per second.
DRIVE_TIME = 800  # Duration of each curved movement.
REPETITIONS = 6  # Number of repetitions.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

for repetition in range(1, REPETITIONS + 1):
    print("Repetition:", repetition)

    if repetition % 2 == 0:
        turn_rate = TURN_RATE  # Curve in one direction.
        print("Even repetition: turning right.")
    else:
        turn_rate = -TURN_RATE  # Curve in the opposite direction.
        print("Odd repetition: turning left.")

    robot.drive(
        DRIVE_SPEED,
        turn_rate,
    )  # Drive using the locally selected turn rate.

    wait(DRIVE_TIME)  # Continue the curved movement briefly.

robot.stop()  # Stop the robot after all repetitions.