#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2

from subsystems.drivesubsys import DriveSubsystem

class TeleOpDrive(commands2.Command):
    def __init__(self, driveSystem : DriveSubsystem, driverController) -> None:
        super().__init__()
        self.driveSystem = driveSystem
        self.addRequirements(self.driveSystem)
        self.controller = driverController
        
    @staticmethod
    def adjSpeed(f : float) -> float:
        v = min(f * f, 1.0)
        return v if f > 0 else -v
        
    def execute(self) -> None:
        self.driveSystem.tankDrive( \
            self.adjSpeed(self.controller.getLeftY()), \
            self.adjSpeed(self.controller.getRightY()))
        
    def end(self, interrupted:bool) -> None:
        self.driveSystem.tankDrive(0,0)
        
    def isFinished(self) -> bool:
        return False    

class RateLimitDrive(commands2.Command):
    def __init__(self, driveSystem : DriveSubsystem, rate : float) -> None:
        super().__init__()
        self.driveSystem = driveSystem
        self.rate = rate
        
    def execute(self) -> None:
        self.driveSystem.setMaxOutput(self.rate)
        
    def isFinished(self) -> bool:
        return False