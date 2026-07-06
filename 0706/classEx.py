class Television:
    serial_number = 0
    def __init__(self, channel, volume, on):
        Television.serial_number += 1
        self.serial_number = Television.serial_number
        self.channel = channel
        self.volume = volume
        self.on = on

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel
    
    def __str__(self):
        return f"Television(serialNumber={self.serial_number}, channel={self.channel}, volume={self.volume}, on={self.on})"

tv1 = Television(1, 10, True)
tv2 = Television(5, 20, False)
tv3 = Television(7, 15, True)
