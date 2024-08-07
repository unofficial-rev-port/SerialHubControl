from . import REVMessage as REVMsg

##Servo driver
def setServoConfiguration(commObj, destination, servoChannel, framePeriod):
    """Set pwm range for a servo"""
    setServoConfigurationMsg = REVMsg.SetServoConfiguration()
    setServoConfigurationMsg.payload.servoChannel = servoChannel
    setServoConfigurationMsg.payload.framePeriod = framePeriod
    return commObj.sendAndReceive(setServoConfigurationMsg, destination)

def getServoConfiguration(commObj, destination, servoChannel):
    """Get pwm range for a servo"""
    getServoConfigurationMsg = REVMsg.GetServoConfiguration()
    getServoConfigurationMsg.payload.servoChannel = servoChannel
    packet = commObj.sendAndReceive(getServoConfigurationMsg, destination)
    return packet.payload.framePeriod

def setServoPulseWidth(commObj, destination, servoChannel, pulseWidth):
    """Set pulse width for servo"""
    setServoPulseWidthMsg = REVMsg.SetServoPulseWidth()
    setServoPulseWidthMsg.payload.servoChannel = servoChannel
    setServoPulseWidthMsg.payload.pulseWidth = pulseWidth
    return commObj.sendAndReceive(setServoPulseWidthMsg, destination)

def getServoPulseWidth(commObj, destination, servoChannel):
    """Get pulse width for servo"""
    getServoPulseWidthMsg = REVMsg.GetServoPulseWidth()
    getServoPulseWidthMsg.payload.servoChannel = servoChannel
    packet = commObj.sendAndReceive(getServoPulseWidthMsg, destination)
    return packet.payload.pulseWidth

def setServoEnable(commObj, destination, servoChannel, enable):
    """Enable/disable a servo"""
    setServoEnableMsg = REVMsg.SetServoEnable()
    setServoEnableMsg.payload.servoChannel = servoChannel
    setServoEnableMsg.payload.enable = enable
    return commObj.sendAndReceive(setServoEnableMsg, destination)

def getServoEnable(commObj, destination, servoChannel):
    """Check enable/disable state for a servo"""
    getServoEnableMsg = REVMsg.GetServoEnable()
    getServoEnableMsg.payload.servoChannel = servoChannel
    packet = commObj.sendAndReceive(getServoEnableMsg, destination)
    return packet.payload.enabled

class internalServo:
    def __init__(self, commObj, channel, destinationModule, sourceModule):
        self.commObj = commObj
        self.destinationModule = destinationModule
        self.channel = channel
        self.isEnabled = True
        self.period = None
        self.pulseWidth = None
        self.revMod = sourceModule

    def setDestination(self, destinationModule):
        """Set destination lynx module for a servo"""
        self.destinationModule = destinationModule

    def getDestination(self):
        """Get destination lynx module for a servo"""
        return self.destinationModule

    def setChannel(self, channel):
        """Set port for servo"""
        self.channel = channel

    def getChannel(self):
        """Get port for servo"""
        return self.channel

    def setPeriod(self, period):
        """Set servo period"""
        setServoConfiguration(self.commObj, self.destinationModule, self.channel, period)
        self.period = period

    def getPeriod(self):
        """Get servo period"""
        return self.period

    def setPulseWidth(self, pulseWidth):
        """Set the pulse width for the servo"""
        setServoPulseWidth(self.commObj, self.destinationModule, self.channel, pulseWidth)

    def getPulseWidth(self):
        """Get the pulse width for the servo"""
        return self.pulseWidth

    def enable(self):
        """Enable the servo"""
        setServoEnable(self.commObj, self.destinationModule, self.channel, 1)

    def disable(self):
        """Disable the servo"""
        setServoEnable(self.commObj, self.destinationModule, self.channel, 0)

    def isEnabled(self):
        """Check if a servo is enabled"""
        return self.enable

    def init(self):
        """Setup the servo"""
        self.setPeriod(20000)