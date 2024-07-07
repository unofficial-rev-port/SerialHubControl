from . import REVMessage as REVMsg
from REVConstants import *

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