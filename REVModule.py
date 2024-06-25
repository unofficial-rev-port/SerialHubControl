from SDKDevice import REVMotor
import REVServo, REVADC, REVDIO, REVI2C

##Note: Modules are hubs (lynx modules)
class Module:
    """Lynx Module device"""
    def __init__(self, commObj, address, parent, manualBulkread = True):
        self.commObj = commObj
        self.address = address
        self.parent = parent
        self.motors = []
        self.servos = []
        self.i2cChannels = []
        self.adcPins = []
        self.dioPins = []
        self.bulkInputData = None
        self.analogInput = []
        self.digitalInput = []
        self.encoderPosition = []
        self.encoderVelocity = []
        self.motorIsOvercurrent = []
        self.isBulkread = manualBulkread


    def init_periphs(self):
        """Initalizes all devices (Motors, Servos, Digital I/O, and ADC"""
        for i in range(0, 4):
            self.motors.append(REVMotor.Motor(self.commObj, i, self.address, self))
            self.motors[-1].setMode(0, 1)
            self.motors[-1].setPower(0)
            self.i2cChannels.append(REVI2C.I2CChannel(self.commObj, i, self.address))

        for j in range(0, 8):
            self.dioPins.append(REVDIO.DIOPin(self.commObj, j, self.address))

        for k in range(0, 6):
            self.servos.append(REVServo.Servo(self.commObj, k, self.address, self))
            self.servos[-1].init()

        for l in range(0, 4):
            self.adcPins.append(REVADC.ADCPin(self.commObj, l, self.address))

    def killSwitch(self):
        """Disable everything for safe stop"""
        for i in range(0, 4):
            self.motors[i].disable()

        for k in range(0, 6):
            self.servos[k].disable()

    def getParentStatus(self):
        """Get status of parent module (?)"""
        return self.parent

    def getAddress(self):
        """Get address of lynx module, functionally identical to getModuleAddress()"""
        return self.address

    def getStatus(self):
        """Get lynx module """
        return self.commObj.getModuleStatus(self.address)

    def getModuleAddress(self):
        """Get address of lynx module, functionally identical to getAddress()"""
        return self.address

    def sendKA(self):
        """Keep alive for lynx module"""
        return self.commObj.keepAlive(self.address)

    def sendFailSafe(self):
        """Failsafe for lynx module"""
        self.commObj.failSafe(self.address)

    def setAddress(self, newAddress):
        """Set the address of the lynx module and update all devices addresses"""
        self.commObj.setNewModuleAddress(self.address, newAddress)
        self.address = newAddress
        for motor in self.motors:
            motor.setDestination(newAddress)

        for servo in self.servos:
            servo.setDestination(newAddress)

        for i2cChannel in self.i2cChannels:
            i2cChannel.setDestination(newAddress)

        for adcPin in self.adcPins:
            adcPin.setDestination(newAddress)

        for dioPin in self.dioPins:
            dioPin.setDestination(newAddress)

    def getInterface(self, interface):
        """Get the interface of the lynx module, direct serial or RS485 (?)"""
        return self.commObj.queryInterface(self.address, interface)

    def setLEDColor(self, red, green, blue):
        """Set the color of the LED on the lynx module"""
        self.commObj.setModuleLEDColor(self.address, red, green, blue)

    def getLEDColor(self):
        """Get the current RGB value of the lynx module"""
        return self.commObj.getModuleLEDColor(self.address)

    def setLEDPattern(self, pattern):
        """ 
      Set a LED patern for the LED of the lynx module
      Example:
      from REVmessages import LEDPattern

      hub = REVModules()
      my_pattern = LEDPattern()
      my_pattern.set_step(0, 255, 0, 0, 10) # set first step to red for 1 second
      my_pattern.set_step(1, 0, 255, 0, 10) # set second step to green for 1 second
      hub.REVModules[0].setLEDPattern(my_pattern)
      hub.REVModules[0].keepAlive()
      """
        return self.commObj.setModuleLEDPattern(self.address, pattern)

    def setLogLevel(self, group, verbosity):
        """Set the logging level"""
        self.commObj.debugLogLevel(self.address, group, verbosity)

    def getBulkData(self):
        """Get bulk input data, analagous to FTC SDK bulkread"""
        return self.commObj.getBulkInputData(self.address)

    def enableCharging(self):
        """Enable Android Phone charging"""
        self.commObj.phoneChargeControl(self.address, 1)

    def disableCharging(self):
        """Disable Android Phone charging"""
        self.commObj.phoneChargeControl(self.address, 0)

    def chargingEnabled(self):
        """Check android phone charging state"""
        return self.commObj.phoneChargeQuery(self.address)

    def debugOutput(self, length, hint):
        """Debug the output"""
        self.commObj.injectDataLogHint(self.address, length, hint)

    def setAllDIO(self, values):
        """Set all Digital I/O"""
        REVDIO.setAllDIOOutputs(self.address, values)

    def getAllDIO(self):
        """Read all Digital I/O"""
        return REVDIO.getAllDIOInputs(self.address)

    def getVersionString(self):
        """Read the firmware version"""
        versionRaw = '' + self.commObj.readVersionString(self.address)
        versionStr = ''
        for i in range(0, int(len(versionRaw) / 2)):
            tmpHex = int(str(versionRaw)[i * 2] + str(versionRaw)[i * 2 + 1], 16)
            versionStr = versionStr + chr(tmpHex)
        return versionStr

    def setIMUBlockReadConfig(self, startRegister, numberOfBytes, readInterval_ms):
        """Set the Configuration of IMU block read"""
        REVI2C.imuBlockReadConfig(self.address, startRegister, numberOfBytes, readInterval_ms)

    def getIMUBlockReadConfig(self):
        """Get the configuration of IMU block read"""
        return REVI2C.imuBlockReadQuery(self.address)

    def getBulkRead(self):
        if self.bulkInputData != None:
            return self.bulkInputData
        else:
            self.bulkInputData = self.getBulkData()
            return self.bulkInputData

    def invalidateBulkCache(self):
        self.bulkInputData = None
        self.analogInput = []
        self.digitalInput = []
        self.encoderPosition = []
        self.encoderVelocity = []
        self.motorIsOvercurrent = []

    def parseBulkData(self):
        read = self.getBulkRead()
        for port in range(0,4):
            self.analogInput[port] = int((read[port + ANALOG_OFFSET] & (1 << (16 - 1))))

        for port in range(0,4):
            self.digitalInput[port] = bool(read[DIGITAL_OFFSET] & 1)

        for port in range(0,4):
            self.encoderPosition[port] = int(read[port + POSITION_OFFSET])

        for port in range(0,4):
            self.encoderVelocity[port] = int((read[port + VELOCITY_OFFSET] & (1 << (16 - 1))))

        for port in range(0,4):
            self.motorIsOvercurrent[port] = bool(read[STATUS_OFFSET] & 1)
        

    def isBulkread(self):
        return self.isBulkread

    def getAnalog(self, port):
        return self.analogInput[port]
    
    def getEncoderPosition(self, port):
        return self.encoderPosition[port]

    def getEncoderVelocity(self, port):
        return self.encoderVelocity[port]
    
    def getDigitalIO(self, port):
        return self.digitalInput[port]
    
    def getIsOverCurrent(self, port):
        return self.motorIsOvercurrent[port]

VELOCITY_OFFSET = 6
ANALOG_OFFSET = 10
DIGITAL_OFFSET = 0
POSITION_OFFSET = 1
STATUS_OFFSET = 5