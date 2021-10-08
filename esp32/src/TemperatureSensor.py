import machine, onewire, ds18x20, time

class TemperatureSensor:
    def __init__(self, pin_id, offset):
        ds_pin = machine.Pin(pin_id)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        self.roms = self.ds_sensor.scan()
        self.offset = offset
        print('Found DS devices: ', self.roms)        

    def read(self):
        self.ds_sensor.convert_temp()
        time.sleep_ms(750)
        return [(self.ds_sensor.read_temp(rom) + self.offset) for rom in self.roms]
