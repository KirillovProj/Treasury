
"""
A Command object, that implements the ISwitch interface and runs the
command on the designated receiver
"""
from interface import ISwitch

class SwitchOnCommand(ISwitch):
    "Switch On Command"

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


class SwitchOffCommand(ISwitch):
    "Switch Off Command"

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()
