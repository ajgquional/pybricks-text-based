"""
Individual Motor Control in the GearsBot Simulator

This program demonstrates how to control one motor using Pybricks.
The motor runs at different speeds and directions before rotating
through specific angles.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


MOTOR_SPEED_SLOW = 200  # Slow motor speed in degrees per second.
MOTOR_SPEED_FAST = 500  # Fast motor speed in degrees per second.
RUN_TIME = 1000  # Motor running time in milliseconds.
PAUSE_TIME = 500  # Pause between motor actions in milliseconds.

motor = Motor(Port.A)  # Create the motor connected to Port A.

print("MOTOR CONTROL DEMONSTRATION STARTED.")
wait(PAUSE_TIME) 

######################################################################

print('\n' + '=' * 70)  # Print a separator line for clarity.
print("Slow motor control demonstration started.")
motor.run(MOTOR_SPEED_SLOW)  # Run the motor forward slowly.
wait(RUN_TIME)  # Allow the motor to run for 1 second.
motor.stop()  # Stop the motor.
print("Slow motor control demonstration finished.")
wait(PAUSE_TIME)  # Pause before the next action.
print('=' * 70)  # Print a separator line for clarity.  

######################################################################

print('\n' + '=' * 70)  # Print a separator line for clarity.   
print("Fast motor control demonstration started.")
motor.run(MOTOR_SPEED_FAST)  # Run the motor forward faster.
wait(RUN_TIME)  # Allow the motor to run for 1 second.
motor.stop()  # Stop the motor.
print("Fast motor control demonstration finished.")
wait(PAUSE_TIME)  # Pause before reversing the motor.
print('=' * 70)  # Print a separator line for clarity.  

######################################################################

print('\n' + '=' * 70)  # Print a separator line for clarity. 
print("Reverse motor control demonstration started.")
motor.run(-MOTOR_SPEED_SLOW)  # Run backward using negative speed.
wait(RUN_TIME)  # Allow the motor to run backward for 1 second.
motor.stop()  # Stop the motor.
print("Reverse motor control demonstration finished.")
wait(PAUSE_TIME)  # Pause before the angle-based movements.
print('=' * 70)  # Print a separator line for clarity.  

######################################################################

print('\n' + '=' * 70)  # Print a separator line for clarity. 
print("Angle-based motor control demonstration started.")
motor.run_angle(
    MOTOR_SPEED_SLOW,
    360,
)  # Rotate the motor forward by one complete revolution.
print("Angle-based motor control demonstration finished.")
wait(PAUSE_TIME)  # Pause before reversing the motor.
print('=' * 70)  # Print a separator line for clarity. 

######################################################################

print('\n' + '=' * 70)  # Print a separator line for clarity. 
print("Reverse angle-based motor control demonstration started.")
motor.run_angle(
    MOTOR_SPEED_SLOW,
    -180,
)  # Rotate the motor backward by half a revolution.
print("Reverse angle-based motor control demonstration finished.")
print('=' * 70)  # Print a separator line for clarity. 

######################################################################

print("\nMOTOR CONTROL DEMONSTRATION FINISHED.")