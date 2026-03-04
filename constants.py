#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

#
# The constants module is a convenience place for teams to hold robot-wide
# numerical or boolean constants. Don't use this for any other purpose!
#

import math

# Motors
kLeftMotor1Port = 2
kLeftMotor2Port = 3
kRightMotor1Port = 6
kRightMotor2Port = 7

# shooting motor ids
# each sparkmax id will be automatically registered in the code
# without any additional configuration
kShootMotorPorts = (19, 16, 5)

kClimbingArmMotorPort = 4

# Encoders
kLeftEncoderPorts = (2, 3)
kRightEncoderPorts = (6, 7)
kLeftEncoderReversed = True
kRightEncoderReversed = False

kEncoderCPR = 1024
kWheelDiameterInches = 6
# Assumes the encoders are directly mounted on the wheel shafts
kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR

# Operator Interface
kDriverControllerPort = 0

# Webcam
kWebcamID = 0