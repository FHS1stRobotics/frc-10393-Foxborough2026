# steps
- actually use the venv :DDDDDDD
- Pushups

# env stuff did
- py -3 -m venv .venv
- py -3 -m
- py -3 -m pop install robotpy
- py -3 -m pop install robotpy-rev
- py -3 -m pip install robotpy-navx
- py -3 -m pip install phoenix6
-- phoenix6 requires 2026.2.1.1 (NOT 2026.2.2) - DO NOT UPGARDE IT

# env stuff NOT DID
- py -3 -m pip install opencv-python  
-- opencv-python hates py 3.14 and RoboRIO 2026 requries 3.14 so ...

# build stuff did
- be sure to updated requires in pyproject.toml- requires = ["robotpy-rev","phoenix6","robotpy-navx"] 
- py -3 -m robotpy sync
- py -3 -m robotpy deploy --skip-tests


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