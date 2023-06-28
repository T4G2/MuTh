from .consts import *

class MusicNote:
    def __init__(self, interpreter: "BaseInterpreter", value : int = NOTE_A_VALUE, accidental : int = 0, octave : int= 4) -> None:
        self._interpreter = interpreter
        # C id has 0 value ( 0 - 6)
        self.value = value
        # either -2, -1, 0 , 1, 2
        self.accidental = accidental
        self.octave = octave



    def get_pitch_value(self) -> int:
        return 12 * self.octave + NOTES_SEMITONES[self.value] + self.accidental


    def get_frequency(self):
        return 2 ** (self.get_pitch_value() / 12) * C1_BASE_FREQUENCY
    

    def is_valid():
        # TODO
        return True
    
    def __str__(self) -> str:
        return self._interpreter.note_to_str(self)
