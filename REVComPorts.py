import time
from serial.tools import list_ports
import re
defaultComPort = 0
comPortCommand = ''
testFixture = False

class comPort:
    def __init__(self, sn, name):
        self.sn = sn
        self.name = name

    def getSN(self):
        return self.sn

    def getNumber(self):
        num = re.findall('\\d+', self.name)
        return num[-1]

    def getName(self):
        return self.name


##Note: serial number stuff? may be causing issues for fw update
def getPorts():
    comPorts = []
    device_list = list_ports.comports()
    for usbDevice in device_list:
        if 'SER=' in usbDevice.hwid:
            sections = usbDevice.hwid.split(' ')
            for section in sections:
                if 'SER=' in section:
                    serialNumber = section[4:]
                    deviceName = usbDevice.device
                    comPorts.append(comPort(serialNumber, deviceName))

    return comPorts


def populateSerialPorts():
    global REVPorts
    global serialPorts
    serialPorts = getPorts()
    REVPorts = []
    for port in serialPorts:
        if port.getSN().startswith('D') and len(port.getSN()) > 2:
            REVPorts.append(port)