from . import REVMessage as REVMsg

##Some constants
ADC_INPUT_CHANNEL_0 = 0
ADC_INPUT_CHANNEL_1 = 1
ADC_INPUT_CHANNEL_2 = 2
ADC_INPUT_CHANNEL_3 = 3
GPIO_CURRENT = 4
I2C_BUS_CURRENT = 5
SERVO_CURRENT = 6
BATTERY_CURRENT = 7
MOTOR_CHANNEL_0_CURRENT = 8
MOTOR_CHANNEL_1_CURRENT = 9
MOTOR_CHANNEL_2_CURRENT = 10
MOTOR_CHANNEL_3_CURRENT = 11
VOLTAGE_5V_MONITOR = 12
VOLTAGE_BATTERY_MONITOR = 13
CONTROLLER_TEMPERATURE = 14

##Note: appears to just be part of the current sensing for motors? (ADC = analog digital converter)
class ADCPin:
    """Driver for ADC (current and voltage sensors mostly)"""
    def __init__(self, commObj, channel, destinationModule):
        self.commObj = commObj
        self.channel = channel
        self.destinationModule = destinationModule

    def setDestination(self, destinationModule):
        """Set ADC destination module"""
        self.destinationModule = destinationModule

    def getDestination(self):
        """Get set destination module"""
        return self.destinationModule

    def setChannel(self, channel):
        """Set the ADC Channel"""
        self.channel = channel

    def getChannel(self):
        """Get ADC Channel"""
        return self.channel

    def getADC(self, rawMode):
        """Get all ADC (?)"""
        getADC = REVMsg.GetADC()
        getADC.payload.adcChannel = self.channel
        getADC.payload.rawMode = rawMode
        packet = self.commObj.sendAndReceive(getADC, self.destinationModule)
        return packet.payload.adcValue