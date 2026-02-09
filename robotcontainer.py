#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
from wpilib.interfaces import GenericHID

import commands2
import commands2.button
import commands2.cmd

import constants

from subsystems.drivesubsys import DriveSubsystem


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The robot's subsystems
        self.driveSubsystem = DriveSubsystem()

        # The driver's controller
        self.driverController = commands2.button.CommandXboxController(
            constants.kDriverControllerPort
        )

        # Configure the button bindings
        self.configureButtonBindings()

        # Configure default commands
        # Set the default drive command to split-stick arcade drive
        self.driveSubsystem.setDefaultCommand(
            # A split-stick arcade command, with forward/backward controlled by the left
            # hand, and turning controlled by the right.
            commands2.cmd.run(
                lambda: self.driveSubsystem.arcadeDrive(
                    -self.driverController.getLeftY(),
                    -self.driverController.getRightX(),
                ),
                self.driveSubsystem,
            )
        )

        # Chooser
        self.chooser = wpilib.SendableChooser()

        # Put the chooser on the dashboard
        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """

        # While holding R1, drive at half speed
        # are backslashes more readable?
        self.driverController.x() \
            .onTrue(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.setMaxOutput(0.5))
            ) \
            .onFalse(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.setMaxOutput(1))
            )
        
        # self.driverController.rightTrigger() \
        #     .onTrue(
                
        #     ).onFalse(

        #     )

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()