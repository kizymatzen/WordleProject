# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    # create the game window
    gw = WordleGWindow()

    # pick a random word from the provided list
    random_word = random.choice(FIVE_LETTER_WORDS)

    # display the random_word in the first row
    for col, letter in enumerate(secret_word):
        gw.set_square_letter(0, col, letter) 

    # set up the enter key listener
    gw.add_enter_listener(enter_action)

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
