import multiprocessing as mp, time, REVComPorts, REVMessage as REVMsg
from REVModule import Module
import binascii, serial, time

#Serial Communications 
class REVcomm:
    """The serial communications for REV hubs"""
    def __init__(self, errors = False):
        self.serialReceive_Thread = False
        self.FunctionReturnTime = 0
        self.msgNum = 1
        self.rxQueue = mp.Queue(256)
        self.txQueue = mp.Queue(256)
        self.roundTripAverage = 0
        self.numMsgs = 0
        self.msgSendTime = 0
        self.msgRcvTime = 0
        self.discoveryTimeout = 0.5
        self.averageMsgTime = 0
        self.REVProcessor = serial.Serial(baudrate=460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        self.errorHandler = errors

    def listPorts(self):
        """list available ports"""
        REVComPorts.populateSerialPorts()
        return REVComPorts.REVPorts

    def openActivePort(self):
        """Open a serial port"""
        try:
            numSerialErrors = 2
            while not self.REVProcessor.isOpen():
                self.REVProcessor.port = self.listPorts()[0].getName()
                try:
                    self.REVProcessor.open()
                except serial.SerialException as e:
                    error ='Serial port error: ' + str(e) + ' retrying...'
                    print(error)
                    numSerialErrors -= 1
                    if numSerialErrors == 0:
                        self.throwError(error)
                        break
                    time.sleep(1)
        except IndexError:
            self.throwError('There are no connected hubs')

    def closeActivePort(self):
        """Close an active serial port"""
        self.REVProcessor.close()

    def sendAndReceive(self, PacketToWrite, destination):
        """Send new packets and parse response"""
        incomingPacket = ''
        packetLength = 0
        msgNum = 0
        retry = True
        try:
            retryAttempt = 0
            while retry:
                PacketToWrite.header.destination = destination
                if isinstance(PacketToWrite, REVMsg.REVPacket):
                    MaxRetries = 1
                    PacketToWrite.header.msgNum = msgNum
                    msgNum = (msgNum + 1) % 256
                    if msgNum == 0:
                        msgNum = 1
                    printData = PacketToWrite.header.packetType.data >> 8 | PacketToWrite.header.packetType.data % 256 << 8
                    discoveryMode = False
                    if printData == REVMsg.MsgNum.Discovery:
                        discoveryMode = True

                    #write the packet 
                    self.REVProcessor.write(binascii.unhexlify(PacketToWrite.getPacketData()))
                    
                    waitTimeStart = time.time()
                    timeout = False
                    while self.REVProcessor.inWaiting() == 0:
                        if time.time() - waitTimeStart > 1:
                            timeout = True
                            retryAttempt += 1
                            if retryAttempt > MaxRetries:
                                retry = False
                            break
                    if timeout:
                        raise(TimeoutError)

                    if discoveryMode:
                        packet = [] 

                    # read all incoming bytes
                    bytes = []
                    packet = ""
                    while self.REVProcessor.in_waiting() < 0:
                        newByte = str(binascii.hexlify(self.REVProcessor.read(1)).upper())[2:-1]
                        bytes.append(newByte)
                        packet += newByte
                        
                    # process the packet if theres any bytes
                    if len(bytes) != 0:
                        if bytes[0] == '44' and bytes[1] == '4B':
                            lengthbytes = bytes[2] + bytes[3]
                            packet += lengthbytes
                            packetLength = int(int(lengthbytes, 16) >> 8 | int(lengthbytes, 16) % 256 << 8)
                            if packetLength <= REVMsg.PAYLOAD_MAX_SIZE:
                                if len(packet) / 2 == packetLength:
                                    receivedChkSum = int(packet[-2:], 16)
                                    calculatedChkSum = self.checkPacket(packet, receivedChkSum)
                                    if calculatedChkSum[0]:
                                        newPacket = self.processPacket(packet)
                                        if discoveryMode:
                                            packet.append(newPacket)
                                            time.sleep(2)
                                            if self.REVProcessor.inWaiting() > 0:
                                                pass
                                            else:
                                                return packet
                                        else:
                                            return newPacket
                                    else:
                                        print('Invalid ChkSum: ',  calculatedChkSum[1], '==', calculatedChkSum[2])
                            
                else:
                    exit('\n\n\n!!!Attempting to send something other than a REVPacket!!!\n\n\n')

        except serial.SerialException:
            self.REVProcessor.close()
            return False

        return True

    def checkResponse(self, receivedPacket, PacketToWrite):
        """Check for valid response packet"""
        packetType = int(receivedPacket.header.packetType)
        data = PacketToWrite.header.packetType.data >> 8 | PacketToWrite.header.packetType.data % 256 << 8
        responseExpected = REVMsg.printDict[data]['Response']
        if packetType == responseExpected:
            if receivedPacket.header.refNum == PacketToWrite.header.msgNum:
                return True
            else:
                if packetType == REVMsg.RespNum.Discovery_RSP:
                    return True
                print('This response is for a different message. Sent: %d, Received: %d.' % (receivedPacket.header.refNum, PacketToWrite.header.msgNum))
                return False

        else:
            if packetType == REVMsg.MsgNum.NACK:
                printData = PacketToWrite.header.packetType.data >> 8 | PacketToWrite.header.packetType.data % 256 << 8
                print('NACK Code: ', receivedPacket.payload.nackCode)
                print("NACK'd Packet: ", REVMsg.printDict[printData]['Name'], '::', PacketToWrite.getPacketData())
                return False
            else:
                print('Incorrect Response Type. Response Expected: ', binascii.hexlify(str(data)), ', Response Received: ', binascii.hexlify(str(packetType)))
                return False

    def checkPacket(self, incomingPacket, receivedChkSum):
        """Check for valid checksum"""
        calcChkSum = 0
        for bytePointer in range(0, len(incomingPacket) - 2, 2):
            calcChkSum += int(incomingPacket[bytePointer:bytePointer + 2], 16)
            calcChkSum %= 256

        return (receivedChkSum == calcChkSum, receivedChkSum, calcChkSum)

    def processPacket(self, incomingPacket):
        """Parse a incoming packet"""
        packetLength = int(self.swapEndianess(incomingPacket[REVMsg.REVPacket.LengthIndex_Start:REVMsg.REVPacket.LengthIndex_End]), 16)
        packetDest = int(incomingPacket[REVMsg.REVPacket.DestinationIndex_Start:REVMsg.REVPacket.DestinationIndex_End], 16)
        packetSrc = int(incomingPacket[REVMsg.REVPacket.SourceIndex_Start:REVMsg.REVPacket.SourceIndex_End], 16)
        packetMsgNum = int(incomingPacket[REVMsg.REVPacket.MsgNumIndex_Start:REVMsg.REVPacket.MsgNumIndex_End], 16)
        packetRefNum = int(incomingPacket[REVMsg.REVPacket.RefNumIndex_Start:REVMsg.REVPacket.RefNumIndex_End], 16)
        packetCommandNum = int(self.swapEndianess(incomingPacket[REVMsg.REVPacket.PacketTypeIndex_Start:REVMsg.REVPacket.PacketTypeIndex_End]), 16)
        packetPayload = incomingPacket[REVMsg.REVPacket.HeaderIndex_End:-2]
        newPacket = REVMsg.printDict[packetCommandNum]['Packet']()
        newPacket.assignRawBytes(incomingPacket)
        newPacket.header.length = packetLength
        newPacket.header.destination = packetDest
        newPacket.header.source = packetSrc
        newPacket.header.msgNum = packetMsgNum
        newPacket.header.refNum = packetRefNum
        newPacket.header.packetType = packetCommandNum
        bytePointer = 0
        for payloadMember in newPacket.payload.getOrderedMembers():
            valueToAdd = REVMsg.REVBytes(len(payloadMember))
            valueToAdd.data = int(self.swapEndianess(packetPayload[bytePointer:bytePointer + len(payloadMember) * 2]), 16)
            newPacket.payload.payloadMember = valueToAdd
            bytePointer = bytePointer + len(payloadMember) * 2
        return newPacket

    def swapEndianess(self, bytes):
        """Swap bytes for packets"""
        swappedBytes = ''
        for bytePointer in range(0, len(bytes), 2):
            thisByte = bytes[bytePointer:bytePointer + 2]
            swappedBytes = thisByte + swappedBytes
        return swappedBytes

    def getModuleStatus(self, destination):
        """Get the status for a Lynx module"""
        getModuleStatusMsg = REVMsg.GetModuleStatus()
        getModuleStatusMsg.payload.clearStatus = 1
        packet = self.sendAndReceive(getModuleStatusMsg, destination)
        return packet.payload.motorAlerts

    def keepAlive(self, destination):
        """Send keep alive packet"""
        keepAliveMsg = REVMsg.KeepAlive()
        return self.sendAndReceive(keepAliveMsg, destination)

    def failSafe(self, destination):
        """Failsafe"""
        failSafeMsg = REVMsg.FailSafe()
        self.sendAndReceive(failSafeMsg, destination)

    def setNewModuleAddress(self, destination, moduleAddress):
        """Set a new lynx module address """
        setNewModuleAddressMsg = REVMsg.SetNewModuleAddress()
        setNewModuleAddressMsg.payload.moduleAddress = moduleAddress
        self.sendAndReceive(setNewModuleAddressMsg, destination)

    def queryInterface(self, destination, interfaceName):
        """Query interface"""
        queryInterfaceMsg = REVMsg.QueryInterface()
        queryInterfaceMsg.payload.interfaceName = interfaceName
        packet = self.sendAndReceive(queryInterfaceMsg, destination)
        return (
         packet.payload.packetID, packet.numValues)

    def setModuleLEDColor(self, destination, redPower, greenPower, bluePower):
        """Set the color of the LED on a lynx modle from RGB"""
        setModuleLEDColorMsg = REVMsg.SetModuleLEDColor()
        setModuleLEDColorMsg.payload.redPower = redPower
        setModuleLEDColorMsg.payload.greenPower = greenPower
        setModuleLEDColorMsg.payload.bluePower = bluePower
        self.sendAndReceive(setModuleLEDColorMsg, destination)

    def getModuleLEDColor(self, destination):
        """Read the set RGB of lynx module LED"""
        getModuleLEDColorMsg = REVMsg.GetModuleLEDColor()
        packet = self.sendAndReceive(getModuleLEDColorMsg, destination)
        return (
         packet.payload.redPower, packet.payload.greenPower, packet.payload.bluePower)

    def setModuleLEDPattern(self, destination, stepArray):
        """Set a patern for lynx LED"""
        setModuleLEDPatternMsg = REVMsg.SetModuleLEDPattern()
        for i, step in enumerate(stepArray.patt):
            setattr(setModuleLEDPatternMsg.payload, ('rgbtStep{}').format(i), step)  
        self.sendAndReceive(setModuleLEDPatternMsg, destination)

    def getModuleLEDPattern(self, destination):
        """Read module LED patern"""
        getModuleLEDPatternMsg = REVMsg.GetModuleLEDPattern()
        packet = self.sendAndReceive(getModuleLEDPatternMsg, destination)
        return packet

    def debugLogLevel(self, destination, groupNumber, verbosityLevel):
        """Debug log level"""
        debugLogLevelMsg = REVMsg.DebugLogLevel()
        debugLogLevelMsg.payload.groupNumber = groupNumber
        debugLogLevelMsg.payload.verbosityLevel = verbosityLevel
        self.sendAndReceive(debugLogLevelMsg, destination)

    def discovery(self):
        """Discover Connected lynx modules"""
        self.discovered = REVMsg.Discovery()
        packets = self.sendAndReceive(self.discovered, 255)
        REVModules = []
        for packet in packets:
            module = Module(self, packet.header.source, packet.payload.parent, self)
            module.init_periphs()
            REVModules.append(module)
        return REVModules

    def getBulkInputData(self, destination):
        """Get bulk data; Analgous to the FTC SDK Bulkread"""
        getBulkInputDataMsg = REVMsg.GetBulkInputData()
        packet = self.sendAndReceive(getBulkInputDataMsg, destination)
        return packet

    def phoneChargeControl(self, destination, enable):
        """seems to be able to charge connected android phone somehow? not sure how this even works"""
        phoneChargeControlMsg = REVMsg.PhoneChargeControl()
        phoneChargeControlMsg.payload.enable = enable
        self.sendAndReceive(phoneChargeControlMsg, destination)

    def phoneChargeQuery(self, destination):
        """See if connected android phone is being charged"""
        phoneChargeQueryMsg = REVMsg.PhoneChargeQuery()
        packet = self.sendAndReceive(phoneChargeQueryMsg, destination)
        return packet.payload.enable

    def injectDataLogHint(self, destination, length, hintText):
        """Inject Data log hint text"""
        injectDataLogHintMsg = REVMsg.InjectDataLogHint()
        injectDataLogHintMsg.payload.length = length
        injectDataLogHintMsg.payload.hintText = hintText
        self.sendAndReceive(injectDataLogHintMsg, destination)

    def readVersionString(self, destination):
        """used to read the firmware version"""
        readVersionStringMsg = REVMsg.ReadVersionString()
        packet = self.sendAndReceive(readVersionStringMsg, destination)
        return packet.payload.versionString
    
    def throwError(self, error): 
        """This is a generic error handler api that allows objects farhter down the stack to send errors to an error handler"""
        if self.errorHandler != False:
            self.errorHandler.throwError(error)
        else:
            print(error)