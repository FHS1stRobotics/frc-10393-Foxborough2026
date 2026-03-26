# steps
- actually use the venv :DDDDDDD
- Pushups

# stuff did
- py -3 -m pip install phoenix6
- py -3 -m pip install robotpy-navx
- be sure to updated requires in pyproject.toml- requires = ["robotpy-rev","opencv-python","phoenix6","robotpy-navx"]
- phoenix6 requires 2026.2.1.1 - DO NOT UPGARDE IT

# Functions
Features
- short burst spin to shoot from close (single shot)
- another burst spin to shoot from far away (single shot)
- hold right trigger for continuous shooting
- at the beginning of auto, shoot all fuel into the hub and then go climb the tower

# Subsystems/Commands Needed
- __Shooting__
  - shootsubsys.py
  - shootcommand.py
- __Auto__
    - auto.py