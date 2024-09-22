# MoMaLeNe

Real-Time Fluid Simulation.

## Installation

### Create a virtual environment
Using venv:
```bash
python3.10 -m venv venv
source venv/bin/activate
```
In VSCode, select this new environment as the interpreter. 
Run `deactivate` to close the virtual environment.

Using conda:
```bash
conda create -n momalene python=3.10 -y
```

### Install dependencies
```
pip install -e .
```

### Run
```
python3 main.py
```

```bash
sudo apt update
sudo apt install libxcb-cursor0 libx11-xcb1
sudo apt install xvfb
```