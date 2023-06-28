from consts import *

class MusicNote:
    def __init__(self, note: int, accidental: int) -> None:
        # A4 id has 0 value
        self.note = note
        # either -2, -1, 0 , 1, 2
        self.accidental = accidental


    def get_frequency(self):
        return 2 ** ((self.note + self.accidental) / 12) * A4_BASE_FREQUENCY
    

    def is_valid():
        # TODO
        return True
