#!/usr/bin/env python
from rpiledmatrix import switch_on, switch_off, turn_all_off, cleanup, blink_on, blink_off
import rpiledmatrix
def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    turn_all_off()
    for i, b in enumerate(board[1:10]):
        if b.lower() == 'x':
            blink_on(i)
        elif b.lower() == 'o':
            switch_on(i)
        else:
            switch_off(i)
            blink_off(i)

def prompt(text):
    print(text)

def cleanup():
    turn_all_off()
    rpiledmatrix.cleanup()
    prompt("All is well")