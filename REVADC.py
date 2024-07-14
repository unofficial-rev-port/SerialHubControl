import REVComm
from . import REVMessage as REVMsg
from REVConstants import *

##Note: appears to just be part of the current sensing for motors? (ADC = analog digital converter)
class ADCPin:
    """Driver for ADC (current and voltage sensors mostly)"""
    def __init__(self, commObj: REVComm.REVcomm, channel: int, destinationModule: int):
        self.commObj = commObj
        self.channel = channel
        self.destinationModule = destinationModule

    def setDestination(self, destinationModule: int):
        """Set ADC destination module"""
        self.destinationModule = destinationModule

    def getDestination(self) -> int:
        """Get set destination module"""
        return self.destinationModule

    def setChannel(self, channel: int):
        """Set the ADC Channel"""
        self.channel = channel

    def getChannel(self) -> int:
        """Get ADC Channel"""
        return self.channel

    def getADC(self, rawMode):
        """Get all ADC (?)"""
        getADC = REVMsg.GetADC()
        getADC.payload.adcChannel = self.channel
        getADC.payload.rawMode = rawMode
        packet = self.commObj.sendAndReceive(getADC, self.destinationModule)
        return packet.payload.adcValue
