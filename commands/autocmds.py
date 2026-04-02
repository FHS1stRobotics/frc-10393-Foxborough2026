#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2

from subsystems.drivesubsys import DriveSubsystem

class AutoDrive(commands2.Command):
    def __init__(self, driveSystem : DriveSubsystem, speed : float) -> None:
        super().__init__()
        self.driveSystem = driveSystem
        self.addRequirements(self.driveSystem)
        self.speed = speed
        
    def execute(self) -> None:
        self.driveSystem.tankDrive(self.speed, self.speed)
        
    def end(self, interrupted:bool) -> None:
        self.driveSystem.stopTankDrive()
        
    def isFinished(self) -> bool:
        return False
    