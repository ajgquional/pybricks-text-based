"""
Mission Selector in the GearsBot Simulator

This program demonstrates how functions can organize robot behavior
into reusable skills and complete missions. The student can choose
which mission to run by changing the MISSION variable.

The functions are arranged from simple to more advanced examples.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.

MISSION = "patrol"  # Change to "forward", "square", "patrol", or "zigzag".

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.


def move_forward(distance):
    """
    Move the robot forward by a specified distance.

    Args:
        distance: Distance to travel in millimeters.
    """
    robot.straight(distance)


def turn_robot(angle):
    """
    Turn the robot by a specified angle.

    Args:
        angle: Turning angle in degrees.
            Positive values turn one direction.
            Negative values turn the opposite direction.
    """
    robot.turn(angle)


def drive_square(side_length):
    """
    Drive the robot in a square.

    Args:
        side_length: Length of each side in millimeters.
    """
    for _ in range(4):
        move_forward(side_length)
        turn_robot(90)


def patrol(distance, rounds):
    """
    Move forward and backward repeatedly to simulate a patrol.

    Args:
        distance: Patrol distance in millimeters.
        rounds: Number of complete forward-and-back patrol rounds.
    """
    for _ in range(rounds):
        move_forward(distance)
        move_forward(-distance)


def zigzag(distance, turn_angle, segments):
    """
    Drive the robot in an alternating zigzag pattern.

    Args:
        distance: Distance traveled during each segment in millimeters.
        turn_angle: Turning angle used after each segment.
        segments: Number of zigzag segments to complete.
    """
    for segment in range(segments):
        move_forward(distance)

        if segment % 2 == 0:
            turn_robot(turn_angle)
        else:
            turn_robot(-turn_angle)


def calculate_patrol_distance(distance, rounds):
    """
    Calculate the total distance traveled during a patrol.

    Args:
        distance: Distance traveled in one direction in millimeters.
        rounds: Number of complete patrol rounds.

    Returns:
        Total patrol distance in millimeters.
    """
    return distance * 2 * rounds


print("Selected mission:", MISSION)

if MISSION == "forward":
    move_forward(500)

elif MISSION == "square":
    drive_square(300)

elif MISSION == "patrol":
    patrol_distance = 400
    patrol_rounds = 3

    total_distance = calculate_patrol_distance(
        patrol_distance,
        patrol_rounds,
    )

    print("Planned patrol distance:", total_distance, "mm")
    patrol(patrol_distance, patrol_rounds)

elif MISSION == "zigzag":
    zigzag(
        distance=250,
        turn_angle=45,
        segments=6,
    )

else:
    print("Unknown mission.")

robot.stop()  # Make sure the robot is stopped after the selected mission.

print("Mission finished.")