#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import commands2.cmd

from subsystems.shootsubsys import ShootSubsystem

class Start(commands2.Command):
    def __init__(self, system: ShootSubsystem, control : commands2.button.CommandXboxController) -> None:
        super().__init__()
        self.shootSubsystem = system
        self.controller = control

    def execute(self) -> None:
        self.shootSubsystem.setAllMotorSpeed(self.controller.getRightTriggerAxis())
        
    def end(self, interrupted:bool) -> None:
        self.shootSubsystem.setAllMotorSpeed(0)
        
    def isFinished(self) -> bool:
        return False
