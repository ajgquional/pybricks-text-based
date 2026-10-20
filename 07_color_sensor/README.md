# 🎨 Lesson 7: Color Sensor

In this lesson, we'll learn how to use the **Color Sensor** to help a robot recognize colors and respond to its surroundings.

Instead of moving along a fixed path, our robot will make decisions based on the colors it detects. We'll begin by testing the sensor, then create a robot that stops at a red marker, and finally navigate a maze using colored instructions.

We'll use the [GearsBot Simulator](https://gears.aposteriori.com.sg/) before testing our programs on an actual LEGO SPIKE Prime robot.

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:

- Initialize and use a Color Sensor in Pybricks.
- Detect colors using `color()`.
- Measure reflected light intensity using `reflection()`.
- Combine sensor readings with loops and conditional statements.
- Program a robot to react to different colored markers.

## 🔍 Understanding the Color Sensor

A Color Sensor allows a robot to detect the color of a nearby surface and measure how much light it reflects.

In Pybricks, we can use two important methods:

| Method | Description | Example |
|---|---|---|
| `color()` | Detects the color of a nearby surface | `color_sensor.color()` |
| `reflection()` | Measures reflected light intensity from 0% to 100% | `color_sensor.reflection()` |

### Initializing the Color Sensor

**GearsBot Simulator**

```python
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

color_sensor = ColorSensor(Port.S1)
```

**Actual LEGO SPIKE Prime**

```python
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port

color_sensor = ColorSensor(Port.C)
```

The port depends on where the sensor is connected.

### Detecting Colors

We can use `color()` to identify a surface color.

```python
from pybricks.parameters import Color

detected_color = color_sensor.color()

if detected_color == Color.RED:
    print("Red detected!")
elif detected_color == Color.BLUE:
    print("Blue detected!")
elif detected_color == Color.GREEN:
    print("Green detected!")
```

The `Color` constants make it easier to compare detected colors without remembering their numerical values.

### Measuring Reflected Light

We can use `reflection()` to measure how much light a surface reflects.

```python
brightness = color_sensor.reflection()

print("Reflected light:", brightness)
```

A light-colored surface generally reflects more light than a dark-colored surface.

This will become especially useful when we create a **line-following robot**.

## 🌍 Loading Custom Worlds in GearsBot

Some activities use custom worlds with colored markers on the ground.

The world files are located in the [`worlds/`](worlds/) directory. Each world consists of a PNG image and a corresponding JSON configuration file.

### Step 1: Download the World JSON File

1. Open the [`worlds/`](worlds/) directory on GitHub.
2. Select the JSON file for your chosen activity.
3. Click the **Download raw file** button to save the JSON file to your computer.

Available world configurations:

| Activity | World JSON |
|---|---|
| Color Sensor Test | [`color_test_world.json`](worlds/color_test_world.json) |
| Forward Until Red | [`color_stop_world.json`](worlds/color_stop_world.json) |
| Color Command Maze | [`color_maze_world.json`](worlds/color_maze_world.json) |

### Step 2: Import the World into GearsBot

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Navigate to the **Worlds** tab.
3. Select the option to import a custom world.
4. Choose the JSON file you downloaded.
5. Load the imported world into the simulator.

The custom ground image should appear in the simulation.

**Note:** The JSON files reference PNG images hosted on GitHub, so an internet connection may be needed to load the images.

### Step 3: Prepare the Robot

1. Select or configure a robot with two drive motors.
2. Connect the left motor to **Port A** and the right motor to **Port B**.
3. Add a Color Sensor on **Port S1**.
4. Position the Color Sensor so it faces the ground.
5. Check the robot's starting position and direction.

### Step 4: Run the Program

1. Open the corresponding `simulator_*.py` script.
2. Copy the code into GearsBot's Python editor.
3. Run the simulation.
4. Observe how the robot responds to the colored markers.

## 🤖 Activities

### Activity 1: Color Sensor Test

**Goal:** Detect different colors and measure their reflected light intensity.

**World:** [`color_test_world.json`](worlds/color_test_world.json)

**Scripts:**
- [`simulator_test_color_sensor.py`](simulator_test_color_sensor.py)
- [`actual_test_color_sensor.py`](actual_test_color_sensor.py)

The robot reads the Color Sensor and prints the detected color and reflected light intensity.

**Try this:** Move the robot over different colored patches. Do all colors produce the same reflected light intensity?

### Activity 2: Forward Until Red

**Goal:** Make the robot drive forward and stop when it detects red.

**World:** [`color_stop_world.json`](worlds/color_stop_world.json)

**Scripts:**
- [`simulator_forward_until_red.py`](simulator_forward_until_red.py)
- [`actual_forward_until_red.py`](actual_forward_until_red.py)

The robot drives forward while continuously checking the Color Sensor. Once it detects red, it stops.

**Key concept:** A `while` loop can keep the robot moving until a sensor condition is satisfied.

**Try this:** Change `DRIVE_SPEED`. How does increasing the speed affect the robot's stopping position?

### Activity 3: Color Command Maze

**Goal:** Navigate a maze using colored markers as movement instructions.

**World:** [`color_maze_world.json`](worlds/color_maze_world.json)

**Scripts:**
- [`simulator_color_maze.py`](simulator_color_maze.py)
- [`actual_color_maze.py`](actual_color_maze.py)

Each marker tells the robot what to do next.

| Detected color | Robot action |
|---|---|
| 🔵 Blue | Turn left |
| 🟢 Green | Turn right |
| 🔴 Red | Stop |

The robot follows the instructions until it reaches the red marker.

**Key concept:** Combining loops and conditionals allows a robot to navigate based on sensor feedback.

**Try this:** Rearrange the markers or modify the turning angles. Can you create a different route?

### Activity 4: Line Following 🚧

**Goal:** Make the robot follow a line by continuously measuring reflected light intensity.

This activity will introduce feedback-based steering using `reflection()`.

*Coming soon.*

## 🧱 Testing on an Actual LEGO SPIKE Prime

After completing the simulator activities, you can test the corresponding `actual_*.py` programs on a physical robot.

Before running a program:

1. Connect the drive motors to Ports A and B.
2. Connect the Color Sensor to Port C.
3. Open [Pybricks Code](https://code.pybricks.com/).
4. Connect your SPIKE Prime Hub running Pybricks firmware.
5. Open or paste the appropriate `actual_*.py` script.
6. Check the wheel dimensions, speed settings, and sensor position.
7. Run the program and observe the robot's behavior.

For the physical Color Command Maze, you can use colored paper, tape, or LEGO bricks as navigation markers. When using upright LEGO bricks, point the Color Sensor forward rather than downward, and leave enough space for the robot to turn without colliding with the markers.

**Important:** The physical robot may behave differently from the simulator. You may need to calibrate `WHEEL_DIAMETER`, `AXLE_TRACK`, `DRIVE_SPEED`, and `EXIT_DISTANCE`.

## 📚 References

- [Pybricks Documentation](https://docs.pybricks.com/)
- [Pybricks Color Sensor API](https://docs.pybricks.com/en/latest/pupdevices/colorsensor.html)
- [Pybricks DriveBase API](https://docs.pybricks.com/en/latest/robotics.html)
- [GearsBot Simulator](https://gears.aposteriori.com.sg/)

---

**Next lesson activity:** Line Following — teaching the robot to continuously correct its movement using reflected light intensity.