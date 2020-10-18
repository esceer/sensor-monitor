class LightSensor:
    def __init__(self, name):
        from python_tsl2591 import tsl2591
        self._tsl = tsl2591()
        self._name = name

    @property
    def name(self):
        return self._name

    def get_full_spectrum_light(self):
        full, ir = self._tsl.get_full_luminosity()
        return full

    def get_human_visible_light(self):
        full, ir = self._tsl.get_full_luminosity()
        return self._tsl.calculate_lux(full, ir)

    def get_infrared_light(self):
        full, ir = self._tsl.get_full_luminosity()
        return ir

    def get_value(self):
        return self.get_human_visible_light()
