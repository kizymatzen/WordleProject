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
    guess_count = 0 # initialize the guess count

    # pick a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)    
        
    # display the random_word in the first row
    for col in range(N_COLS):
        gw.set_square_letter(0, col, random_word[col])
   

    def enter_action(s):

        nonlocal guess_count # allow modification of the guess count
   # print(gw.get_current_row())

        current_row = gw.get_current_row()

        # collect the word from the graphics window
        word = "".join([gw.get_square_letter(current_row, col) for col in range(N_COLS)]).lower()

        # check if the word is in the dictionary
        if word in FIVE_LETTER_WORDS:
            gw.show_message("Great job! That's a valid word.")
        else:
            gw.show_message("Not in word list.")

        gw.set_current_row(current_row + 1) # move to the next row
        guess_count += 1 # increment guess count

    # set up the enter key listener
    gw.add_enter_listener(enter_action)  
    
if __name__ == "__main__":
    wordle()