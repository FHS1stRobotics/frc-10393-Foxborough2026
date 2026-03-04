#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import commands2.cmd

from subsystems.armsubsys import ArmSubsystem


class ArmCommands:
    def __init__(self) -> None:
        raise Exception("This is a utility class!")

    @staticmethod
    def setMotorSpeedForTime(armSubsystem: ArmSubsystem, timeSeconds: float, speed: float) -> commands2.Command:
        return commands2.cmd.runOnce(
            lambda: armSubsystem.setMotorSpeedForTime(timeSeconds, speed)
        )