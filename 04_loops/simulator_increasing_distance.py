"""
Increasing Distance Movement in the GearsBot Simulator

This program demonstrates how the loop variable can be used
in a calculation. The robot moves farther during each repetition.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
BASE_DISTANCE = 100  # Starting movement distance in millimeters.
REPETITIONS = 5  # Number of movements.
PAUSE_TIME = 300  # Pause between movements in milliseconds.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Increasing distance demonstration started.")

for repetition in range(1, REPETITIONS + 1):
    move_distance = BASE_DISTANCE * repetition  # Increase each movement.

    print("Repetition:", repetition)
    print("Distance:", move_distance, "mm")

    robot.straight(move_distance)  # Move using the calculated distance.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Increasing distance demonstration finished.")