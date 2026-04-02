#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import constants
import wpilib
import wpilib.drive

from wpimath.filter import SlewRateLimiter
from rev import (
    SparkMax, 
    SparkBaseConfig, 
    SparkMaxConfig,
    ResetMode, 
    PersistMode
)
from phoenix6 import (
    hardware,
    controls,
    configs
)

class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.left1 = SparkMax(constants.kLeftMotor1Port, type=SparkMax.MotorType.kBrushless)
        self.left2 = SparkMax(constants.kLeftMotor2Port, type=SparkMax.MotorType.kBrushless)
        self.right1 = SparkMax(constants.kRightMotor1Port, type=SparkMax.MotorType.kBrushless)
        self.right2 = SparkMax(constants.kRightMotor2Port, type=SparkMax.MotorType.kBrushless)
        
        # Configure left2 to follow left1        
        cfg = SparkMaxConfig().inverted(constants.kLeftEncoderReversed)
        self.left1.configure(cfg,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        
        cfg = SparkBaseConfig().follow(constants.kLeftMotor1Port)  # Tell this controller to follow left1’s CAN ID
        self.left2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # Configure right2 to follow right1        
        cfg = SparkMaxConfig().inverted(constants.kRightEncoderReversed)
        self.right1.configure(cfg,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        
        cfg = SparkBaseConfig().follow(constants.kRightMotor1Port)  
        self.right2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(self.left1, self.right1)
        
        # The left-side drive encoder
        self.leftEncoder = wpilib.Encoder(
            *constants.kLeftEncoderPorts,
            reverseDirection=constants.kLeftEncoderReversed
        )
        self.leftLimit = SlewRateLimiter(constants.kDriveMotorSlewRate)
        self.leftEncoder.setDistancePerPulse(constants.kEncoderDistancePerPulse)

        # The right-side drive encoder
        self.rightEncoder = wpilib.Encoder(
            *constants.kRightEncoderPorts,
            reverseDirection=constants.kRightEncoderReversed
        )
        self.rightLimit = SlewRateLimiter(constants.kDriveMotorSlewRate)
        self.rightEncoder.setDistancePerPulse(constants.kEncoderDistancePerPulse)

        # Sets the distance per pulse for the encoders
        
        # # Vex falcon TEST for now
        self.falconMotor = hardware.TalonFX(constants.kFalconMotorIdx)
        falcon_configs = configs.MotorOutputConfigs()
        self.falconMotor.configurator.apply(falcon_configs)
        self.falconRequest = controls.DutyCycleOut(0)
        
    def slewSpeed(self, speed: float, limiter: SlewRateLimiter) -> float:
        last = limiter.lastValue()
        if abs(speed) < abs(last) and speed * last > 0 :
            speed = -speed
            limiter.reset(speed)
        else :
            speed = limiter.calculate(-speed)
        return speed
        
    def tankDrive(self, leftSpeed: float, rightSpeed: float) -> None:
        """
        Drives the robot using tank controls.

        :param leftSpeed: the commanded movement of the left side
        :param rightSpeed: the commanded movement of the right side
        """              
        leftSpeed = self.slewSpeed(leftSpeed, self.leftLimit)
        rightSpeed = self.slewSpeed(rightSpeed, self.rightLimit)
        self.drive.tankDrive(leftSpeed, rightSpeed)
        
    def resetMyLimiters(self) -> None:
        self.leftLimit.reset(0)
        self.rightLimit.reset(0)
        
    def stopTankDrive(self) -> None:
        self.tankDrive(0,0)
        self.resetMyLimiters()

    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
        self.resetMyLimiters()

    def getAverageEncoderDistance(self) -> float:
        """Gets the average distance of the TWO encoders."""
        return (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.drive.setMaxOutput(maxOutput)
        
    def tweakFalcon(self, value: float):
        self.falconRequest.output = value
        self.falconMotor.set_control(self.falconRequest)