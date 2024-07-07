from . import REVMessage as REVMsg
import time
from REVConstants import *

def i2cWriteSingleByte(commObj, destination, i2cChannel, slaveAddress, byteToWrite):
    """Write a single I2C byte"""
    i2cWriteSingleByteMsg = REVMsg.I2CWriteSingleByte()
    i2cWriteSingleByteMsg.payload.i2cChannel = i2cChannel
    i2cWriteSingleByteMsg.payload.slaveAddress = slaveAddress
    i2cWriteSingleByteMsg.payload.byteToWrite = byteToWrite
    commObj.sendAndReceive(i2cWriteSingleByteMsg, destination)


def i2cWriteMultipleBytes(commObj, destination, i2cChannel, slaveAddress, numBytes, bytesToWrite):
    """Write multiple I2C bytes"""
    i2cWriteMultipleBytesMsg = REVMsg.I2CWriteMultipleBytes()
    i2cWriteMultipleBytesMsg.payload.i2cChannel = i2cChannel
    i2cWriteMultipleBytesMsg.payload.slaveAddress = slaveAddress
    i2cWriteMultipleBytesMsg.payload.numBytes = numBytes
    i2cWriteMultipleBytesMsg.payload.bytesToWrite = bytesToWrite
    commObj.sendAndReceive(i2cWriteMultipleBytesMsg, destination)


def i2cWriteStatusQuery(commObj, destination, i2cChannel):
    """Check status of I2C write"""
    i2cWriteStatusQueryMsg = REVMsg.I2CWriteStatusQuery()
    i2cWriteStatusQueryMsg.payload.i2cChannel = i2cChannel
    packet = commObj.sendAndReceive(i2cWriteStatusQueryMsg, destination)
    return (packet.payload.i2cStatus, packet.payload.numBytes)


def i2cReadSingleByte(commObj, destination, i2cChannel, slaveAddress):
    """Read a single I2C byte"""
    i2cReadSingleByteMsg = REVMsg.I2CReadSingleByte()
    i2cReadSingleByteMsg.payload.i2cChannel = i2cChannel
    i2cReadSingleByteMsg.payload.slaveAddress = slaveAddress
    commObj.sendAndReceive(i2cReadSingleByteMsg, destination)


def i2cReadMultipleBytes(commObj, destination, i2cChannel, slaveAddress, numBytes):
    """Read Multiple I2C Bytes"""
    i2cReadMultipleBytesMsg = REVMsg.I2CReadMultipleBytes()
    i2cReadMultipleBytesMsg.payload.i2cChannel = i2cChannel
    i2cReadMultipleBytesMsg.payload.slaveAddress = slaveAddress
    i2cReadMultipleBytesMsg.payload.numBytes = numBytes
    commObj.sendAndReceive(i2cReadMultipleBytesMsg, destination)


def i2cReadStatusQuery(commObj, destination, i2cChannel):
    """Check status of I2C read"""
    i2cReadStatusQueryMsg = REVMsg.I2CReadStatusQuery()
    i2cReadStatusQueryMsg.payload.i2cChannel = i2cChannel
    packet = commObj.sendAndReceive(i2cReadStatusQueryMsg, destination)
    return (
     packet.payload.i2cStatus, packet.payload.byteRead, packet.payload.payloadBytes)


def i2cConfigureChannel(commObj, destination, i2cChannel, speedCode):
    """Configure an I2C channel"""
    i2cConfigureChannelMsg = REVMsg.I2CConfigureChannel()
    i2cConfigureChannelMsg.payload.i2cChannel = i2cChannel
    i2cConfigureChannelMsg.payload.speedCode = speedCode
    commObj.sendAndReceive(i2cConfigureChannelMsg, destination)


def i2cConfigureQuery(commObj, destination, i2cChannel):
    """Query I2C configure"""
    i2cConfigureQueryMsg = REVMsg.I2CConfigureQuery()
    i2cConfigureQueryMsg.payload.i2cChannel = i2cChannel
    packet = commObj.sendAndReceive(i2cConfigureQueryMsg, destination)
    return packet.payload.speedCode


def i2cBlockReadConfig(commObj, destination, i2cChannel, address, startRegister, numberOfBytes, readInterval_ms):
    """Config a repeating I2C block read"""
    i2cBlockReadConfigMsg = REVMsg.I2CBlockReadConfig()
    i2cBlockReadConfigMsg.channel = i2cChannel
    i2cBlockReadConfigMsg.address = address
    i2cBlockReadConfigMsg.startRegister = startRegister
    i2cBlockReadConfigMsg.numberOfBytes = numberOfBytes
    i2cBlockReadConfigMsg.readInterval_ms = readInterval_ms
    commObj.sendAndReceive(i2cBlockReadConfigMsg, destination)


def i2cBlockReadQuery(commObj, destination):
    """Query the current config for I2C Block Read"""
    i2cBlockReadQueryMsg = REVMsg.I2CBlockReadQuery()
    packet = commObj.sendAndReceive(i2cBlockReadQueryMsg, destination)
    return packet


def imuBlockReadConfig(commObj, destination, startRegister, numberOfBytes, readInterval_ms):
    """Configure IMU block read"""
    imuBlockReadConfigMsg = REVMsg.IMUBlockReadConfig()
    imuBlockReadConfigMsg.startRegister = startRegister
    imuBlockReadConfigMsg.numberOfBytes = numberOfBytes
    imuBlockReadConfigMsg.readInterval_ms = readInterval_ms
    commObj.sendAndReceive(imuBlockReadConfigMsg, destination)


def imuBlockReadQuery(commObj, destination):
    """Query the current IMU Block read config"""
    imuBlockReadQueryMsg = REVMsg.IMUBlockReadQuery()
    packet = commObj.sendAndReceive(imuBlockReadQueryMsg, destination)
    return packet


class I2CChannel:
    """Class for I2C device channel"""
    def __init__(self, commObj, channel, destinationModule):
        self.commObj = commObj
        self.channel = channel
        self.destinationModule = destinationModule
        self.devices = {}

    def setChannel(self, channel):
        """Set active channel for I2C"""
        self.channel = channel

    def getChannel(self):
        """Get the active channel for I2C"""
        return self.channel

    def setDestination(self, destinationModule):
        """Set destination Lynx module"""
        self.destinationModule = destinationModule

    def getDestination(self):
        """Get current destination Lynx module"""
        return self.destinationModule

    def addDevice(self, address, name):
        """Add a device to the device list for this channel"""
        self.devices[name] = I2CDevice(self.commObj, self.channel, self.destinationModule, address)

    def addColorSensor(self, name):
        """Add a color sensor to the device list for this channel"""
        self.devices[name] = ColorSensor(self.commObj, self.channel, self.destinationModule)

    def addIMU(self, name):
        """Add an IMU to the device list"""
        self.devices[name] = IMU(self.commObj, self.channel, self.destinationModule)

    def addI2CDevice(self, name, device):
        """Add an I2C device to the device list for this channel"""
        self.devices[name] = device

    def getDevices(self):
        """Read the connected devices on this channel"""
        return self.devices

    def setSpeed(self, speedCode):
        """Set the speed for this channel"""
        i2cConfigureChannel(self.destinationModule, self.channel, speedCode)
        return i2cConfigureQuery(self.destinationModule, self.channel)


class I2CDevice:
    """I2C Device class"""
    def __init__(self, commObj, channel, destinationModule, address):
        self.commObj = commObj
        self.channel = channel
        self.destinationModule = destinationModule
        self.address = address
        self.type = 'Generic'

    def setType(self, type):
        """Set the type of device"""
        self.type = type

    def getType(self):
        """Get the device type"""
        return self.type

    def setChannel(self, channel):
        """Set the channel of a device"""
        self.channel = channel

    def getChannel(self):
        """Get the channel of a device"""
        return self.channel

    def setDestination(self, destinationModule):
        """Set the destination Lynx Module for a device"""
        self.destinationModule = destinationModule

    def getDestination(self):
        """Get the destination lynx module for a device"""
        return self.destinationModule

    def setAddress(self, address):
        """Set address for a device"""
        self.address = address

    def getAddress(self):
        """Get the address for a device"""
        return self.address

    def writeByte(self, byteToWrite):
        """Write a single byte to I2C"""
        i2cWriteSingleByte(self.commObj, self.destinationModule, self.channel, self.address, byteToWrite)

    def writeMultipleBytes(self, numBytes, bytesToWrite):
        """Write multiple Bytes to I2C"""
        i2cWriteMultipleBytes(self.commObj, self.destinationModule, self.channel, self.address, numBytes, bytesToWrite)

    def readByte(self):
        """Read a single byte from I2C"""
        i2cReadSingleByte(self.commObj, self.destinationModule, self.channel, self.address)
        return int(i2cReadStatusQuery(self.commObj, self.destinationModule, self.channel)[2]) & 255

    def readMultipleBytes(self, numBytes):
        """Read Multiple bytes from I2C"""
        i2cReadMultipleBytes(self.commObj, self.destinationModule, self.channel, self.address, numBytes)
        byteMask = '0x'
        for i in range(0, numBytes):
            byteMask += 'FF'
        return int(i2cReadStatusQuery(self.commObj, self.destinationModule, self.channel)[2]) & int(byteMask, 16)

    def setBlockReadConfig(self, startRegister, numberOfBytes, readInterval_ms):
        """Set the block read configuration for an I2C device"""
        i2cBlockReadConfig(self.commObj, self.destinationModule, self.channel, self.address, startRegister, numberOfBytes, readInterval_ms)

    def getBlockReadConfig(self):
        """Get the block read config for an I2C device"""
        return i2cBlockReadQuery(self.commObj, self.destinationModule)

class ColorSensor(I2CDevice):
    """Color sensor I2C device type"""
    def __init__(self, commObj, channel, destinationModule):
        I2CDevice.__init__(self, commObj, channel, destinationModule, COLOR_SENSOR_ADDRESS)

    def initSensor(self):
        self.writeByte(COMMAND_REGISTER_BIT | ENABLE_REGISTER)
        self.writeByte(7)
        self.writeByte(COMMAND_REGISTER_BIT | ATIME_REGISTER)
        self.writeByte(255)
        self.writeByte(COMMAND_REGISTER_BIT | PPULSE_REGISTER)
        self.writeByte(8)
        try:
            ident = self.getDeviceID()
        except TypeError:
            ident = 255

        return ident == COLOR_SENSOR_ID

    def getEnable(self):
        """see if a device is enabled"""
        self.writeByte(COMMAND_REGISTER_BIT | ENABLE_REGISTER)
        byte1 = self.readByte()
        return byte1

    def getDominantColor(self):
        """Get the dominant RGB color from the sensor"""
        time.sleep(0.05)
        red = self.getRedValue()
        green = self.getGreenValue()
        blue = self.getBlueValue()
        RED = 0
        GREEN = 2
        BLUE = 1
        if red > blue and red > green:
            print('RED')
            return RED
        else:
            if blue > red and blue > green:
                print('BLUE')
                return BLUE
            if green > red and green > blue:
                print('GREEN')
                return GREEN
            return -1

    def getDeviceID(self):
        """Get the ID of an I2C device"""
        self.writeByte(COMMAND_REGISTER_BIT | MULTI_BYTE_BIT | ID_REGISTER)
        return self.readByte()

    def getGreenValue(self):
        """Get the Green value from the color sensor"""
        return self.getRegisterValue(GDATA_REGISTER)

    def getRedValue(self):
        """Get the Red value from the color sensor"""
        return self.getRegisterValue(RDATA_REGISTER)

    def getBlueValue(self):
        """Get the blue value from the color sensor"""
        return self.getRegisterValue(BDATA_REGISTER)

    def getClearValue(self):
        """Get the clear value from the color sensor"""
        return self.getRegisterValue(CDATA_REGISTER)

    def getProxValue(self):
        """Get the distance from the color sensor"""
        return self.getRegisterValue(PDATA_REGISTER)

    def getRegisterValue(self, register):
        """Get the register value"""
        self.writeByte(COMMAND_REGISTER_BIT | MULTI_BYTE_BIT | register)
        return self.readMultipleBytes(2)

class IMU(I2CDevice):
    """IMU I2C device type"""
    def __init__(self, commObj, channel, destinationModule):
        I2CDevice.__init__(self, commObj, channel, destinationModule, IMU_ADDRESS)

    def getDeviceID(self):
        """Get the chip id of the IMU"""
        return self.getRegisterValue(CHIP_ID)

    def initSensor(self):
        """Initialize the IMU"""
        for _ in range(3):
            self.setRegisterValue(OPR_MODE, CONFIGMODE)
            self.setRegisterValue(PWR_MODE, NORMAL)
            self.setRegisterValue(SYS_TRIGGER, 128)
            self.setRegisterValue(PAGE_ID, 0)
            self.setRegisterValue(UNIT_SEL, ACC_UNIT_MSS)
            self.setRegisterValue(OPR_MODE, IMUMODE)
            try:
                stat = self.getRegisterValue(SYS_STAT)
            except AttributeError:
                stat = -1

            if stat == 5:
                break
            time.sleep(0.1)

    def getTemperature(self):
        """Get the.. temperature sensor from the IMU"""
        return self.getRegisterValue(TEMP)

    def getGyroData_X(self):
        """Get the X axis gyro rotation"""
        return self.getTwoByteRegisterValue(GYR_DATA_X_LSB)

    def getGyroData_Y(self):
        """Get the Y axis gyro rotation"""
        return self.getTwoByteRegisterValue(GYR_DATA_Y_LSB)

    def getGyroData_Z(self):
        """Get the Z axis gyro rotation"""
        return self.getTwoByteRegisterValue(GYR_DATA_Z_LSB)

    def getAccData_X(self):
        """Get the X axis acceleration"""
        return self.getTwoByteRegisterValue(ACC_DATA_X_LSB)

    def getAccData_Y(self):
        """Get the Y axis acceleration"""
        return self.getTwoByteRegisterValue(ACC_DATA_Y_LSB)

    def getAccData_Z(self):
        """Get the Z axis acceleration"""
        return self.getTwoByteRegisterValue(ACC_DATA_Z_LSB)

    def getMagData_X(self):
        """Get the X axis magnetisim"""
        return self.getTwoByteRegisterValue(MAG_DATA_X_LSB)

    def getMagData_Y(self):
        """Get the Y axis magnetisim"""
        return self.getTwoByteRegisterValue(MAG_DATA_Y_LSB)

    def getMagData_Z(self):
        """Get the Z axis magnetisim"""
        return self.getTwoByteRegisterValue(MAG_DATA_Z_LSB)

    def getAllEuler(self):
        """Get all Euler values (?)"""
        values = self.getSixByteRegisterValue(EUL_H_LSB)
        return [360.0 * float(value) / 5760.0 for value in values]

    def getGravity(self):
        """Get the gravitational acceleration in all axis"""
        values = self.getSixByteRegisterValue(GRV_DATA_X_LSB)
        return [float(value) / 100 for value in values]

    def getAllLinAccel(self):
        """Get all Axis acceleration"""
        values = self.getSixByteRegisterValue(LIA_DATA_X_LSB)
        return [float(value) / 1000 for value in values]

    def setRegisterValue(self, register, value):
        """Set IMU register value"""
        self.writeMultipleBytes(2, register + (value << 8))

    def getRegisterValue(self, register):
        """Get an IMU register value"""
        self.writeByte(register)
        return self.readByte()

    def getTwoByteRegisterValue(self, register):
        """Get a 2 byte IMU register value"""
        self.writeByte(register)
        val = int(self.readMultipleBytes(2))
        bits = int(16)
        if val & 1 << bits - 1 != 0:
            val = val - (1 << bits)
        return val

    def getSixByteRegisterValue(self, register):
        """Get a 6 byte IMU register value"""
        self.writeByte(register)
        val = int(self.readMultipleBytes(6))
        bits = int(16)
        values = []
        for i in range(0, 3):
            it_val = val & 65535
            if it_val & 1 << bits - 1 != 0:
                it_val = it_val - (1 << bits)
            values.append(it_val)
            val = val >> 16
        return values