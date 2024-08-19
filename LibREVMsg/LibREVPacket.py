
class REVHeader:
    def __init__(self, Cmd=''):
        self.length = REVBytes(2)
        self.destination = REVBytes(1)
        self.source = REVBytes(1)
        self.msgNum = REVBytes(1)
        self.refNum = REVBytes(1)
        self.packetType = REVBytes(2)
        self.packetType = Cmd >> 8 | Cmd % 256 << 8

    def __len__(self):
        length = 0
        for classMemberName in dir(self):
            classMember = getattr(self, classMemberName)
            if isinstance(classMember, REVBytes):
                length += len(classMember)

        return length

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name].data = value
        elif isinstance(value, REVBytes):
            self.__dict__[name] = value
        else:
            exit('\n\n\n!!!Attempting to add something other than REVBytes to payload structure!!!\n\n\n')

    def __add__(self, TextToAppend):
        return self.__str__() + TextToAppend

    def __radd__(self, TextToPrepend):
        return TextToPrepend + self.__str__()

    def __str__(self):
        return self.length.getHexString() + self.destination.getHexString() + self.source.getHexString() + self.msgNum.getHexString() + self.refNum.getHexString() + self.packetType.getHexString()

class REVPayload:
    def __len__(self):
        length = 0
        for classMemberName in dir(self):
            classMember = getattr(self, classMemberName)
            if isinstance(classMember, REVBytes):
                length += len(classMember)

        return length

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name].data = value
        elif isinstance(value, REVBytes):
            self.__dict__[name] = value
        else:
            print('Value is not an instance of REVBytes: ', value)
            exit('\n\n\n!!!Attempting to add something other than REVBytes to payload structure!!!\n\n\n')

    def __add__(self, TextToAppend):
        return self.__str__() + TextToAppend

    def __radd__(self, TextToPrepend):
        return TextToPrepend + self.__str__()

    def __str__(self):
        payloadDict = {}
        payloadStr = ''
        for objectStr in dir(self):
            memberObject = getattr(self, objectStr)
            if isinstance(memberObject, REVBytes):
                payloadDict[memberObject.memberOrder] = memberObject

        for payloadKey in sorted(payloadDict):
            if payloadDict[payloadKey].data < 0:
                comp = 'FF' * len(payloadDict[payloadKey])
                comp = int('0x' + comp, 16) - abs(int(payloadDict[payloadKey])) + 1
                strComp = ''
                strComp = hex(int(comp))[2:]
                if strComp.endswith('L'):
                    strComp = strComp[:-1]
                if len(strComp) > 2:
                    swappedText = ''
                    for i in range(len(strComp), 0, -2):
                        swappedText += strComp[i - 2:i]

                    strComp = swappedText
                payloadStr += strComp
            else:
                payloadStr += payloadDict[payloadKey]

        return payloadStr

    def getOrderedMembers(self):
        payloadMembers = []
        payloadDict = {}
        for objectStr in dir(self):
            memberObject = getattr(self, objectStr)
            if isinstance(memberObject, REVBytes):
                payloadDict[memberObject.memberOrder] = memberObject

        for payloadKey in sorted(payloadDict):
            payloadMembers.append(payloadDict[payloadKey])

        return payloadMembers

class REVPacket:
    """Packet definition
    0x44 (D)
    0x4B (K)
    PacketLength
    PacketLength
    Destination Module Address
    Source Module Address
    Message Number
    Reference Number
    Packet ID
    Payload....
    Checksum"""

    FrameIndex_Start = 0
    FrameIndex_End = FrameIndex_Start + 4
    HeaderIndex_Start = FrameIndex_End
    LengthIndex_Start = FrameIndex_End
    LengthIndex_End = LengthIndex_Start + 4
    DestinationIndex_Start = LengthIndex_End
    DestinationIndex_End = DestinationIndex_Start + 2
    SourceIndex_Start = DestinationIndex_End
    SourceIndex_End = SourceIndex_Start + 2
    MsgNumIndex_Start = SourceIndex_End
    MsgNumIndex_End = MsgNumIndex_Start + 2
    RefNumIndex_Start = MsgNumIndex_End
    RefNumIndex_End = RefNumIndex_Start + 2
    PacketTypeIndex_Start = RefNumIndex_End
    PacketTypeIndex_End = PacketTypeIndex_Start + 4
    HeaderIndex_End = PacketTypeIndex_End

    def __init__(self, Header, Payload):
        self.frame = '444B'
        self.header = Header
        self.payload = Payload
        self.chkSum = '00'
        self.calcLength()

    def calcLength(self):
        self.header.length = len(self.header) + len(self.payload) + 3
        self.header.length = int(self.header.length) >> 8 | int(self.header.length) % 256 << 8

    def getPacketData(self):
        chkSummableBytes = self.frame + self.header + self.payload
        chkSum = 0
        for i in range(0, len(chkSummableBytes), 2):
            chkSum += int(chkSummableBytes[i:i + 2], 16)
            chkSum %= 256

        self.chkSum = '%02X' % chkSum
        return (self.frame + self.header + self.payload + self.chkSum).upper()

    def assignRawBytes(self, rawBytes_nibble):
        frameBytes = rawBytes_nibble[REVPacket.FrameIndex_Start:REVPacket.FrameIndex_End]
        lengthByte = rawBytes_nibble[REVPacket.LengthIndex_Start:REVPacket.LengthIndex_End]
        destinationBytes = rawBytes_nibble[REVPacket.DestinationIndex_Start:REVPacket.DestinationIndex_End]
        sourceBytes = rawBytes_nibble[REVPacket.SourceIndex_Start:REVPacket.SourceIndex_End]
        msgNumByte = rawBytes_nibble[REVPacket.MsgNumIndex_Start:REVPacket.MsgNumIndex_End]
        refNumByte = rawBytes_nibble[REVPacket.RefNumIndex_Start:REVPacket.RefNumIndex_End]
        packetBytes = rawBytes_nibble[REVPacket.HeaderIndex_End:-2]
        checkSumByte = rawBytes_nibble[-2:]
        self.header.length = lengthByte
        self.header.destination = destinationBytes
        self.header.source = sourceBytes
        self.header.msgNum = msgNumByte
        self.header.refNum = refNumByte
        self.header.packetType = packetBytes
        payloadDict = {}
        for payloadMemberName in dir(self.payload):
            payloadMember = getattr(self.payload, payloadMemberName)
            if isinstance(payloadMember, REVBytes):
                payloadDict[payloadMember.memberOrder] = {'Name': payloadMemberName, 'Length': (payloadMember.numBytes)}

        byteCounter = 0
        for payloadKey in sorted(payloadDict):
            name = payloadDict[payloadKey]['Name']
            length = payloadDict[payloadKey]['Length']
            value = packetBytes[byteCounter:byteCounter + length * 2]
            byteCounter += length * 2
            if length > 1:
                swappedText = ''
                for i in range(len(value), 0, -2):
                    swappedText += value[i - 2:i]

                value = swappedText