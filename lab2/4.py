def compose(notes, moves, start):
    i = start
    song = [notes[start]]
    for move in moves:
        i = (i + move) % len(notes)
        song += [notes[i]]
    return song

print(compose(['do', 're', 'mi', 'fa', 'sol'], [1, -3, 4, 2], 2))
