"""
Patrol Movement on an Actual SPIKE Prime Robot

This program demonstrates a practical use of a for loop.
The robot repeatedly moves forward and backward along
the same path to simulate a simple patrol.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
PATROL_DISTANCE = 400  # Distance traveled in each direction.
PATROL_ROUNDS = 3  # Number of complete patrol rounds.
PAUSE_TIME = 500  # Pause at each end of the patrol path.

hub = PrimeHub()  # Create an object representing the SPIKE Prime hub.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Patrol demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

for round_number in range(PATROL_ROUNDS):
    print("Patrol round:", round_number + 1)
    hub.display.char(str(round_number + 1))  # Show the patrol round.

    robot.straight(PATROL_DISTANCE)  # Move to the far end.
    wait(PAUSE_TIME)

    hub.display.icon(Icon.DOWN)  # Show that the robot will move back.
    robot.straight(-PATROL_DISTANCE)  # Return to the starting point.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Patrol demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.