#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import commands2.cmd

from subsystems.shootsubsys import ShootSubsystem


class ShootCommands:
    def __init__(self) -> None:
        raise Exception("This is a utility class!")

    @staticmethod
    def setAllMotorSpeed(shootSubsystem: ShootSubsystem, speed: float) -> commands2.Command:
        return commands2.cmd.runOnce(
            lambda: shootSubsystem.setAllMotorSpeed(speed)
        )