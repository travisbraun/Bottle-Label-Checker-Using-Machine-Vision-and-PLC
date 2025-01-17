
## Overview

This program is designed for monitoring and inspecting bottles on a production line using TwinCAT3, Python, and OPC UA for communication. The application integrates machine vision image processing to ensure each bottle has a label.

---

## Features

- **OPC UA Integration**: Reads and writes variables to/from a TwinCAT server.
- **Sensor Monitoring**: Tracks proximity sensors to detect bottles.
- **Machine Vision**: Processes images to identify bottles with and without labels.
- **Control Logic**: Activates ejectors for defective bottles.
---

## Requirements

### Software

- Python 3.10+
- TwinCAT (for OPC UA server)
- Git (for version control)
- UA Expert

### Python Dependencies

Install the following packages using pip:

```bash
pip install opcua opencv-python numpy
```

---

## File Structure

```
BottleChecker
├── BottleMachineVision/       # TwinCAT project file
├── main.py                    # Main Python script for OPC UA interactions
├── Resources                  # Sample images to test with
└── README.md                  # Documentation
```

---

## Usage

### 1. Setup TwinCAT Server

1. Ensure the TwinCAT server is running on your machine.
2. Configure the OPC UA settings to enable read/write permissions and anonymous clients.
3. Verify variable accessibility using the TwinCAT XAE environment.

### 2. Run the Program

1. Open the terminal and navigate to the program directory.
2. Run the main Python script:
    
    ```bash
    python main.py
    ```


### 3. Interact With TwinCAT Interface
1. Activate the proximity button to check the current bottle.
2. Click "Exit Script" to exit the program.

---

### Demo Video
https://drive.google.com/file/d/1aiXGq15d1_LjcWTllOecRmeOPVQKK_r0/view?usp=drive_link