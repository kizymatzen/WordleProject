# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    # create the game window
    gw = WordleGWindow() 

     # pick a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)

    # display the random_word in the first row
    for col in range(N_COLS):
        gw.set_square_letter(0, col, random_word[col])

    def enter_action(s):
        # collect the word from the graphics window
        word = "".join([gw.get_square_letter(0, col) for col in range(N_COLS)])

        # check if the word is in the dictionary
        if word in FIVE_LETTER_WORDS:
            gw.show_message("Great job! That's a valid word.")
        else:
            gw.show_message("Not in word list.")


    # set up the enter key listener
    gw.add_enter_listener(enter_action)
    #

    # row = 0
    # clm = 0
    # rand_word = random.choice(FIVE_LETTER_WORDS)
    # for index in range(0,5):
    #     letter = rand_word[index]
    #     gw.set_square_letter(row, clm, letter)
    #     clm += 1


# Startup code

if __name__ == "__main__":
    wordle()
