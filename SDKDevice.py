import REVServo, REVMotor, REVModule

class dcmotor:
    def __init__(self, commObj, port, module):
        self.port = port
        self.module = module
        self.commObj = commObj
        self.current =  REVADC.ADCPin(self.commObj, 8 + port, self.module)W
        self.mode = MODE_CONSTANT_POWER
        self.zeroPowerBehavior = FLOAT_AT_ZERO
        self.enabled = true
        self.currentLimit = null
        self.power = 0
        self.targetPosition = null
        self.targetVelocity = null
        self.velocityPIDCoefficients = (null, null, null)
        self.positionPIDCoefficients = (null, null, null)

    def setMode(self, mode):
        setMotorChannelMode(self.commObj, self.module, self.port, mode, self.zeroPowerBehavior)
        self.mode = mode

    def getMode(self):
        return getmotorChannelmode(self, self.module, self.port)[0]

    def setZeroPowerBehavior(self, zeroPowerBehavior):
        setMotorChannelMode(self.commObj, self.module, self.port, self.mode, self.zeroPowerBehavior)
        self.zeroPowerBehavior = zeroPowerBehavior

    def getZeroPowerBehavior(self):
        return self.zeroPowerBehavior
    
    def enable(self, enable):
        setMotorChannelEnable(self.commObj, self.module, self.port, int(enable))
        self.enabled = enable

    def isEnabled(self):
        return self.enabled

    def setCurrentAlert(self, current):
        setMotorChannelCurrentAlertLevel(self.commObj, self.module, self.port, current)
        self.currentLimit = current
    
    def getCurrentLimit(self):
        return self.currentLimit
    
    def isOverCurrent(self):
        return null
    
    def stopAndResetEncoder(self):
        enable(False)
        resetMotorEncoder(self.commObj, self.module, self.port)
        enable(True)

    def setPower(self, power):
        self.power = power
        setMotorConstantPower(self.commObj, self.module, self.port, power)

    def getPower(self):
        return self.power
    
    def setTargetVelocity(self, velocity):
        self.targetVelocity = velocity
        setMotorTargetVelocity(self.commObj, self.module, self.port, velocity)

    def getTargetVelocity(self):
        return self.targetVelocity

    def setTargetPosition(self, position, tolerance = 20):
        self.targetPosition = position
        setMotorTargetPosition(self.commObj, self.module, self.port, position, tolerance)

    def getTargetPosition(self):
        return self.targetPosition

    def atTarget(self):
        return getMotorAtTarget(self.commObj, self.module, self.port)

    def getVelocity(self):
        bulkData = REVModule.getBulkInputData(self.commObj, self.module)
        val = int(bulkData[self.port + VELOCITY_OFFSET])
        bits = int(16)
        if val & 1 << bits - 1 != 0:
            val = val - (1 << bits)
        return val
    
    def getPosition(self):
        return getMotorEncoderPosition(self.commObj, self.module, self.port)

    def getCurrent(self):
        return self.motorCurrent.getADC(0)

    def setVelocityPID(self, p, i, d):
        self.velocityPIDCoefficients = (p, i, d)
        setVelocityPIDCoefficients(self.commObj, self.module, self.port, p, i, d)

    def getVelocityPID(self):
        return self.velocityPIDCoefficients

    def setPositionPID(self, p, i, d):
        self.positionPIDCoefficients = (p, i, d)
        setPositionPIDCoefficients(self.commObj, self.module, self.port, p, i, d)

    def getPositionPID(self):
        return self.positionPIDCoefficients

class encoder:
    def __init__(self, commObj, port, module):
        self.port = port
        self.module = module
        self.commObj = commObj
    
    def getPosition(self):
        return getMotorEncoderPosition(self.commObj, self.module, self.port)

    def resetEncoder(self):
        resetMotorEncoder(self.commObj, self.module, self.port)
        
    def getVelocity(self):
        bulkData = REVModule.getBulkInputData(self.commObj, self.module)
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
        self.position = null
        self.range = range
        self.isEnabled = true

    def setPosition(self, position):
        self.position = position
        SetPWMPulseWidth((min(max(position, 0), 1) * self.range)
    
    def getPosition(self):
        return self.position
    
    def setPwmRange(self, range):
        self.range = range
        setPeriod(range)

    def getPwmRange(self):
        return self.range
    
    def enable(self, enable):
        setServoEnable(self.commObj, self.destinationModule, self.channel, int(enable))
    
    def isEnabled(self):
        return self.isEnabled

class colorSensorV3:
    def __init__(self):