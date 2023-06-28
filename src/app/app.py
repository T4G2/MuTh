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
        
        muth = DInterpreter()

        input_str = ""
        while(True):
            try:
                input_str = input("Input new note or exit to exit: \n")

                if input_str.lower().strip() == "exit":
                    return

                note = muth.str_to_note(input_str)
                print(f'{note.octave}, {note.value}, {note.accidental}')
            except ValueError as err:
                print(f'Error: {err}')
                return
