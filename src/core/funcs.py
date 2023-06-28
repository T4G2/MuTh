from .music_note import MusicNote

ACCIDENTALS = {
    '#' : +1,
    'b' : -1,
    'n' : 0,
    's' : +1, # As Sharp
}

def parse_accidentals(acc: str, note: MusicNote) -> int:
    # it is either ## or bb or # or b or n(as natural)
    
    acc_count = len(acc)

    if acc_count == 0:
        return

    if (acc_count == 2):
        if acc[0] != acc[1] or acc[0] not in ('#', 'b', 's'):
            raise ValueError(f'Accidental {acc} is not correct!')
        note.accidental = ACCIDENTALS[acc[0]] * 2
        return 
    

    if (acc[0] not in ACCIDENTALS):
        raise ValueError(f'Accidental {acc} is not correct!')

    note.accidental =  ACCIDENTALS[acc[0]]
    
    

        
