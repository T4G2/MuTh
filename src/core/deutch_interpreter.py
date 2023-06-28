from music_note import MusicNote
from base_interpreter import BaseInterpeter
from funcs import parse_accidentals
from consts import *


BASE_NOTES = {
    0: "A",
    # 1: "B",
    2: "H",
    3: "C",
    5: "D",
    7: "E",
    8: "F",
    10: "G"
}


# TODO use bidict

#first one is pitch ,second one is accidental
BASE_NOTES_REVERSE = {
    "A": ( 0, 0),
    "B": ( 2,-1),
    "H": ( 2, 0),
    "C": ( 3, 0),
    "D": ( 5, 0),
    "E": ( 7, 0),
    "F": ( 8, 0),
    "G": (10, 0)
}

NAMING_EXCEPTIONS = {
    (2, -1) : "B"
}


class DInterpeter (BaseInterpeter):
    def __init__(self) -> None:
        pass

        '''
        Format of notes:
        First one should be nameof  note A, B, H, C, D, E, F, G, 
        Second one is optionally a number 
        Also the first if is smaller of larger should be treated as in different octave
        The thord and fourth is resered for accidentals '#', 'b' 'n', '##' , 'bb'
        '''
    def str_to_note(self, string: str) -> MusicNote:

        # TODO What about size of notes? A4 A3# A2n etc

        # min argument count is 1, max 3
        if  len(string) not in range(1, 3 + 1):
            raise ValueError(f'Incorrect Note Input: {str}')

        note_char = str[0]

        note_value = BASE_NOTES_REVERSE.get(note_char)

        if note_value is None:
            raise ValueError(f'Incorrect Note Input: {str}')


        
        accidental = parse_accidentals(string[1:])

        note = MusicNote(note_value, accidental)

        if not MusicNote.valid():
            raise ValueError(f'Incorrect Note Input: {str}')
        
        return note
        

        

    def string_to_note(self, note: MusicNote) -> str:
        raise NotImplementedError()
