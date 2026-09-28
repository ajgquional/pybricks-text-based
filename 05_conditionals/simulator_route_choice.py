"""
Route Choice in the GearsBot Simulator

This program demonstrates how conditionals can select different
movement routes by changing the speed and turn rate passed
directly to robot.drive().
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
DRIVE_SPEED = 200  # Forward speed in millimeters per second.
TURN_RATE = 90  # Turning rate in degrees per second.
FORWARD_TIME = 1000  # Initial straight movement time.
TURN_TIME = 1000  # Duration of the turning movement.
ROUTE_TIME = 1000  # Movement time after selecting a route.

ROUTE = "left"  # Change to "left", "right", or "straight".

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Selected route:", ROUTE)

robot.drive(DRIVE_SPEED, 0)  # Drive toward the route junction.
wait(FORWARD_TIME)
robot.stop()

if ROUTE == "left":
    robot.drive(0, -TURN_RATE)  # Turn left in place.
    wait(TURN_TIME)
    robot.stop()

    robot.drive(DRIVE_SPEED, 0)  # Continue along the left route.
    wait(ROUTE_TIME)

elif ROUTE == "right":
    robot.drive(0, TURN_RATE)  # Turn right in place.
    wait(TURN_TIME)
    robot.stop()

    robot.drive(DRIVE_SPEED, 0)  # Continue along the right route.
    wait(ROUTE_TIME)

elif ROUTE == "straight":
    robot.drive(DRIVE_SPEED, 0)  # Continue straight ahead.
    wait(ROUTE_TIME)

else:
    print("Unknown route. Robot will stop.")

robot.stop()  # Stop after completing the selected route.