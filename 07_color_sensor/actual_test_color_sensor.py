
"""
Color Sensor Test - Actual LEGO SPIKE Prime

This program continuously reads the color and reflected light
intensity detected by the SPIKE Prime Color Sensor.

Place the sensor over different colored surfaces and observe
the readings in the Pybricks output console.

Expected surfaces:
    Red, Green, Blue, and White.

Hardware:
    LEGO SPIKE Prime Hub
    SPIKE Prime Color Sensor connected to Port C
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Icon
from pybricks.tools import wait


hub = PrimeHub()  # Initialize the SPIKE Prime Hub.
color_sensor = ColorSensor(Port.C)  # Initialize the color sensor on Port C.

hub.display.icon(Icon.HAPPY)  # Indicate that the program has started.

print("Color sensor test started.")
print("Place the sensor over different colored surfaces.")
print("Press Stop in Pybricks to end the test.")

while True:
    detected_color = color_sensor.color()  # Read the detected color.
    reflection = color_sensor.reflection()  # Read reflected light intensity.

    print("Color:", detected_color, "| Reflection:", reflection)

    wait(500)  # Wait half a second before the next reading.
