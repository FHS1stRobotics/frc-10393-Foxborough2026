#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib

import commands2
import commands2.button

import constants

from subsystems.drivesubsys import DriveSubsystem
from subsystems.shootsubsys import ShootSubsystem
from subsystems.armsubsys import ArmSubsystem

from commands.drivecmds import TeleOpDrive, RateLimitDrive
from commands.autocmds import AutoDrive
from commands.shootcmds import Start
from commands.armcmds import GoArm

from commands2 import CommandScheduler

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
        self.shootSubsystem = ShootSubsystem()
        self.armSubsystem = ArmSubsystem()

        # The controller
        self.controller = commands2.button.CommandXboxController(
            constants.kDriverControllerPort
        )        
        self.shooterOn = False

        # Configure the button bindings
        self.configureButtonBindings()
    
        # Configure default commands
        # Set the default drive command to tank drive
        self.driveSubsystem.setDefaultCommand(TeleOpDrive(self.driveSubsystem, self.controller))
        
        # Smart Dashboard Chooser
        self.chooser = wpilib.SendableChooser()
        self.chooser.setDefaultOption("Default Auto", constants.fDefaultAutoSpeed)
        self.chooser.addOption("Another auto",constants.fOtherAutoSpeed)
        
        # Dashboard stuff
        wpilib.SmartDashboard.putData(CommandScheduler.getInstance())

        # Put the chooser on the dashboard
        wpilib.SmartDashboard.putData("Autonomous Commands", self.chooser)
        
    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        # limits max output to half when pressing leftbumper
        # are backslashes more readable?
        self.controller.leftBumper() \
            .whileTrue(RateLimitDrive(self.driveSubsystem, 0.5)) \
            .whileFalse(RateLimitDrive(self.driveSubsystem, 1.0))

        # Climing Arm Control
        self.controller.a().whileTrue(GoArm(self.armSubsystem, constants.fClimbSpeedUp))        
        self.controller.b().whileTrue(GoArm(self.armSubsystem, constants.fClimbSpeedDn))
            
        self.controller.rightTrigger(0.3).whileTrue(Start(self.shootSubsystem, self.controller))
            
        self.controller.rightBumper() \
            .onTrue(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.tweakFalcon(-0.15))
            ) \
            .onFalse(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.tweakFalcon(0.0))
            )
            
    def toggleShooter(self) -> bool:
        self.shooterOn = not self.shooterOn
        return self.shooterOn

    def getAutonomousCommand(self) -> commands2.Command:
        return AutoDrive(self.driveSubsystem, self.chooser.getSelected())