"""
First Pybricks Program for an Actual SPIKE Prime Robot

This program prints status messages, displays icons on the hub,
rotates one motor forward and backward, and then stops it.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port, Color # if the hub's LED color is to be varied, import Color; otherwise, omit it
from pybricks.pupdevices import Motor
from pybricks.tools import wait


MOTOR_SPEED = 300  # Motor speed in degrees per second.
RUN_TIME = 1000  # Motor running time in milliseconds.
PAUSE_TIME = 500  # Pause between motor actions in milliseconds.

hub = PrimeHub()  # Create an object representing the SPIKE Prime hub.
motor = Motor(Port.A)  # Create the motor connected to Port A.

print("Hello, Pybricks!")  # Display a welcome message in the console.
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)  # Keep the starting icon visible briefly.

print("The motor will rotate forward.")
hub.display.icon(Icon.UP)  # Show the forward motor direction.

motor.run(MOTOR_SPEED)  # Rotate forward at 300 degrees per second.
wait(RUN_TIME)  # Keep the motor running for 1 second.
motor.stop()  # Stop the motor.

hub.display.off()  # Turn off all LEDs during the pause.
wait(PAUSE_TIME)  # Pause before rotating backward.

print("The motor will rotate backward.")
hub.display.icon(Icon.DOWN)  # Show the backward motor direction.

motor.run(-MOTOR_SPEED)  # Rotate backward at 300 degrees per second.
wait(RUN_TIME)  # Keep the motor running for 1 second.
motor.stop()  # Stop the motor.

print("Program finished!")
hub.display.icon(Icon.HAPPY)  # Show that the program finished.
wait(1000)  # Keep the completion icon visible for 1 second.
hub.display.off()  # Clear the light matrix.


# ------------------------------------------------------------
# Optional Hub Experiments
# ------------------------------------------------------------
# The PrimeHub object gives access to the built-in features of
# the SPIKE Prime hub, including its light matrix, status light,
# speaker, buttons, battery information, and motion sensor.
#
# Uncomment one experiment at a time to see what the hub can do.

# Display a letter on the 5 x 5 light matrix.
# hub.display.char("A")
# wait(1000)
# hub.display.off()

# Display a built-in icon on the light matrix.
# hub.display.icon(Icon.HAPPY)
# wait(1000)
# hub.display.off()

# Turn the hub's status light green.
# hub.light.on(Color.GREEN)
# wait(1000)
# hub.light.off()

# Blink the hub's status light red.
# hub.light.blink(Color.RED, [500, 500])
# wait(3000)
# hub.light.off()

# Play a short sound using the built-in speaker.
# hub.speaker.beep()

# Print the buttons that are currently being pressed.
# Press and hold a hub button before this line runs.
# print("Pressed buttons:", hub.buttons.pressed())