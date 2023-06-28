from typing import Tuple

from .music_note import MusicNote
from .interval import Interval

class BaseInterpreter:
    def __init__(self, localization) -> None:
        self._localization = localization
    
    def loc(self, string: str) -> str:
        return self._localization.get(string)

    def str_to_note(self, string: str) -> MusicNote:
        raise NotImplementedError()

    def note_to_str(self, note: MusicNote) -> str:
        raise NotImplementedError()

    def notes_to_interval(self, notes : Tuple[MusicNote, MusicNote]) -> Interval:
        interval = Interval(self)
        interval.get_from_notes(notes)
        return interval
    
    def interval_to_str(self, interval: Interval) -> str:
        raise NotImplementedError()