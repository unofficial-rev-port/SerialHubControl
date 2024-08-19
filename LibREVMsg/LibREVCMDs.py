import LibREVBytes
import LibREVPacket
class ACK_Payload(REVPayload):
    def __init__(self):
        self.attnReq = REVBytes(1)

class NACK_Payload(REVPayload):
    def __init__(self):
        self.nackCode = REVBytes(1)

class GetModuleStatus_Payload(REVPayload):
    def __init__(self):
        self.clearStatus = REVBytes(1)

class KeepAlive_Payload(REVPayload):
    def __init__(self):
        pass

class FailSafe_Payload(REVPayload):
    def __init__(self):
        pass

class SetNewModuleAddress_Payload(REVPayload):
    def __init__(self):
        self.moduleAddress = REVBytes(1)

class QueryInterface_Payload(REVPayload):
    def __init__(self):
        self.interfaceName = REVBytes(PAYLOAD_MAX_SIZE - 7)

class StartProgramDownload_Payload(REVPayload):
    def __init__(self):
        pass

class ProgramDownloadChunk_Payload(REVPayload):
    def __init__(self):
        pass

class SetModuleLEDColor_Payload(REVPayload):
    def __init__(self):
        self.redPower = REVBytes(1)
        self.greenPower = REVBytes(1)
        self.bluePower = REVBytes(1)

class GetModuleLEDColor_Payload(REVPayload):
    def __init__(self):
        pass

class SetModuleLEDPattern_Payload(REVPayload):
    def __init__(self):
        self.rgbtStep0 = REVBytes(4)
        self.rgbtStep1 = REVBytes(4)
        self.rgbtStep2 = REVBytes(4)
        self.rgbtStep3 = REVBytes(4)
        self.rgbtStep4 = REVBytes(4)
        self.rgbtStep5 = REVBytes(4)
        self.rgbtStep6 = REVBytes(4)
        self.rgbtStep7 = REVBytes(4)
        self.rgbtStep8 = REVBytes(4)
        self.rgbtStep9 = REVBytes(4)
        self.rgbtStep10 = REVBytes(4)
        self.rgbtStep11 = REVBytes(4)
        self.rgbtStep12 = REVBytes(4)
        self.rgbtStep13 = REVBytes(4)
        self.rgbtStep14 = REVBytes(4)
        self.rgbtStep15 = REVBytes(4)

class GetModuleLEDPattern_Payload(REVPayload):
    def __init__(self):
        pass

class DebugLogLevel_Payload(REVPayload):
    def __init__(self):
        self.groupNumber = REVBytes(1)
        self.verbosityLevel = REVBytes(1)

class Discovery_Payload(REVPayload):
    def __init__(self):
        pass

class GetBulkInputData_Payload(REVPayload):
    def __init__(self):
        pass

class SetSingleDIOOutput_Payload(REVPayload):
    def __init__(self):
        self.dioPin = REVBytes(1)
        self.value = REVBytes(1)

class SetAllDIOOutputs_Payload(REVPayload):

    def __init__(self):
        self.values = REVBytes(1)

class SetDIODirection_Payload(REVPayload):
    def __init__(self):
        self.dioPin = REVBytes(1)
        self.directionOutput = REVBytes(1)

class GetDIODirection_Payload(REVPayload):
    def __init__(self):
        self.dioPin = REVBytes(1)

class GetSingleDIOInput_Payload(REVPayload):
    def __init__(self):
        self.dioPin = REVBytes(1)

class GetAllDIOInputs_Payload(REVPayload):
    def __init__(self):
        pass

class GetADC_Payload(REVPayload):
    def __init__(self):
        self.adcChannel = REVBytes(1)
        self.rawMode = REVBytes(1)

class SetMotorChannelMode_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.motorMode = REVBytes(1)
        self.floatAtZero = REVBytes(1)

class GetMotorChannelMode_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorChannelEnable_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.enabled = REVBytes(1)

class GetMotorChannelEnable_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorChannelCurrentAlertLevel_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.currentLimit = REVBytes(2)

class GetMotorChannelCurrentAlertLevel_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class ResetMotorEncoder_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorConstantPower_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.powerLevel = REVBytes(2)

class GetMotorConstantPower_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorTargetVelocity_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.velocity = REVBytes(2)

class GetMotorTargetVelocity_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorTargetPosition_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.position = REVBytes(4)
        self.atTargetTolerance = REVBytes(2)

class GetMotorTargetPosition_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class GetMotorAtTarget_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class GetMotorEncoderPosition_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)

class SetMotorPIDCoefficients_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.mode = REVBytes(1)
        self.p = REVBytes(4)
        self.i = REVBytes(4)
        self.d = REVBytes(4)

class GetMotorPIDCoefficients_Payload(REVPayload):
    def __init__(self):
        self.motorChannel = REVBytes(1)
        self.mode = REVBytes(1)

class SetPWMConfiguration_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)
        self.framePeriod = REVBytes(2)

class GetPWMConfiguration_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)

class SetPWMPulseWidth_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)
        self.pulseWidth = REVBytes(2)

class GetPWNPulseWidth_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)

class SetPWMEnable_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)
        self.enable = REVBytes(1)

class GetPWMEnable_Payload(REVPayload):
    def __init__(self):
        self.pwmChannel = REVBytes(1)

class SetServoConfiguration_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)
        self.framePeriod = REVBytes(2)

class GetServoConfiguration_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)

class SetServoPulseWidth_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)
        self.pulseWidth = REVBytes(2)

class GetServoPulseWidth_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)

class SetServoEnable_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)
        self.enable = REVBytes(1)

class GetServoEnable_Payload(REVPayload):
    def __init__(self):
        self.servoChannel = REVBytes(1)

class I2CWriteSingleByte_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)
        self.slaveAddress = REVBytes(1)
        self.byteToWrite = REVBytes(1)

class I2CWriteMultipleBytes_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)
        self.slaveAddress = REVBytes(1)
        self.numBytes = REVBytes(1)
        self.bytesToWrite = REVBytes(PAYLOAD_MAX_SIZE - 7)

class I2CWriteStatusQuery_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)

class I2CReadSingleByte_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)
        self.slaveAddress = REVBytes(1)

class I2CReadMultipleBytes_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)
        self.slaveAddress = REVBytes(1)
        self.numBytes = REVBytes(1)

class I2CReadStatusQuery_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)

class I2CConfigureChannel_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)
        self.speedCode = REVBytes(1)

class PhoneChargeControl_Payload(REVPayload):
    def __init__(self):
        self.enable = REVBytes(1)

class PhoneChargeQuery_Payload(REVPayload):
    def __init__(self):
        pass

class InjectDataLogHint_Payload(REVPayload):
    def __init__(self):
        self.length = REVBytes(1)
        self.hintText = REVBytes(PAYLOAD_MAX_SIZE - 7)

class I2CConfigureQuery_Payload(REVPayload):
    def __init__(self):
        self.i2cChannel = REVBytes(1)

class ReadVersionString_Payload(REVPayload):
    def __init__(self):
        pass

class I2CBlockReadConfig_Payload(REVPayload):
    def __init__(self):
        self.channel = REVBytes(1)
        self.address = REVBytes(1)
        self.startRegister = REVBytes(1)
        self.numberOfBytes = REVBytes(1)
        self.readInterval_ms = REVBytes(1)

class I2CBlockReadQuery_Payload(REVPayload):
    def __init__(self):
        self.channel = REVBytes(1)

class I2CWriteReadMultipleBytes_Payload(REVPayload):
    def __init__(self):
        self.channel = REVBytes(1)
        self.address = REVBytes(1)
        self.startRegister = REVBytes(1)
        self.numberOfBytes = REVBytes(1)

class IMUBlockReadConfig_Payload(REVPayload):
    def __init__(self):
        self.startRegister = REVBytes(1)
        self.numberOfBytes = REVBytes(1)
        self.readInterval_ms = REVBytes(1)

class IMUBlockReadQuery_Payload(REVPayload):
    def __init__(self):
        self.channel = REVBytes(1)

class GetModuleStatus_RSP_Payload(REVPayload):
    def __init__(self):
        self.statusWord = REVBytes(1)
        self.motorAlerts = REVBytes(1)

class QueryInterface_RSP_Payload(REVPayload):
    def __init__(self):
        self.packetID = REVBytes(2)
        self.numValues = REVBytes(2)

class GetModuleLEDColor_RSP_Payload(REVPayload):
    def __init__(self):
        self.redPower = REVBytes(1)
        self.greenPower = REVBytes(1)
        self.bluePower = REVBytes(1)

class GetModuleLEDPattern_RSP_Payload(REVPayload):
    def __init__(self):
        self.rgbtStep0 = REVBytes(4)
        self.rgbtStep1 = REVBytes(4)
        self.rgbtStep2 = REVBytes(4)
        self.rgbtStep3 = REVBytes(4)
        self.rgbtStep4 = REVBytes(4)
        self.rgbtStep5 = REVBytes(4)
        self.rgbtStep6 = REVBytes(4)
        self.rgbtStep7 = REVBytes(4)
        self.rgbtStep8 = REVBytes(4)
        self.rgbtStep9 = REVBytes(4)
        self.rgbtStep10 = REVBytes(4)
        self.rgbtStep11 = REVBytes(4)
        self.rgbtStep12 = REVBytes(4)
        self.rgbtStep13 = REVBytes(4)
        self.rgbtStep14 = REVBytes(4)
        self.rgbtStep15 = REVBytes(4)

class Discovery_RSP_Payload(REVPayload):
    def __init__(self):
        self.parent = REVBytes(1)

class TunnelReadDebugPort_RSP_Payload(REVPayload):
    def __init__(self):
        self.numBytes = REVBytes(1)
        self.bytesRead = REVBytes(PAYLOAD_MAX_SIZE - 7)

class GetBulkInputData_RSP_Payload(REVPayload):
    def __init__(self):
        self.digitalInputs = REVBytes(1)
        self.motor0Encoder = REVBytes(4)
        self.motor1Encoder = REVBytes(4)
        self.motor2Encoder = REVBytes(4)
        self.motor3Encoder = REVBytes(4)
        self.motorStatus = REVBytes(1)
        self.motor0Velocity = REVBytes(2)
        self.motor1Velocity = REVBytes(2)
        self.motor2Velocity = REVBytes(2)
        self.motor3Velocity = REVBytes(2)
        self.motor0mode = REVBytes(1)
        self.motor1mode = REVBytes(1)
        self.motor2mode = REVBytes(1)
        self.motor3mode = REVBytes(1)
        self.analogInput0 = REVBytes(2)
        self.analogInput1 = REVBytes(2)
        self.analogInput2 = REVBytes(2)
        self.analogInput3 = REVBytes(2)
        self.gpioCurrent_mA = REVBytes(2)
        self.i2cCurrent_mA = REVBytes(2)
        self.servoCurrent_mA = REVBytes(2)
        self.batteryCurrent_mA = REVBytes(2)
        self.motor0current_mA = REVBytes(2)
        self.motor1current_mA = REVBytes(2)
        self.motor2current_mA = REVBytes(2)
        self.motor3current_mA = REVBytes(2)
        self.mon5v_mV = REVBytes(2)
        self.batteryVoltage_mV = REVBytes(2)
        self.servo0cmd = REVBytes(2)
        self.servo1cmd = REVBytes(2)
        self.servo2cmd = REVBytes(2)
        self.servo3cmd = REVBytes(2)
        self.servo4cmd = REVBytes(2)
        self.servo5cmd = REVBytes(2)
        self.servo0framePeriod_us = REVBytes(2)
        self.servo1framePeriod_us = REVBytes(2)
        self.servo2framePeriod_us = REVBytes(2)
        self.servo3framePeriod_us = REVBytes(2)
        self.servo4framePeriod_us = REVBytes(2)
        self.servo5framePeriod_us = REVBytes(2)
        self.i2c0data = REVBytes(10)
        self.i2c1data = REVBytes(10)
        self.i2c2data = REVBytes(10)
        self.i2c3data = REVBytes(10)
        self.imuBlock = REVBytes(10)
        self.i2c0Status = REVBytes(1)
        self.i2c1Status = REVBytes(1)
        self.i2c2Status = REVBytes(1)
        self.i2c3Status = REVBytes(1)
        self.imuStatus = REVBytes(1)
        self.mototonicTime = REVBytes(4)

class GetDIODirection_RSP_Payload(REVPayload):
    def __init__(self):
        self.directionOutput = REVBytes(1)

class GetSingleDIOInput_RSP_Payload(REVPayload):
    def __init__(self):
        self.inputValue = REVBytes(1)

class GetAllDIOInputs_RSP_Payload(REVPayload):
    def __init__(self):
        self.inputValues = REVBytes(1)

class GetADC_RSP_Payload(REVPayload):
    def __init__(self):
        self.adcValue = REVBytes(2)

class GetMotorChannelMode_RSP_Payload(REVPayload):
    def __init__(self):
        self.motorChannelMode = REVBytes(1)
        self.floatAtZero = REVBytes(1)

class GetMotorChannelEnable_RSP_Payload(REVPayload):
    def __init__(self):
        self.enabled = REVBytes(1)

class GetMotorChannelCurrentAlertLevel_RSP_Payload(REVPayload):
    def __init__(self):
        self.currentLimit = REVBytes(2)

class GetMotorConstantPower_RSP_Payload(REVPayload):
    def __init__(self):
        self.powerLevel = REVBytes(2)

class GetMotorTargetVelocity_RSP_Payload(REVPayload):
    def __init__(self):
        self.velocity = REVBytes(2)

class GetMotorTargetPosition_RSP_Payload(REVPayload):
    def __init__(self):
        self.targetPosition = REVBytes(4)
        self.atTargetTolerance = REVBytes(2)

class GetMotorAtTarget_RSP_Payload(REVPayload):
    def __init__(self):
        self.atTarget = REVBytes(1)


class GetMotorEncoderPosition_RSP_Payload(REVPayload):
    def __init__(self):
        self.currentPosition = REVBytes(4)

class GetMotorPIDCoefficients_RSP_Payload(REVPayload):
    def __init__(self):
        self.p = REVBytes(4)
        self.i = REVBytes(4)
        self.d = REVBytes(4)

class GetPWMConfiguration_RSP_Payload(REVPayload):
    def __init__(self):
        self.framePeriod = REVBytes(2)

class GetPWNPulseWidth_RSP_Payload(REVPayload):
    def __init__(self):
        self.pulseWidth = REVBytes(1)

class GetPWMEnable_RSP_Payload(REVPayload):
    def __init__(self):
        self.enabled = REVBytes(1)

class GetServoConfiguration_RSP_Payload(REVPayload):
    def __init__(self):
        self.framePeriod = REVBytes(2)

class GetServoPulseWidth_RSP_Payload(REVPayload):
    def __init__(self):
        self.pulseWidth = REVBytes(2)

class GetServoEnable_RSP_Payload(REVPayload):
    def __init__(self):
        self.enabled = REVBytes(1)

class I2CWriteStatusQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.i2cStatus = REVBytes(1)
        self.numBytes = REVBytes(1)

class I2CReadStatusQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.i2cStatus = REVBytes(1)
        self.byteRead = REVBytes(1)
        self.payloadBytes = REVBytes(PAYLOAD_MAX_SIZE - 7)

class PhoneChargeQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.enable = REVBytes(1)

class I2CConfigureQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.speedCode = REVBytes(1)

class ReadVersionString_RSP_Payload(REVPayload):
    def __init__(self):
        self.length = REVBytes(1)
        self.versionString = REVBytes(40)

class I2CBlockReadQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.address = REVBytes(1)
        self.startRegister = REVBytes(1)
        self.numberOfBytes = REVBytes(1)
        self.readInterval_ms = REVBytes(1)

class IMUBlockReadQuery_RSP_Payload(REVPayload):
    def __init__(self):
        self.startRegister = REVBytes(1)
        self.numberOfBytes = REVBytes(1)
        self.readInterval_ms = REVBytes(1)

class ACK(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.ACK), ACK_Payload())

class NACK(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.NACK), NACK_Payload())

class GetModuleStatus(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetModuleStatus), GetModuleStatus_Payload())

class KeepAlive(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.KeepAlive), KeepAlive_Payload())

class FailSafe(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.FailSafe), FailSafe_Payload())

class SetNewModuleAddress(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetNewModuleAddress), SetNewModuleAddress_Payload())

class QueryInterface(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.QueryInterface), QueryInterface_Payload())

class StartProgramDownload(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.StartProgramDownload), StartProgramDownload_Payload())


class ProgramDownloadChunk(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.ProgramDownloadChunk), ProgramDownloadChunk_Payload())

class SetModuleLEDColor(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetModuleLEDColor), SetModuleLEDColor_Payload())

class GetModuleLEDColor(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetModuleLEDColor), GetModuleLEDColor_Payload())

class SetModuleLEDPattern(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetModuleLEDPattern), SetModuleLEDPattern_Payload())

class GetModuleLEDPattern(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetModuleLEDPattern), GetModuleLEDPattern_Payload())

class DebugLogLevel(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.DebugLogLevel), DebugLogLevel_Payload())

class Discovery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.Discovery), Discovery_Payload())

class GetBulkInputData(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetBulkInputData), GetBulkInputData_Payload())

class SetSingleDIOOutput(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetSingleDIOOutput), SetSingleDIOOutput_Payload())

class SetAllDIOOutputs(REVPacket):

    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetAllDIOOutputs), SetAllDIOOutputs_Payload())

class SetDIODirection(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetDIODirection), SetDIODirection_Payload())

class GetDIODirection(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetDIODirection), GetDIODirection_Payload())

class GetSingleDIOInput(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetSingleDIOInput), GetSingleDIOInput_Payload())

class GetAllDIOInputs(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetAllDIOInputs), GetAllDIOInputs_Payload())

class GetADC(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetADC), GetADC_Payload())

class SetMotorChannelMode(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorChannelMode), SetMotorChannelMode_Payload())

class GetMotorChannelMode(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorChannelMode), GetMotorChannelMode_Payload())

class SetMotorChannelEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorChannelEnable), SetMotorChannelEnable_Payload())

class GetMotorChannelEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorChannelEnable), GetMotorChannelEnable_Payload())

class SetMotorChannelCurrentAlertLevel(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorChannelCurrentAlertLevel), SetMotorChannelCurrentAlertLevel_Payload())

class GetMotorChannelCurrentAlertLevel(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorChannelCurrentAlertLevel), GetMotorChannelCurrentAlertLevel_Payload())

class ResetMotorEncoder(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.ResetMotorEncoder), ResetMotorEncoder_Payload())

class SetMotorConstantPower(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorConstantPower), SetMotorConstantPower_Payload())

class GetMotorConstantPower(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorConstantPower), GetMotorConstantPower_Payload())

class SetMotorTargetVelocity(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorTargetVelocity), SetMotorTargetVelocity_Payload())

class GetMotorTargetVelocity(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorTargetVelocity), GetMotorTargetVelocity_Payload())

class SetMotorTargetPosition(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorTargetPosition), SetMotorTargetPosition_Payload())

class GetMotorTargetPosition(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorTargetPosition), GetMotorTargetPosition_Payload())

class GetMotorAtTarget(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorAtTarget), GetMotorAtTarget_Payload())

class GetMotorEncoderPosition(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorEncoderPosition), GetMotorEncoderPosition_Payload())

class SetMotorPIDCoefficients(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetMotorPIDCoefficients), SetMotorPIDCoefficients_Payload())

class GetMotorPIDCoefficients(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetMotorPIDCoefficients), GetMotorPIDCoefficients_Payload())

class SetPWMConfiguration(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetPWMConfiguration), SetPWMConfiguration_Payload())

class GetPWMConfiguration(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetPWMConfiguration), GetPWMConfiguration_Payload())

class SetPWMPulseWidth(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetPWMPulseWidth), SetPWMPulseWidth_Payload())

class GetPWNPulseWidth(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetPWNPulseWidth), GetPWNPulseWidth_Payload())


class SetPWMEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetPWMEnable), SetPWMEnable_Payload())

class GetPWMEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetPWMEnable), GetPWMEnable_Payload())

class SetServoConfiguration(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetServoConfiguration), SetServoConfiguration_Payload())


class GetServoConfiguration(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetServoConfiguration), GetServoConfiguration_Payload())

class SetServoPulseWidth(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetServoPulseWidth), SetServoPulseWidth_Payload())

class GetServoPulseWidth(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetServoPulseWidth), GetServoPulseWidth_Payload())

class SetServoEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.SetServoEnable), SetServoEnable_Payload())

class GetServoEnable(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.GetServoEnable), GetServoEnable_Payload())

class I2CWriteSingleByte(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CWriteSingleByte), I2CWriteSingleByte_Payload())

class I2CWriteMultipleBytes(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CWriteMultipleBytes), I2CWriteMultipleBytes_Payload())

class I2CReadSingleByte(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CReadSingleByte), I2CReadSingleByte_Payload())

class I2CReadMultipleBytes(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CReadMultipleBytes), I2CReadMultipleBytes_Payload())

class I2CReadStatusQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CReadStatusQuery), I2CReadStatusQuery_Payload())

class I2CWriteStatusQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CWriteStatusQuery), I2CWriteStatusQuery_Payload())

class I2CConfigureChannel(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CConfigureChannel), I2CConfigureChannel_Payload())

class PhoneChargeControl(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.PhoneChargeControl), PhoneChargeControl_Payload())

class PhoneChargeQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.PhoneChargeQuery), PhoneChargeQuery_Payload())

class InjectDataLogHint(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.InjectDataLogHint), InjectDataLogHint_Payload())

class I2CConfigureQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CConfigureQuery), I2CConfigureQuery_Payload())

class ReadVersionString(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.ReadVersionString), ReadVersionString_Payload())

class I2CBlockReadConfig(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CBlockReadConfig), I2CBlockReadConfig_Payload())

class I2CBlockReadQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CBlockReadQuery), I2CBlockReadQuery_Payload())

class I2CWriteReadMultipleBytes(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.I2CWriteReadMultipleBytes), I2CWriteReadMultipleBytes_Payload())

class IMUBlockReadConfig(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.IMUBlockReadConfig), IMUBlockReadConfig_Payload())

class IMUBlockReadQuery(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=MsgNum.IMUBlockReadQuery), IMUBlockReadQuery_Payload())

class GetModuleStatus_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetModuleStatus_RSP), GetModuleStatus_RSP_Payload())

class QueryInterface_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.QueryInterface_RSP), QueryInterface_RSP_Payload())

class GetModuleLEDColor_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetModuleLEDColor_RSP), GetModuleLEDColor_RSP_Payload())

class GetModuleLEDPattern_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetModuleLEDPattern_RSP), GetModuleLEDPattern_RSP_Payload())

class Discovery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.Discovery_RSP), Discovery_RSP_Payload())

class GetBulkInputData_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetBulkInputData_RSP), GetBulkInputData_RSP_Payload())

class GetDIODirection_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetDIODirection_RSP), GetDIODirection_RSP_Payload())

class GetSingleDIOInput_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetSingleDIOInput_RSP), GetSingleDIOInput_RSP_Payload())

class GetAllDIOInputs_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetAllDIOInputs_RSP), GetAllDIOInputs_RSP_Payload())

class GetADC_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetADC_RSP), GetADC_RSP_Payload())

class GetMotorChannelMode_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorChannelMode_RSP), GetMotorChannelMode_RSP_Payload())

class GetMotorChannelEnable_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorChannelEnable_RSP), GetMotorChannelEnable_RSP_Payload())

class GetMotorChannelCurrentAlertLevel_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorChannelCurrentAlertLevel_RSP), GetMotorChannelCurrentAlertLevel_RSP_Payload())

class GetMotorConstantPower_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorConstantPower_RSP), GetMotorConstantPower_RSP_Payload())

class GetMotorTargetVelocity_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorTargetVelocity_RSP), GetMotorTargetVelocity_RSP_Payload())

class GetMotorTargetPosition_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorTargetPosition_RSP), GetMotorTargetPosition_RSP_Payload())

class GetMotorAtTarget_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorAtTarget_RSP), GetMotorAtTarget_RSP_Payload())

class GetMotorEncoderPosition_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorEncoderPosition_RSP), GetMotorEncoderPosition_RSP_Payload())

class GetMotorPIDCoefficients_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetMotorPIDCoefficients_RSP), GetMotorPIDCoefficients_RSP_Payload())

class GetPWMConfiguration_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetPWMConfiguration_RSP), GetPWMConfiguration_RSP_Payload())

class GetPWNPulseWidth_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetPWNPulseWidth_RSP), GetPWNPulseWidth_RSP_Payload())

class GetPWMEnable_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetPWMEnable_RSP), GetPWMEnable_RSP_Payload())

class GetServoConfiguration_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetServoConfiguration_RSP), GetServoConfiguration_RSP_Payload())

class GetServoPulseWidth_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetServoPulseWidth_RSP), GetServoPulseWidth_RSP_Payload())

class GetServoEnable_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.GetServoEnable_RSP), GetServoEnable_RSP_Payload())

class I2CWriteStatusQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.I2CWriteStatusQuery_RSP), I2CWriteStatusQuery_RSP_Payload())

class I2CReadStatusQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.I2CReadStatusQuery_RSP), I2CReadStatusQuery_RSP_Payload())

class PhoneChargeQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.PhoneChargeQuery_RSP), PhoneChargeQuery_RSP_Payload())

class I2CConfigureQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.I2CConfigureQuery_RSP), I2CConfigureQuery_RSP_Payload())

class ReadVersionString_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.ReadVersionString_RSP), ReadVersionString_RSP_Payload())

class I2CBlockReadQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.I2CBlockReadQuery_RSP), I2CBlockReadQuery_RSP_Payload())

class IMUBlockReadQuery_RSP(REVPacket):
    def __init__(self):
        REVPacket.__init__(self, REVHeader(Cmd=RespNum.IMUBlockReadQuery_RSP), IMUBlockReadQuery_RSP_Payload())
