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
    # this is a test
    # pick a random word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)

    total_guesses = 10

    # display the random_word in the first row
    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, random_word[col])

    def enter_action(s):
        nonlocal total_guesses

        # # stops the counter if they run out of guesses
        if total_guesses == 0:
            return

        current_row = gw.get_current_row()
        print("just submitted row", current_row + 1)

        # collect the word from the graphics window
        word = "".join(
            [gw.get_square_letter(current_row, col) for col in range(N_COLS)]
        ).lower()

        # decrement the total number of guesses
        total_guesses -= 1

        # check if the word is in the dictionary
        if word in FIVE_LETTER_WORDS:
            gw.show_message(
                "Great job! That's a valid word. "
                + str(total_guesses)
                + " guesses left!"
            )
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(
                "Not in word list. Only " + str(total_guesses) + " guesses left!"
            )

        # end the game if they run out of guesses
        if total_guesses == 0:
            gw.show_message("Game is over! You ran out of guesses:(")

    # set up the enter key listener
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
