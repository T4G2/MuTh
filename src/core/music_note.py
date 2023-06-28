from .consts import *

class MusicNote:
    def __init__(self, value : int = NOTE_A_VALUE, accidental : int = 0, octave : int= 4) -> None:
        # A4 id has 0 value
        self.value = value
        # either -2, -1, 0 , 1, 2
        self.accidental = accidental
        self.octave = octave


    def get_frequency(self):
        return 2 ** ((self.note + self.accidental) / 12) * A4_BASE_FREQUENCY
    

    def is_valid():
        # TODO
        return True
