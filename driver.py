from PyHT6022.LibUsbScope import Oscilloscope


class HantekDriver:

    def __init__(self):
        self.scope = Oscilloscope()

    def connect(self):
        self.scope.setup()
        self.scope.open_handle()

    def configure(
        self,
        sample_rate=0x04,
        gain=0x01,
        channels=2
    ):
        self.scope.set_sample_rate(sample_rate)
        self.scope.set_ch1_voltage_range(gain)
        self.scope.set_num_channels(channels)

    def capture(self, samples=0x2000):
        ch1, ch2 = self.scope.read_data(samples)
        return ch1, ch2

    def close(self):
        self.scope.close_handle()