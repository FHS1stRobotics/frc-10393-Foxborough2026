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
    SparkMaxConfig,
    ResetMode, 
    PersistMode
)
from phoenix6 import (
    hardware,
    controls,
    configs
)

import constants as const

class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.left1 = SparkMax(const.kLeftMotor1Port, type=SparkMax.MotorType.kBrushless)
        self.left2 = SparkMax(const.kLeftMotor2Port, type=SparkMax.MotorType.kBrushless)
        self.right1 = SparkMax(const.kRightMotor1Port, type=SparkMax.MotorType.kBrushless)
        self.right2 = SparkMax(const.kRightMotor2Port, type=SparkMax.MotorType.kBrushless)
        
        # Configure left2 to follow left1        
        cfg = SparkMaxConfig().inverted(const.kLeftEncoderReversed)
        self.left1.configure(cfg,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        
        cfg = SparkBaseConfig().follow(const.kLeftMotor1Port)  # Tell this controller to follow left1’s CAN ID
        self.left2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # Configure right2 to follow right1        
        cfg = SparkMaxConfig().inverted(const.kRightEncoderReversed)
        self.right1.configure(cfg,  ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        
        cfg = SparkBaseConfig().follow(const.kRightMotor1Port)  
        self.right2.configure(cfg, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

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
        
        # # Vex falcon TEST for now
        # self.falconMotor = hardware.TalonFX(const.kFalconMotorIdx)
        # falcon_configs = configs.MotorOutputConfigs()
        # self.falconMotor.configurator.apply(falcon_configs)
        # self.falconRequest = controls.DutyCycleOut(0)

    def tankDrive(self, leftSpeed: float, rightSpeed: float) -> None:
        print (f"hi {leftSpeed} {rightSpeed}")
        """
        Drives the robot using tank controls.

        :param leftSpeed: the commanded movement of the left side
        :param rightSpeed: the commanded movement of the right side
        """
        left = max(min(leftSpeed * leftSpeed, 1.0), -1.0)
        left = -left if leftSpeed < 0 else left
        right = max(min(rightSpeed * rightSpeed, 1.0), -1.0)
        right = -right if rightSpeed < 0 else right
                
        self.drive.tankDrive(-left, -right)

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
        
    # def tweakFalcon(self, value: float):
    #     self.falconRequest.output = value
    #     self.falconMotor.set_control(self.falconRequest)