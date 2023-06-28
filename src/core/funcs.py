ACCIDENTALS = {
    '#' : +1,
    'b' : -1,
    'n' : 0,
}

def parse_accidentals(acc: str) -> int:
    # it is either ## or bb or # or b or n(as natural)
    
    acc_count = len(acc)

    if (acc_count == 2):
        if acc[0] != acc[1] or acc[0] not in ('#, b'):
            raise ValueError(f'Accidental {acc} is not correct!')
        return ACCIDENTALS[acc[0]] * 2
    

    if (acc[0] not in ('#', 'b', 'n')):
        raise ValueError(f'Accidental {acc} is not correct!')

    return ACCIDENTALS[acc[0]]
    
    

        
