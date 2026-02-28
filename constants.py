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
kLeftMotor1Port = 7
kLeftMotor2Port = 6
kRightMotor1Port = 2
kRightMotor2Port = 3

# shooting motor ids
# each sparkmax id will be automatically registered in the code
# without any additional configuration
kShootMotorPorts = (0, 1, 100)

kClimbingArmMotorPort = 4

# Encoders
kLeftEncoderPorts = (0, 1)
kRightEncoderPorts = (2, 3)
kLeftEncoderReversed = False
kRightEncoderReversed = True

kEncoderCPR = 1024
kWheelDiameterInches = 6
# Assumes the encoders are directly mounted on the wheel shafts
kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR

# Operator Interface
kDriverControllerPort = 0

# Webcam
kWebcamID = 0