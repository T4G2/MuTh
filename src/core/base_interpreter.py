from music_note import MusicNote


class BaseInterpeter:
    def __init__(self) -> None:
        pass

    def str_to_note(self, string: str) -> MusicNote:
        raise NotImplementedError()

    def string_to_note(self, note: MusicNote) -> str:
        raise NotImplementedError()
