from PyHT6022.LibUsbScope import Oscilloscope


class HantekDriver:
    def __init__(self):
        self.scope = Oscilloscope()
        self.connected = False

    def connect(self):
        print("Setup...")
        self.scope.setup()

        print("Open handle...")
        self.scope.open_handle()

        self.connected = True
        print("Connected")

    def configure(
        self,
        sample_rate_index=0x04,
        voltage_range=0x01,
        channels=2,
    ):
        if not self.connected:
            raise RuntimeError("Scope is not connected")

        print("Configure...")

        self.scope.set_sample_rate(sample_rate_index)
        self.scope.set_ch1_voltage_range(voltage_range)

        if channels == 2:
            self.scope.set_num_channels(2)
        else:
            self.scope.set_num_channels(1)

        print("Configured")

    def capture(self, data_points=0x2000):
        if not self.connected:
            raise RuntimeError("Scope is not connected")

        print("Capture...")
        ch1, ch2 = self.scope.read_data(data_points)

        return ch1, ch2

    def close(self):
        if self.connected:
            print("Close handle...")
            self.scope.close_handle()
            self.connected = False
            print("Closed")