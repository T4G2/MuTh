from core.deutch_interpreter import DInterpeter
import repackage
repackage.up()

class App:
    def __init__(self) -> None:
        pass

    
    def run(self):
        muth = DInterpreter()

        print("Input New Note")
        input_str = input("Input new note or exit to exit")
        while(input_str.lower() != "exit"):
            try:
                note = muth.str_to_note(input_str)
                print(f'{note.note}, {note.accidental}')
            except ValueError as err:
                print(f'Error: {err.args}')
