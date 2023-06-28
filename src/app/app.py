import repackage
repackage.up(1)

from core.german_interpreter import DInterpreter

class App:
    def __init__(self) -> None:
        pass

    
    def run(self):
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
