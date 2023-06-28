from typing import Tuple

from .base_interpreter import BaseInterpreter
from .funcs import parse_accidentals
from .consts import *

from .music_note import MusicNote
from .interval import Interval



BASE_NOTES = {
    ( 0, 0): "A",
    ( 2,-1): "B",
    ( 2, 0): "H",
    ( 3, 0): "C",
    ( 5, 0): "D",
    ( 7, 0): "E",
    ( 8, 0): "F",
    (10, 0): "G"
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


def process_note(string: str, note : MusicNote) -> str:
    if len(string) == 0:
         raise ValueError(f'Incorrect Note Input: {string}')
         
    note_char = string[0]

    note_tuple = BASE_NOTES_REVERSE.get(note_char.upper())
    if  note_tuple is None:
            raise ValueError(f'Incorrect Note Input: {string}')
    
    note_value, accidental = note_tuple

    octave = 3
    if note_char.isupper():
         octave -= 1

    note.value = note_value
    note.accidental = accidental
    note.octave = octave

    return string[1:]


def process_octave(string: str, note: MusicNote) -> str:
    if len(string) == 0 or not string[0].isdigit():
         return string
    delta_octave = int(string[0])

    # this means that any number after changes negatively the octave
    if note.octave < 3:
         delta_octave *= -1

    note.octave += delta_octave
    return string[1:]


class DInterpreter (BaseInterpreter):
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

        note = MusicNote(self)
        string = process_note(string, note)
        string = process_octave(string, note)
        parse_accidentals(string, note)

        if not MusicNote.is_valid():
            raise ValueError(f'Incorrect Note Input: {str}')
        
        return note
        

    def note_to_str(self, note: MusicNote) -> str:
        raise NotImplementedError()
    
    
    def interval_to_str(self, interval: Interval) -> str:
        return "Interval Naming Non Implemented"
    
    def str_to_interval(self, string:str) -> Interval:
         pass
