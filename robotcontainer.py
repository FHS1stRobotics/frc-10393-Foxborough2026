#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib

import commands2
import commands2.button
import commands2.cmd

import constants

from subsystems.drivesubsys import DriveSubsystem
from subsystems.shootsubsys import ShootSubsystem
from subsystems.armsubsys import ArmSubsystem
from commands2 import SequentialCommandGroup

import commands.shootcmds
import commands.armcmds

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
        
        self.shootSetAllMotorSpeed = commands.shootcmds.ShootCommands.setAllMotorSpeed
        self.shootStopAllMotorSpeed = commands.shootcmds.ShootCommands.stopAllMotorSpeed
        self.setArmMotorSpeedForTime = commands.armcmds.ArmCommands.setMotorSpeedForTime

        # The driver's controller
        self.driverController = commands2.button.CommandXboxController(
            constants.kDriverControllerPort
        )
        
        self.shooterOn = False
        
        self.feedCommand = SequentialCommandGroup(
            self.shootSetAllMotorSpeed(self.shootSubsystem, self.driverController)
        )

        # Configure the button bindings
        self.configureButtonBindings()
    
        # Configure default commands
        # Set the default drive command to tank drive
        self.driveSubsystem.setDefaultCommand(
            commands2.cmd.run(
                lambda: self.driveSubsystem.tankDrive(
                    self.driverController.getLeftY(),
                    self.driverController.getRightY(),
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
        # limits max output to half when pressing leftbumper
        # are backslashes more readable?
        self.driverController.leftBumper() \
            .onTrue(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.setMaxOutput(0.5))
            ) \
            .onFalse(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.setMaxOutput(1))
            )
            
        self.driverController.a() \
            .onTrue(
                self.armSubsystem.setMotorSpeed(
                    speed=-1.0
                )
            ) \
            .onFalse(
                self.armSubsystem.setMotorSpeed(
                    speed=0.0
                )
            )
            
        self.driverController.x() \
            .onTrue(
                 commands2.cmd.runOnce(
                    lambda: self.shootSubsystem.setAllMotorSpeed(1.0 if self.toggleShooter() else 0.0)
                )
            )
            
        self.driverController.b() \
            .onTrue(
                self.armSubsystem.setMotorSpeed(
                    speed=1.0
                )
            ) \
            .onFalse(
                self.armSubsystem.setMotorSpeed(
                    speed=0.0
                )
            )
            
        self.driverController.rightTrigger(0.3) \
            .toggleOnTrue(           
                commands2.cmd.repeatingSequence(self.feedCommand)
            ) \
            .toggleOnFalse(         
                commands2.cmd.runOnce(lambda : self.feedCommand.end(False))
            )
            
        self.driverController.rightBumper() \
            .onTrue(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.tweakFalcon(0.5))
            ) \
            .onFalse(
                commands2.cmd.runOnce(lambda: self.driveSubsystem.tweakFalcon(0.0))
            )
            
    def toggleShooter(self) -> bool:
        self.shooterOn = not self.shooterOn
        return self.shooterOn

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()