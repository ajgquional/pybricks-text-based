
"""
Color Sensor Test - GearsBot Simulator

Test whether the color sensor detects the colored patches
in the custom color-test world.

Expected colors:
    Red, Green, Blue, and White (background).

Place the robot over different patches and observe the
detected colors in the simulator's console.
"""

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait


# Initialize the color sensor.
# Change Port.S1 if your simulator robot uses a different port.
color_sensor = ColorSensor(Port.S1)

print("Color sensor test started.")
print("Move the robot over the colored patches.")
print("Press Stop in GearsBot to end the test.")

while True:
    detected_color = color_sensor.color()  # Read the current color.
    reflection = color_sensor.reflection()  # Read reflected light intensity.

    print("Color:", detected_color, "| Reflection:", reflection)

    wait(500)  # Wait half a second before reading again.
