class LEDPattern:
    def __init__(self):
        self.patt = []
        for _ in range(15):
            self.patt.append(REVBytes(4))

    def set_step(self, step_num, r, g, b, t):
        r &= 255
        g &= 255
        b &= 255
        t &= 255
        self.patt[step_num] = r << 24 | g << 16 | b << 8 | t