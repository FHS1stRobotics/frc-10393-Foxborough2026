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
kLeftMotor1Port = 6
kLeftMotor2Port = 7
kRightMotor1Port = 2
kRightMotor2Port = 3

# shooting motor ids
# each SparkMax id will be automatically registered in the code
# without any additional configuration
kShootMotorPorts = (19, 16, 1)
kShootMotorInvert = (False, True, True)
kShootMotorScale = (1.0, 1.0, 1.0)

# Climbing arm stuff
kClimbingArmMotorPort = 4
kClimbingArmMotorInvert = False
fClimbSpeedUp = 1.0
fClimbSpeedDn = 1.0

# Encoders - SparkMax
kLeftEncoderPorts = (2, 3)
kLeftEncoderReversed = False
kRightEncoderPorts = (6, 7)
kRightEncoderReversed = True
kDriveMotorSlewRate = 2

kEncoderCPR = 1024
kWheelDiameterInches = 6

# Falcon motors
kFalconMotorIdx = 10

# Assumes the encoders are directly mounted on the wheel shafts
kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR

# Operator Interface
kDriverControllerPort = 0

# Webcam
kWebcamID = 0

# AutoCommand speeds
fDefaultAutoSpeed = 0.5
fOtherAutoSpeed = -0.5