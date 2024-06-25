import REVServo, REVMotor, REVDIO, REVADC

class dcmotor:
    def __init__(self, commObj, port, module, sourceModule):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.revMod = sourceModule
        self.internal = REVMotor(self.commObj, self.port, self.module, self.revMod)

    def setMode(self, mode):
        self.internal.setMotorChannelMode(self.commObj, self.module, self.port, mode, self.zeroPowerBehavior)
        self.mode = mode

    def getMode(self):
        return self.internal.getmotorChannelmode(self, self.module, self.port)[0]

    def setZeroPowerBehavior(self, zeroPowerBehavior):
        self.internal.setMotorChannelMode(self.commObj, self.module, self.port, self.mode, self.zeroPowerBehavior)
        self.zeroPowerBehavior = zeroPowerBehavior

    def getZeroPowerBehavior(self):
        return self.zeroPowerBehavior
    
    def enable(self, enable):
        self.internal.setMotorChannelEnable(self.commObj, self.module, self.port, int(enable))
        self.enabled = enable

    def isEnabled(self):
        return self.enabled

    def setCurrentAlert(self, current):
        self.internal.setMotorChannelCurrentAlertLevel(self.commObj, self.module, self.port, current)
        self.currentLimit = current
    
    def getCurrentLimit(self):
        return self.currentLimit
    
    def isOverCurrent(self):
        return self.revMod.isOverCurrent(self.port)
    
    def stopAndResetEncoder(self):
        self.enable(False)
        self.internal.resetMotorEncoder(self.commObj, self.module, self.port)
        self.enable(True)

    def setPower(self, power):
        self.power = power
        self.internal.setMotorConstantPower(self.commObj, self.module, self.port, power)

    def getPower(self):
        return self.power
    
    def setTargetVelocity(self, velocity):
        self.targetVelocity = velocity
        self.internal.setMotorTargetVelocity(self.commObj, self.module, self.port, velocity)

    def getTargetVelocity(self):
        return self.targetVelocity

    def setTargetPosition(self, position, tolerance = 20):
        self.targetPosition = position
        self.internal.setMotorTargetPosition(self.commObj, self.module, self.port, position, tolerance)

    def getTargetPosition(self):
        return self.targetPosition

    def atTarget(self):
        return self.getMotorAtTarget(self.commObj, self.module, self.port)

    def getVelocity(self):
        if self.revMod.isBulkread():
            return self.revMod.getEncoderVelocity[self.port]
        else: 
            return self.internal.getVelocity()
    
    def getPosition(self):
        if self.revMod.isBulkread():
            return self.revMod.getEncoderPosition[self.port]
        else:
            return self.internal.getMotorEncoderPosition(self.commObj, self.module, self.port)

    def getCurrent(self):
        return self.motorCurrent.getADC(0)

    def setVelocityPID(self, p, i, d):
        self.velocityPIDCoefficients = (p, i, d)
        self.internal.setVelocityPIDCoefficients(self.commObj, self.module, self.port, p, i, d)

    def getVelocityPID(self):
        return self.velocityPIDCoefficients

    def setPositionPID(self, p, i, d):
        self.positionPIDCoefficients = (p, i, d)
        self.internal.setPositionPIDCoefficients(self.commObj, self.module, self.port, p, i, d)

    def getPositionPID(self):
        return self.positionPIDCoefficients

class encoder:
    def __init__(self, commObj, port, module):
        self.port = port
        self.module = module
        self.commObj = commObj
    
    def getPosition(self):
        return self.internal.getMotorEncoderPosition(self.commObj, self.module, self.port)

    def resetEncoder(self):
        self.internal.resetMotorEncoder(self.commObj, self.module, self.port)
        
    def getVelocity(self):
        return self.internal.getVelocity(
        if self.revMod.isBulkread():
            return self.revMod.getEncoderVelocity[self.port]
        else:
            bulkData = self.revMod.getBulkInputData(self.commObj, self.module)
            val = int(bulkData[self.port + VELOCITY_OFFSET])
            bits = int(16)
            if val & 1 << bits - 1 != 0:
                val = val - (1 << bits)
            return val

class servo:
    def __init__(self, commObj, port, module):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.position = NotImplementedError
        self.range = range
        self.isEnabled = True
        self.internal = REVServo()

    def setPosition(self, position):
        self.position = position
        self.internal.SetPWMPulseWidth((min(max(position, 0), 1) * self.range))
    
    def getPosition(self):
        return self.position
    
    def setPwmRange(self, range):
        self.range = range
        self.internal.setPeriod(range)

    def getPwmRange(self):
        return self.range
    
    def enable(self, enable):
        self.internal.setServoEnable(self.commObj, self.destinationModule, self.channel, int(enable))
    
    def isEnabled(self):
        return self.isEnabled
