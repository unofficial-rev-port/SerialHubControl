
class REVBytes:
    creationCounter = 0

    def __init__(self, NumBytes):
        self.numBytes = NumBytes
        self.data = 0
        self.memberOrder = REVBytes.creationCounter
        REVBytes.creationCounter += 1

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return self.numBytes

    def __setattr__(self, name, value):
        if isinstance(value, str):
            try:
                value = int(value, 16)
            except ValueError:
                value = int(ord(value), 16)

        if isinstance(value, REVBytes):
            value = value.data
        self.__dict__[name] = value

    def __lt__(self, other):
        if self.data < other:
            return True
        return False

    def __le__(self, other):
        if self.data <= other:
            return True
        return False

    def __eq__(self, other):
        if self.data == other:
            return True
        return False

    def __ne__(self, other):
        if self.data != other:
            return True
        return False

    def __ge__(self, other):
        if self.data >= other:
            return True
        return False

    def __gt__(self, other):
        if self.data > other:
            return True
        return False

    def __sub__(self, other):
        return self.data - other

    def __rsub__(self, other):
        return other - self.data

    def __add__(self, other):
        return self.data + other

    def __float__(self):
        return float(self.data)

    def __int__(self):
        return int(self.data)

    def __add__(self, other):
        if isinstance(other, str):
            myBytes = self.getHexString()
            if len(myBytes) > 2:
                swappedText = ''
                for i in range(len(myBytes), 0, -2):
                    swappedText += myBytes[i - 2:i]

                myBytes = swappedText
            return myBytes + other
        else:
            return self.data + other

    def __radd__(self, other):
        if isinstance(other, str):
            myBytes = self.getHexString()
            if len(myBytes) > 2:
                swappedText = ''
                for i in range(len(myBytes), 0, -2):
                    swappedText += myBytes[i - 2:i]

                myBytes = swappedText
            return other + myBytes
        else:
            return other + self.data
        
    def getHexString(self):
        hexString = '%0' + str(self.numBytes * 2) + 'X'
        hexString = hexString % int(self.data) 
        return hexString