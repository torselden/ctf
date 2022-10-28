#!/bin/env python3

from pwn import remote
from pprint import pprint as pp


HOST = 'ctf.knowit.se'
PORT = 59210

MUSIC_NOTATION = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5' ][::-1]


def main ():

    there_is_data = True

    conn = remote(HOST, PORT)

    for _ in range(18):  # drop the splash screen ascii art
        conn.recvline()

    while True:
        data = conn.recvuntil([b"Sing it:",b"}"])
        if b"}" in data:
            pp(data.split(b'\n'))
            conn.close()
            exit(0)
        score = parse_score(data)
        pp(score)
        note_values = parse_notes(score)
        pp(note_values)
        conn.sendline(note_values)
        

def parse_score(data):
    score_lines = data.split(b'\n') # rad 0 = A5, rad 12 = C4
    return score_lines


def parse_notes(score):
    notes = {}
    for note, line in enumerate(score):
        timing = [str(n) for (n, e) in enumerate(line) if e == ord('x')]
        for time in timing:
            if time in notes:
                notes[time] += MUSIC_NOTATION[line]
            else:
                notes[time] = MUSIC_NOTATION[note]

    note_string = ''.join([note for key, note in sorted(notes.items())]).encode()
    return note_string


if __name__ == '__main__':
    main()