from typing import Tuple

from .music_note import MusicNote

class Interval:
    

    def __init__(self, interpreter: "BaseInterpreter") -> None:
        self._interpreter = interpreter
        self._delta = 0 # name is always 1 above so Prime - _delta=0
        
        # IN CASE OF CONSONALT(1, 4,5,8) -1 diminished 0 perfect 1 augmented
        # IN CASE OF NON CONSONANT ??
        self.type = 0
        pass

    def get_type(self):
        return self.delta + 1
    
    def get_tuple(self):
        return self.delta + 1, self.type

    def is_perfect(self):
        return (self._delta % 12) in (1, 4, 5, 8)

    def __str__(self) -> str:
        return self._interpreter.interval_to_str(self)
    
    def get_from_notes(self, notes : Tuple[MusicNote, MusicNote]):
        self._delta = notes[1].value - notes[0].value
        self.type = notes[1].accidental - notes[0].accidental 
        pass