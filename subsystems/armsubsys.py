#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
from rev import SparkMax
import constants as const
from time import sleep


class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.motor = SparkMax(const.kClimbingArmMotorPort, SparkMax.MotorType.kBrushless)
        
        self.motor.setInverted(False)
        
    def setMotorSpeed(self, speed: float) -> commands2.Command:
        return commands2.cmd.runOnce(
            lambda: self.motor.set(speed)
        )
    
    def setMotorSpeedForTime(self, timeSeconds: float, speed: float):
        self.motor.set(speed)
        sleep(timeSeconds)
        self.motor.set(0)