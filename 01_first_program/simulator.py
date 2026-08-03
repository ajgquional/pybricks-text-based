"""
First Pybricks Program for the GearsBot Simulator

This program prints messages, rotates one motor forward, pauses,
rotates the motor backward, and then stops it.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


print("Hello, Pybricks!")  # Display a welcome message.

motor = Motor(Port.A)  # Create the motor connected to Port A.

print("The motor will rotate forward.")

motor.run(300)  # Rotate forward at 300 degrees per second.
wait(1000)  # Keep the motor running for 1 second.
motor.stop()  # Stop the motor.

wait(500)  # Pause for half a second.

print("The motor will rotate backward.")

motor.run(-300)  # Rotate backward at 300 degrees per second.
wait(1000)  # Keep the motor running for 1 second.
motor.stop()  # Stop the motor.

print("Program finished!")