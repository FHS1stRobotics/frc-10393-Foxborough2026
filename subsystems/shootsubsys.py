#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
from rev import SparkMax

import constants as const


class ShootSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.motor = SparkMax(const.kShootMotorPort, SparkMax.MotorType.kBrushless)
        
        self.motor.setInverted(False) # set to True if necessary
        
    def setMotorSpeed(self, speed: float):
        self.motor.set(speed)