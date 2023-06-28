import repackage
repackage.up(1)

from core.german_interpreter import DInterpreter
from core.localization import Localization

class App:
    def __init__(self) -> None:
        pass

    def run(self):
        loc = Localization()
        if not loc.load("../res/loc/sk.loc"):
            print("Could Not Load Localization")
            return
        
        muth = DInterpreter(loc)

        input_str = ""
        while(True):
            try:
                input_str = input("Input two notes or exit to exit: \n")

                if input_str.lower().strip() == "exit":
                    return
                note_strs = input_str.strip().split(' ')
                notes = muth.str_to_note(note_strs[0]), muth.str_to_note(note_strs[1])
                interval = muth.notes_to_interval(notes)
                print(f'{interval._delta}, {interval.type}: {str(interval)}' )
                # print(f'{note.octave}, {note.value}, {note.accidental}: {note.get_frequency()}Hz')
            except ValueError as err:
                print(f'Error: {err}')
                return
