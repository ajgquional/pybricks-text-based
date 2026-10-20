# 🤖 Pybricks Text-Based Programming

Custom beginner-friendly Python scripts for learning **text-based Pybricks programming** using LEGO® Education SPIKE™ Prime.

Each lesson folder contains two script versions:

* `simulator.py` — for the online simulator
* `actual.py` — for an actual SPIKE Prime robot running Pybricks

The tutorial begins with basic motor control and gradually progresses toward sensors, autonomous robot behavior, RoboSports Double Tennis, and advanced device integration such as HuskyLens.

## 📁 Proposed Outline

* 01: First Program
* 02: Motor Control
* 03: Drivebase Movement
* 04: Loops
* 05: Conditions and Decisions (actual TBA)
* 06: Functions (actual TBA)
* 07: Color Sensor (coming soon)
* 08: Distance Sensor (coming soon)
* 09: Gyro and Orientation (coming soon)
* 10: Search and React (coming soon)
* 11: Timers and Match Logic (coming soon)
* 12: Double Tennis (coming soon)
* 13: HuskyLens Integration (coming soon)

> The structure may be adjusted as the tutorial progresses.

## 🌐 Simulator

The simulator activities use **GearsBot**, a free browser-based robotics simulator.

* [GearsBot Simulator](https://gears.aposteriori.com.sg/)
* [GearsBot Pybricks Tutorials](https://tutorials.aposteriori.com.sg/110-Pybricks-Basics/10-Introduction/10-Intro.html)

GearsBot commonly uses the older EV3-style Pybricks API, while an actual SPIKE Prime uses the current Powered Up API. Separate scripts are therefore provided for each platform.

## 🔗 References

### Pybricks

* [Pybricks Website](https://pybricks.com/)
* [Pybricks Code](https://code.pybricks.com/)
* [Pybricks Learning Resources](https://pybricks.com/learn/)
* [Pybricks Documentation](https://docs.pybricks.com/en/latest/)
* [SPIKE Prime Hub Documentation](https://docs.pybricks.com/en/latest/hubs/primehub.html)
* [Motor Documentation](https://docs.pybricks.com/en/latest/pupdevices/motor.html)
* [DriveBase Documentation](https://docs.pybricks.com/en/latest/robotics.html)
* [Pybricks Runner for VS Code](https://open-vsx.org/extension/AnandSingh/pybricks-runner)

### Relevant Competitions

* [Philippine Robot Olympiad](https://felta.ph/pro/download.html)
* [PRO 2025 RoboSports Double Tennis General Rules](https://felta.ph/pro/files/2025/PRO-2025-RoboSports-Double-Tennis-General-Rules.pdf)
* [IDE Series 2026 Singapore](https://ideseries.org/ide2026/)
* [First Lego League 2026-2027 (Bioglow) Philippines](https://felta.ph/pdf/fll/16th_FLL_Philippines_2026-2027_BIOGLOW_Season_Calendar.pdf)

### HuskyLens

* [HuskyLens Wiki](https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336)
* [PyHuskyLens Documentation](https://docs.antonsmindstorms.com/en/latest/Software/PyHuskyLens/docs/index.html)

## 📝 Notes

* Simulator programs are stored in `simulator.py` or `simulator_*.py`.
* Physical SPIKE Prime programs are stored in `actual.py` or `actual_*.py`.
* Motor and sensor ports may need to be changed based on the selected simulator robot or physical robot configuration.
* Wheel diameter, axle track, speed, and sensor thresholds may require calibration on the actual robot.
* The simulator is primarily used to test program logic, while the physical robot is used to test hardware behavior and calibration.

## 🌍 Custom World Generator

This repository includes `generate_world.py`, a command-line tool for generating custom ground images for the [GearsBot Simulator](https://gears.aposteriori.com.sg/).

The tool uses **Pillow** to create reusable training arenas for different robotics lessons.

### 🛠️ Setup

Unlike the Pybricks lesson scripts, which run in GearsBot or on the actual SPIKE Prime robot, the world generator runs locally using Python.

**1. Create a virtual environment**

From the repository's root directory:

```bash
python -m venv .venv
```

**2. Activate the virtual environment**

On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

On Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

**3. Install Pillow**

```bash
python -m pip install Pillow
```

No additional packages are required for the world generator.

### ▶️ Generating a Custom World Ground Image

Run the script from the repository's root directory:

```bash
python generate_world.py --preset <preset-name> --width <width> --height <height> --background <color> --output <output-path-with-image-filename>
```

This generates a PNG image in the output path specified.

The output directory is automatically created if it does not exist.

### ⚙️ CLI Arguments

| Argument | Description | Default |
|---|---|---|
| `--preset` | Selects the world layout | `color-test` |
| `--width` | Image width in pixels | `1200` |
| `--height` | Image height in pixels | `800` |
| `--background` | Background color | `white` |
| `--output` | Output PNG file path | `world.png` |
| `--list-presets` | Displays available world presets | — |

To display all available commands and to view the command-line help:

```bash
python generate_world.py --help
```

To list available presets:

```bash
python generate_world.py --list-presets
```

**Note:** Replace the placeholders with your preferred values. The selected preset must be supported by `generate_world.py`.

## 🚀 Importing the World Image in GearsBot World Builder and Extracting it as JSON

1. Generate the PNG image using the script.
2. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Open **Worlds → World Builder**.
3. Select the ground and locate its image URL setting (`imageURL`).
4. Enter the raw GitHub URL of the generated PNG:

   ```text
   https://raw.githubusercontent.com/ajgquional/pybricks-text-based/main/<image-path>
   ```

5. Adjust the ground dimensions and robot's starting position as needed.
6. After configuration adjustment, save the world to file by clicking **File → Save world to file**. A JSON file will then be downloaded entitled `custom_world.json` (modify the name after download, according to preference). This world configuration extraction as a JSON file is important for future world reuse.
7. In the Simulator tab, load the JSON world file by clicking **Worlds → Load from file**. A window will appear where you can navigate to the saved world. Select it and automatically, the world will be loaded on the simulator.

> The PNG image defines the visual ground layout, while the JSON file stores the world configuration.

### 📌 Notes

- The script generates PNG images, not complete GearsBot world JSON files.
- Image dimensions are specified in pixels.
- Available presets are defined in the PRESETS dictionary inside generate_world.py.
- Generated images can be hosted on GitHub and loaded into GearsBot using their raw image URLs. Should pre-made images are to be used, the use of `generate_world.py` can be bypassed. Instead, you can proceed to the creation of the JSON file for the world to be used in the Simulator.
- The tool is designed to support additional world presets in future lessons. As such, generated images and exported JSON files can be stored together in the appropriate lesson's worlds/ directory.
