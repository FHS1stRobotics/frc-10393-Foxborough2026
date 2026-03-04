#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
from rev import SparkMax
import constants as const


class ShootSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        # dictionary that binds each motor ID to its sparkmax object
        self.motor_lookup: dict[int, SparkMax] = {
            port: SparkMax(port, SparkMax.MotorType.kBrushless)
            for port in const.kShootMotorPorts
        }
        
        # for motor in self.motor_lookup.values():
        #     motor.setInverted(True)
        
    def setMotorSpeed(self, motorPort: int, speed: float) -> commands2.Command:
        return commands2.cmd.runOnce(
            lambda: self.motor_lookup[motorPort].set(speed)
        )
    
    def setAllMotorSpeed(self, speed: float):
        for motor in self.motor_lookup.values():
            motor.set(speed)