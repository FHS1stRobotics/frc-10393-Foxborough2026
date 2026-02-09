#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
import wpilib.drive
from rev import (
    SparkMax, 
    SparkBaseConfig, 
    ResetMode, 
    PersistMode
)
import constants as const


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.left1 = SparkMax(const.kLeftMotor1Port, type=SparkMax.MotorType.kBrushed)
        self.left2 = SparkMax(const.kLeftMotor2Port, type=SparkMax.MotorType.kBrushed)
        self.right1 = SparkMax(const.kRightMotor1Port, type=SparkMax.MotorType.kBrushed)
        self.right2 = SparkMax(const.kRightMotor2Port, type=SparkMax.MotorType.kBrushed)
        
        # Configure left2 to follow left1
        cfg = SparkBaseConfig()
        cfg.follow(const.kLeftMotor1Port)  # Tell this controller to follow left1’s CAN ID
        self.left2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # Configure right2 to follow right1
        cfg = SparkBaseConfig()
        cfg.follow(const.kRightMotor1Port)
        self.right2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # We need to invert one side of the drivetrain so that positive speeds
        # result in both sides moving forward. Depending on how your robot's
        # drivetrain is constructed, you might have to invert the left side instead.
        self.right1.setInverted(True)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(self.left1, self.right1)
        
        # The left-side drive encoder
        self.leftEncoder = wpilib.Encoder(
            *const.kLeftEncoderPorts,
            reverseDirection=const.kLeftEncoderReversed
        )

        # The right-side drive encoder
        self.rightEncoder = wpilib.Encoder(
            *const.kRightEncoderPorts,
            reverseDirection=const.kRightEncoderReversed
        )

        # Sets the distance per pulse for the encoders
        self.leftEncoder.setDistancePerPulse(const.kEncoderDistancePerPulse)
        self.rightEncoder.setDistancePerPulse(const.kEncoderDistancePerPulse)

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(fwd, rot)

    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
        self.rightEncoder.reset()

    def getAverageEncoderDistance(self) -> float:
        """Gets the average distance of the TWO encoders."""
        return (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.drive.setMaxOutput(maxOutput)