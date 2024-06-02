from . import REVModule, REVADC, REVMessage as REVMsg

##Motor driver
def setMotorChannelMode(commObj, destination, motorChannel, motorMode, floatAtZero):
    """Set motor mode and breaking mode"""
    setMotorChannelModeMsg = REVMsg.SetMotorChannelMode()
    setMotorChannelModeMsg.payload.motorChannel = motorChannel
    setMotorChannelModeMsg.payload.motorMode = motorMode
    setMotorChannelModeMsg.payload.floatAtZero = floatAtZero
    commObj.sendAndReceive(setMotorChannelModeMsg, destination)

def getMotorChannelMode(commObj, destination, motorChannel):
    """Read motor mode and breaking mode"""
    getMotorChannelModeMsg = REVMsg.GetMotorChannelMode()
    getMotorChannelModeMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorChannelModeMsg, destination)
    return (
     packet.payload.motorChannelMode, packet.payload.floatAtZero)

def setMotorChannelEnable(commObj, destination, motorChannel, enabled):
    """Enable/disable a motor"""
    setMotorChannelEnableMsg = REVMsg.SetMotorChannelEnable()
    setMotorChannelEnableMsg.payload.motorChannel = motorChannel
    setMotorChannelEnableMsg.payload.enabled = enabled
    commObj.sendAndReceive(setMotorChannelEnableMsg, destination)

def getMotorChannelEnable(commObj, destination, motorChannel):
    """Get the enabled/disabled state of a motor"""
    getMotorChannelEnableMsg = REVMsg.GetMotorChannelEnable()
    getMotorChannelEnableMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorChannelEnableMsg, destination)
    return packet.payload.enabled

def setMotorChannelCurrentAlertLevel(commObj, destination, motorChannel, currentLimit):
    """Set the current alert current in amps (?)"""
    setMotorChannelCurrentAlertLevelMsg = REVMsg.SetMotorChannelCurrentAlertLevel()
    setMotorChannelCurrentAlertLevelMsg.payload.motorChannel = motorChannel
    setMotorChannelCurrentAlertLevelMsg.payload.currentLimit = currentLimit
    commObj.sendAndReceive(setMotorChannelCurrentAlertLevelMsg, destination)

def getMotorChannelCurrentAlertLevel(commObj, destination, motorChannel):
    """Get the current alert in amps (?)"""
    getMotorChannelCurrentAlertLevelMsg = REVMsg.GetMotorChannelCurrentAlertLevel()
    getMotorChannelCurrentAlertLevelMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorChannelCurrentAlertLevelMsg, destination)
    return packet.payload.currentLimit

def resetMotorEncoder(commObj, destination, motorChannel):
    """Reset the motor encoder to 0"""
    resetMotorEncoderMsg = REVMsg.ResetMotorEncoder()
    resetMotorEncoderMsg.payload.motorChannel = motorChannel
    commObj.sendAndReceive(resetMotorEncoderMsg, destination)

def setMotorConstantPower(commObj, destination, motorChannel, powerLevel):
    """Set motor power"""
    setMotorConstantPowerMsg = REVMsg.SetMotorConstantPower()
    setMotorConstantPowerMsg.payload.motorChannel = motorChannel
    setMotorConstantPowerMsg.payload.powerLevel = powerLevel
    commObj.sendAndReceive(setMotorConstantPowerMsg, destination)

def getMotorConstantPower(commObj, destination, motorChannel):
    """Get the currently set power of the motor"""
    getMotorConstantPowerMsg = REVMsg.GetMotorConstantPower()
    getMotorConstantPowerMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorConstantPowerMsg, destination)
    return packet.payload.powerLevel

def setMotorTargetVelocity(commObj, destination, motorChannel, velocity):
    """Set target velocity for Run Using Encoder"""
    setMotorTargetVelocityMsg = REVMsg.SetMotorTargetVelocity()
    setMotorTargetVelocityMsg.payload.motorChannel = motorChannel
    setMotorTargetVelocityMsg.payload.velocity = velocity
    commObj.sendAndReceive(setMotorTargetVelocityMsg, destination)

def getMotorTargetVelocity(commObj, destination, motorChannel):
    """Get target velocity for Run Using Encoder"""
    getMotorTargetVelocityMsg = REVMsg.GetMotorTargetVelocity()
    getMotorTargetVelocityMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorTargetVelocityMsg, destination)
    return packet.payload.velocity

def setMotorTargetPosition(commObj, destination, motorChannel, position, atTargetTolerance):
    """Set target position for run to position"""
    setMotorTargetPositionMsg = REVMsg.SetMotorTargetPosition()
    setMotorTargetPositionMsg.payload.motorChannel = motorChannel
    setMotorTargetPositionMsg.payload.position = position
    setMotorTargetPositionMsg.payload.atTargetTolerance = atTargetTolerance
    commObj.sendAndReceive(setMotorTargetPositionMsg, destination)

def getMotorTargetPosition(commObj, destination, motorChannel):
    """Get target position for run to position"""
    getMotorTargetPositionMsg = REVMsg.GetMotorTargetPosition()
    getMotorTargetPositionMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorTargetPositionMsg, destination)
    return (
     packet.payload.targetPosition, packet.payload.atTargetTolerance)

def getMotorAtTarget(commObj, destination, motorChannel):
    """Check is the motor is at the target position"""
    getMotorAtTargetMsg = REVMsg.GetMotorAtTarget()
    getMotorAtTargetMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorAtTargetMsg, destination)
    return packet.payload.atTarget

def getMotorEncoderPosition(commObj, destination, motorChannel):
    """Read the motor encoder value"""
    getMotorEncoderPositionMsg = REVMsg.GetMotorEncoderPosition()
    getMotorEncoderPositionMsg.payload.motorChannel = motorChannel
    packet = commObj.sendAndReceive(getMotorEncoderPositionMsg, destination)
    val = int(packet.payload.currentPosition)
    bits = int(32)
    if val & 1 << bits - 1 != 0:
        val = val - (1 << bits)
    return val

def setMotorPIDCoefficients(commObj, destination, motorChannel, mode, p, i, d):
    """Set motor PID coefficients"""
    setMotorPIDCoefficientsMsg = REVMsg.SetMotorPIDCoefficients()
    setMotorPIDCoefficientsMsg.payload.motorChannel = motorChannel
    setMotorPIDCoefficientsMsg.payload.mode = mode
    setMotorPIDCoefficientsMsg.payload.p = p * Q16
    setMotorPIDCoefficientsMsg.payload.i = i * Q16
    setMotorPIDCoefficientsMsg.payload.d = d * Q16
    commObj.sendAndReceive(setMotorPIDCoefficientsMsg, destination)

def getMotorPIDCoefficients(commObj, destination, motorChannel, mode):
    """Get motor PID coefficents"""
    getMotorPIDCoefficientsMsg = REVMsg.GetMotorPIDCoefficients()
    getMotorPIDCoefficientsMsg.payload.motorChannel = motorChannel
    getMotorPIDCoefficientsMsg.payload.mode = mode
    packet = commObj.sendAndReceive(getMotorPIDCoefficientsMsg, destination)
    p = int(packet.payload.p) / Q16
    i = int(packet.payload.i) / Q16
    d = int(packet.payload.d) / Q16
    return (
     p, i, d)

def setVelocityPIDCoefficients(commObj, destination, motorChannel, p, i, d):
    """Set motor PID coefficients for run using encoder"""
    setMotorPIDCoefficients(commObj, destination, motorChannel, 1, p, i, d)

def setPositionPIDCoefficients(commObj, destination, motorChannel, p, i, d):
    """Set motor PID coefficients for run to position"""
    setMotorPIDCoefficients(commObj, destination, motorChannel, 2, p, i, d)

def getVelocityPIDCoefficients(commObj, destination, motorChannel):
    """Get motor PID coefficients for run using encoder"""
    return getMotorPIDCoefficients(commObj, destination, motorChannel, 1)

def getPositionPIDCoefficients(commObj, destination, motorChannel):
    """Get motor PID coefficients for run to position"""
    return getMotorPIDCoefficients(commObj, destination, motorChannel, 2)

class Motor:
    """Motor device type"""
    def __init__(self, commObj, channel, destinationModule):
        self.channel = channel
        self.destinationModule = destinationModule
        self.commObj = commObj
        self.motorCurrent = REVADC.ADCPin(self.commObj, 8 + channel, self.destinationModule)

    def setDestination(self, destinationModule):
        """Set the destination module"""
        self.destinationModule = destinationModule
        self.motorCurrent.setDestination(destinationModule)

    def getDestination(self):
        """Get the destination module"""
        return self.destinationModule

    def setChannel(self, channel):
        """Set the channel"""
        self.channel = channel

    def getChannel(self):
        """Get the channel"""
        return self.channel

    def setMode(self, mode, zeroFloat):
        """Set the mode and zero power behavior"""
        setMotorChannelMode(self.commObj, self.destinationModule, self.channel, mode, zeroFloat)

    def getMode(self):
        """Get the mode and zero power behavior"""
        return getMotorChannelMode(self.commObj, self.destinationModule, self.channel)

    def enable(self):
        """Enable the motor"""
        setMotorChannelEnable(self.commObj, self.destinationModule, self.channel, 1)

    def disable(self):
        """Disable the motor"""
        setMotorChannelEnable(self.commObj, self.destinationModule, self.channel, 0)

    def isEnabled(self):
        """Check if the motor is enabled"""
        return getMotorChannelEnable(self.commObj, self.destinationModule, self.channel)

    def setCurrentLimit(self, limit):
        """Set the current alert"""
        setMotorChannelCurrentAlertLevel(self.commObj, self.destinationModule, self.channel, limit)

    def getCurrentLimit(self):
        """Get the current alert"""
        return getMotorChannelCurrentAlertLevel(self.commObj, self.destinationModule, self.channel)

    def resetEncoder(self):
        """Reset motor encoder to zero, functionally identical to resetPosition()"""
        resetMotorEncoder(self.commObj, self.destinationModule, self.channel)

    def setPower(self, powerLevel):
        """Set motor power"""
        setMotorConstantPower(self.commObj, self.destinationModule, self.channel, powerLevel)

    def getPower(self):
        """Get motor power"""
        return getMotorConstantPower(self.commObj, self.destinationModule, self.channel)


    def setTargetVelocity(self, velocity):
        """Set motor target velocity"""
        setMotorTargetVelocity(self.commObj, self.destinationModule, self.channel, velocity)

    def getTargetVelocity(self):
        """Get motor target velocity"""
        return getMotorTargetVelocity(self.commObj, self.destinationModule, self.channel)

    def setTargetPosition(self, position, tolerance):
        """Set motor target position"""
        setMotorTargetPosition(self.commObj, self.destinationModule, self.channel, position, tolerance)

    def getTargetPosition(self):
        """Get motor target position"""
        return getMotorTargetPosition(self.commObj, self.destinationModule, self.channel)

    def isAtTarget(self):
        """Check if the motor has reached its target position"""
        return getMotorAtTarget(self.commObj, self.destinationModule, self.channel)

    def getPosition(self):
        """Get the current encoder positon"""
        position = getMotorEncoderPosition(self.commObj, self.destinationModule, self.channel)
        return position

    def resetPosition(self):
        """Reset motor encoder to zero, functionally identical to resetEncoder()"""
        resetMotorEncoder(self.commObj, self.destinationModule, self.channel)

    def getVelocity(self):
        """Get motor velocity"""
        bulkData = REVModule.getBulkInputData(self.commObj, self.destinationModule)
        val = int(bulkData[self.channel + VELOCITY_OFFSET])
        bits = int(16)
        if val & 1 << bits - 1 != 0:
            val = val - (1 << bits)
        return val

    def getCurrent(self):
        """Get motor current draw in amps (?)"""
        return self.motorCurrent.getADC(0)

    def setVelocityPID(self, p, i, d):
        """Set velocity PID Coefficients"""
        setVelocityPIDCoefficients(self.commObj, self.destinationModule, self.channel, p, i, d)

    def getVelocityPID(self):
        """Get velocity PID Coefficients"""
        return getVelocityPIDCoefficients(self.commObj, self.destinationModule, self.channel)

    def setPositionPID(self, p, i, d):
        """Set position PID Coefficients"""
        setPositionPIDCoefficients(self.commObj, self.destinationModule, self.channel, p, i, d)

    def getPositionPID(self):
        """Get position PID Coefficients"""
        return getPositionPIDCoefficients(self.commObj, self.destinationModule, self.channel)

    def init(self):
        """Initalize the motor to constant power and coast breaking mode"""
        self.setMode(0, 1)
        self.setPower(0)
        self.enable()

#Motor constants
Q16 = 65536.0
MODE_CONSTANT_POWER = 0
MODE_CONSTANT_VELOCITY = 1
MODE_POSITION_TARGET = 2
BRAKE_AT_ZERO = 0
FLOAT_AT_ZERO = 1
VELOCITY_OFFSET = 6
CURRENT_OFFSET = 8