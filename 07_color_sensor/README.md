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

### Activity 4: Line Following — Simple Curves

**Goal:** Program a robot to follow a black line by continuously measuring reflected light intensity and adjusting its direction.

**World:** Line Following Challenges

**Challenge:** Simple Curves

**Script:** [`simulator_simple_curves_line_follower.py`](simulator_simple_curves_line_follower.py)

#### 🌍 Setting Up the Simulator

Unlike the previous activities, this activity uses a built-in GearsBot world. There is no need to download or import a custom JSON file.

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Navigate to the **Worlds** tab.
3. Select **Line Following Challenges**.
4. Select the **Simple Curves** challenge.
5. Make sure the robot has a downward-facing Color Sensor connected to Port S1.
6. Load and run the Python script.
7. Observe how the robot follows the black line.

#### 💡 Reflection and Thresholding

Instead of detecting specific colors using `color()`, we can measure reflected light intensity using `reflection()`.

```python
reflection = color_sensor.reflection()
```

The method returns a value between 0 and 100, where darker surfaces generally produce lower values and lighter surfaces produce higher values.

To distinguish between black and white surfaces, we calculate a **threshold**.

```python
BLACK_REFLECTION = 10
WHITE_REFLECTION = 90

THRESHOLD = (BLACK_REFLECTION + WHITE_REFLECTION) / 2
```

In this example, the threshold is 50.

| Sensor reading | Interpretation |
|---|---|
| Below the threshold | Dark surface |
| At or above the threshold | Light surface |

The black and white reflection values are initial estimates. For better accuracy, measure the actual reflection values of both surfaces and use them to calculate the threshold. This process is called **sensor calibration**.

#### 🧠 Line-Following Algorithm

With a single Color Sensor, the robot follows one edge of the black line rather than its center.

In this activity, the robot follows the right edge of the line using two simple rules:

- If the sensor detects a dark surface, steer right.
- Otherwise, steer left.

```python
while True:
    reflection = color_sensor.reflection()

    if reflection < THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)
    else:
        robot.drive(DRIVE_SPEED, -TURN_RATE)

    wait(20)
```

The robot continuously repeats these instructions to stay near the edge of the line.

This technique is known as **bang-bang control**, a simple form of feedback control in which the robot switches between two fixed steering commands.

Unlike `robot.turn()`, the `robot.drive()` method allows the robot to steer while continuously moving forward.

#### ⚙️ Adjustable Parameters

The performance of the line follower depends on three important parameters.

| Parameter | Initial value | Description |
|---|---:|---|
| `DRIVE_SPEED` | 100 mm/s | Controls how fast the robot moves forward. |
| `TURN_RATE` | 60°/s | Controls how sharply the robot steers. |
| `THRESHOLD` | 50 | Distinguishes dark and light surfaces. |

Changing these parameters can affect the robot's speed, accuracy, and ability to follow sharp curves.

#### 🧪 Experiment: Optimize the Line Follower

The initial program may struggle with sharp curves, causing the robot to temporarily lose the line or move in circles.

Experiment with different parameter values to improve its performance.

Change only one parameter at a time to understand its individual effect on the robot's behavior. Reset the robot to its starting position before each trial.

| Trial | Drive speed (mm/s) | Turn rate (°/s) | Threshold | Times line lost | Completion time (s) |
|---|---:|---:|---:|---:|---:|
| 1 — Baseline | 100 | 60 | 50 | | |
| 2 | 50 | 60 | 50 | | |
| 3 | 150 | 60 | 50 | | |
| 4 | 100 | 30 | 50 | | |
| 5 | 100 | 90 | 50 | | |
| 6 | 100 | 120 | 50 | | |
| 7 | 100 | 60 | 40 | | |
| 8 | 100 | 60 | 60 | | |
| 9 — Optimized | | | | | |

For the threshold experiments, temporarily assign the desired value directly to `THRESHOLD`.

Stop the simulation manually when the robot reaches the end of the track. If the robot fails to complete the track, record the trial as incomplete.

After conducting the experiments, combine the most promising parameter values and test your optimized line follower. Repeat the best-performing trial to check its reliability.

#### 📊 Evaluating Performance

Consider the following metrics when evaluating your line follower:

| Metric | Guide question |
|---|---|
| Correctness | Can the robot complete the entire track? |
| Efficiency | How quickly can the robot complete the track? |
| Reliability | Can the robot consistently complete the track across multiple trials? |
| Robustness | Can the robot handle both gentle and sharp curves? |

#### 💭 Guide Questions

1. Why does the robot move in a zigzag pattern?
2. What happens when the driving speed is too high?
3. What happens when the turning rate is too low or too high?
4. How does changing the threshold affect the robot's behavior?
5. Which combination of parameters produces the best overall performance?
6. Is the fastest line follower necessarily the best line follower?
7. How can we improve the algorithm so that the robot steers more smoothly?

**Key concept:** A robot's performance depends not only on its algorithm but also on how well its parameters are tuned. Experimentation, calibration, and feedback are important aspects of robotics.

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