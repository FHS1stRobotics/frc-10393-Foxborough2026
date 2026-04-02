#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
from rev import (
    SparkMax, 
    SparkMaxConfig,
    ResetMode, 
    PersistMode
)

import constants

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.motor = SparkMax(constants.kClimbingArmMotorPort, SparkMax.MotorType.kBrushless)    
        self.encoder = SparkMaxConfig().inverted(constants.kClimbingArmMotorInvert)
        self.motor.configure(self.encoder,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        
    def setMotorSpeed(self, speed: float) -> None:
        self.motor.set(speed)