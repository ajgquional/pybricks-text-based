"""
Patrol Movement in the GearsBot Simulator

This program demonstrates a practical use of a for loop.
The robot repeatedly moves forward and backward along
the same path to simulate a simple patrol.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
PATROL_DISTANCE = 400  # Distance traveled in each direction.
PATROL_ROUNDS = 3  # Number of complete patrol rounds.
PAUSE_TIME = 500  # Pause at each end of the patrol path.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Patrol demonstration started.")

for round_number in range(PATROL_ROUNDS):
    print("Patrol round:", round_number + 1)

    robot.straight(PATROL_DISTANCE)  # Move to the far end.
    wait(PAUSE_TIME)

    robot.straight(-PATROL_DISTANCE)  # Return to the starting point.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Patrol demonstration finished.")