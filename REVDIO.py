import REVMessage as REVMsg

def setSingleDIOOutput(commObj, destination, dioPin, value):
    """Set a single Digital IO output pin"""
    setSingleDIOOutput = REVMsg.SetSingleDIOOutput()
    setSingleDIOOutput.payload.dioPin = dioPin
    setSingleDIOOutput.payload.value = value
    commObj.sendAndReceive(setSingleDIOOutput, destination)

def setAllDIOOutputs(commObj, destination, values):
    """Set all Digital IO output pins"""
    setAllDIOOutputs = REVMsg.SetAllDIOOutputs()
    setAllDIOOutputs.payload.values = values
    commObj.sendAndReceive(setAllDIOOutputs, destination)

def setDIODirection(commObj, destination, dioPin, directionOutput):
    """Set a Digital IO pin to read or write"""
    setDIODirection = REVMsg.SetDIODirection()
    setDIODirection.payload.dioPin = dioPin
    setDIODirection.payload.directionOutput = directionOutput
    commObj.sendAndReceive(setDIODirection, destination)

def getDIODirection(commObj, destination, dioPin):
    """Get whether a Digital IO pin is read or write"""
    getDIODirection = REVMsg.GetDIODirection()
    getDIODirection.payload.dioPin = dioPin
    packet = commObj.sendAndReceive(getDIODirection, destination)
    return packet.payload.directionOutput

def getSingleDIOInput(commObj, destination, dioPin):
    """Get a single Digital IO input pin"""
    getSingleDIOInput = REVMsg.GetSingleDIOInput()
    getSingleDIOInput.payload.dioPin = dioPin
    packet = commObj.sendAndReceive(getSingleDIOInput, destination)
    return packet.payload.inputValue

def getAllDIOInputs(commObj, destination):
    """Read all Digital IO input pins"""
    getAllDIOInputs = REVMsg.GetAllDIOInputs()
    packet = commObj.sendAndReceive(getAllDIOInputs, destination)
    return packet.payload.inputValues

class DIOPin:
    """Digitial GPIO pin driver"""
    def __init__(self, commObj, pinNumber, destinationModule):
        self.destinationModule = destinationModule
        self.pinNumber = pinNumber
        self.commObj = commObj

    def setDestination(self, destinationModule):
        """Set the destination lynx module for a Digitial IO command"""
        self.destinationModule = destinationModule

    def getDestination(self):
        """Get the destination lynx module for Digital IO"""
        return self.destinationModule

    def setPinNumber(self, pinNumber):
        """Set which Digital IO pin is addressed"""
        self.pinNumber = pinNumber

    def getPinNumber(self):
        """Get the pin that is being addressed"""
        return self.pinNumber

    def setOutput(self, value):
        """Set the value to an output Digital IO pin"""
        setSingleDIOOutput(self.commObj, self.destinationModule, self.pinNumber, value)

    def getInput(self):
        """Read input Digital IO pin"""
        return getSingleDIOInput(self.commObj, self.destinationModule, self.pinNumber)

    def setAsOutput(self):
        """Set a Digital IO pin as output"""
        setDIODirection(self.commObj, self.destinationModule, self.pinNumber, 1)

    def setAsInput(self):
        """Set a Digital IO pin as input"""
        setDIODirection(self.commObj, self.destinationModule, self.pinNumber, 0)

    def getDirection(self):
        """Get input/output state of a Digital IO pin"""
        getDIODirection(self.commObj, self.destinationModule, self.pinNumber)