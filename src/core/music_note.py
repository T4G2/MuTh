from .consts import *

class MusicNote:
    def __init__(self, interpreter: "BaseInterpreter", value : int = NOTE_A_VALUE, accidental : int = 0, octave : int= 4) -> None:
        self._interpreter = interpreter
        # A4 id has 0 value
        self.value = value
        # either -2, -1, 0 , 1, 2
        self.accidental = accidental
        self.octave = octave



    def get_pitch_value(self) -> int:
        return 12 * self.octave + self.note + self.accidental


    def get_frequency(self):
        return 2 ** (self.get_pitch_value() / 12) * C0_BASE_FREQUENCY
    

    def is_valid():
        # TODO
        return True
    
    def __str__(self) -> str:
        return self._interpreter.note_to_str(self)
