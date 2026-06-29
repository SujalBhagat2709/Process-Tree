# Process Tree

## Overview

Process Tree is a terminal-based Python application that simulates how operating systems manage parent and child processes.

Users can create root processes, add child processes, display the process hierarchy, and terminate any process along with all of its child processes.

---

## Features

- Create Root Process
- Add Child Processes
- Recursive Process Tree
- Kill Parent or Child Process
- Automatic Recursive Deletion
- JSON Storage
- Interactive Terminal Menu

---

## Project Structure

process-tree/

├── process_engine.py

├── app.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

python app.py

---

## Example

Create Root Process

Chrome

↓

Add Child

Renderer-1

↓

Add Child

Renderer-2

↓

Add Child

GPU

---

Display

|-- Chrome

    |-- Renderer-1

        |-- GPU

    |-- Renderer-2

---

Kill Renderer-1

↓

Tree becomes

|-- Chrome

    |-- Renderer-2

---

Kill Chrome

↓

All child processes are automatically removed.

---

## Generated File

process_tree.json

Example

{
    "Chrome": {
        "parent": null,
        "children": [
            "Renderer-1",
            "Renderer-2"
        ]
    },
    "Renderer-1": {
        "parent": "Chrome",
        "children": [
            "GPU"
        ]
    },
    "Renderer-2": {
        "parent": "Chrome",
        "children": []
    },
    "GPU": {
        "parent": "Renderer-1",
        "children": []
    }
}

---

## Future Improvements

- Process IDs (PID)
- CPU Usage Simulation
- Memory Usage Simulation
- Running / Sleeping / Zombie States
- Search Process
- Rename Process
- Process Statistics
- Export Tree
- Import Tree
- Colored Terminal Output
- Tree Depth Analysis
- Process Priority

---

## License

MIT License