#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2.cmd

from subsystems.armsubsys import ArmSubsystem

class GoArm(commands2.Command):
    def __init__(self, armSystem : ArmSubsystem, speed : float) -> None:
        super().__init__()
        self.armSystem = armSystem
        self.addRequirements(self.armSystem)
        self.speed = speed
        
    def execute(self) -> None:
        self.armSystem.setMotorSpeed(self.speed)
        
    def end(self, interrupted:bool) -> None:
        self.armSystem.setMotorSpeed(self.speed)
        
    def isFinished(self) -> bool:
        return False
    
    