import REVServo, REVMotor, REVDIO, REVADC

class dcmotor:
    def __init__(self, commObj, port, module, sourceModule):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.revMod = sourceModule
        self.internal = REVMotor(self.commObj, self.port, self.module, self.revMod)

    def setMode(self, mode):
        self.internal.setMode(mode, self.internal.getMode()[1])

    def getMode(self):
        return self.internal.getMode()[0]

    def getZeroPowerBehavior(self):
        return self.internal.getMode()[1]
    
    def setZeroPowerBehavior(self, zeroPowerBehavior):
        self.internal.setMode(self.internal.getMode()[0], zeroPowerBehavior)

    def enable(self):
        self.internal.enable()

    def disable(self):
        self.internal.disbale()

    def isEnabled(self):
        return self.internal.isEnabled()

    def setCurrentAlert(self, current):
        self.internal.setCurrentLimit(current)
    
    def getCurrentAlert(self):
        return self.internal.getCurrentLimit()
    
    def isOverCurrent(self):
        return self.internal.isOverCurrent()
    
    def stopAndResetEncoder(self):
        self.enable(False)
        self.internal.resetPosition()
        self.enable(True)

    def setPower(self, power):
        self.internal.setPower(power)

    def getPower(self):
        return self.internal.getPower()
    
    def setTargetVelocity(self, velocity):
        self.internal.setTargetVelocity(velocity)

    def getTargetVelocity(self):
        return self.internal.targetVelocity()

    def setTargetPosition(self, position, tolerance = 20):
        self.internal.setTargetPosition(position, tolerance)

    def getTargetPosition(self):
        return self.internal.getTargetPosition()

    def atTarget(self):
        return self.internal.isAtTarget()

    def getVelocity(self):
        return self.internal.getVelocity()
    
    def getPosition(self):
        return self.internal.getPosition()

    def getCurrent(self):
        return self.internal.getCurrent()

    def setVelocityPID(self, p, i, d):
        self.internal.setVelocityPIDCoefficients(p, i, d)

    def getVelocityPID(self):
        return self.internal.getVelocityPID()

    def setPositionPID(self, p, i, d):
        self.internal.setPositionPIDCoefficients(p, i, d)

    def getPositionPID(self):
        return self.internal.getPositionPID()

class encoder:
    def __init__(self, commObj, port, module, sourceModule):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.revMod = sourceModule
        self.internal = REVMotor(self.commObj, self.port, self.module, self.revMod)
    
    def getPosition(self):
        return self.internal.getPositon()

    def resetEncoder(self):
        self.internal.resetPosition()
        
    def getVelocity(self):
        return self.internal.getVelocity()

class servo:
    def __init__(self, commObj, port, module, sourceModule):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.revMod = sourceModule
        self.internal = REVServo(self.commObj, self.port, self.module, self.revMod)

    def setPosition(self, position):
        self.internal.setPosition(position)
    
    def getPosition(self):
        return self.internal.getPosition()
    
    def setPwmRange(self, range):
        self.internal.setPeriod(range)

    def getPwmRange(self):
        return self.internal.getPeriod()
    
    def enable(self):
        self.internal.enable()
    
    def isEnabled(self):
        return self.internal.isEnabled()
