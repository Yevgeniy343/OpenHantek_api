from PyHT6022.LibUsbScope import Oscilloscope


class HantekDriver:

    def __init__(self):
        self.scope = Oscilloscope()
        self.connected = False

    def connect(self):
        self.scope.setup()
        self.scope.open_handle()
        self.connected = True

    def configure(
        self,
        sample_rate=0x04,
        voltage_range=0x01,
        channels=2,
    ):
        self.scope.set_sample_rate(sample_rate)
        self.scope.set_ch1_voltage_range(voltage_range)

        if channels == 1:
            self.scope.set_num_channels(1)
        else:
            self.scope.set_num_channels(2)

    def capture(self, samples=0x2000):
        return self.scope.read_data(samples)

    def close(self):
        if self.connected:
            self.scope.close_handle()
            self.connected = False