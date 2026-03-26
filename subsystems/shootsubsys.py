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

import constants as const

class ShootSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        # dictionary that binds each motor ID to its sparkmax object
        self.motor_lookup = {}
        
        for idx in range(len(const.kShootMotorPorts)):
            port = const.kShootMotorPorts[idx]
            motor = SparkMax(port, SparkMax.MotorType.kBrushless)   
            
            cfg = SparkMaxConfig().inverted(const.kShootMotorInvert[idx])
            motor.configure(cfg,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
            
            self.motor_lookup[port] = motor    
            print(f"MOTOR: {motor.getDeviceId()}")
            
    def setMotorSpeed(self, motorPort: int, speed: float) -> commands2.Command:
        return commands2.cmd.runOnce(
            lambda: self.motor_lookup[motorPort].set(speed * const.kShootMotorScale[motorPort])
        )
    
    def setAllMotorSpeed(self, speed: float):
        for idx in self.motor_lookup.keys():
            self.motor_lookup[idx].set(speed)
            print(F"idx:{idx} speed:{speed}")
