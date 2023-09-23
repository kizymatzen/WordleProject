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
    winning_word = random.choice(FIVE_LETTER_WORDS)
    print(winning_word)

    total_guesses = 6

    # display the random_word in the first row
    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, random_word[col])

    def enter_action(s):
        nonlocal total_guesses
        current_row = gw.get_current_row()

        print("just submitted row", current_row + 1)

        # collect the word from the graphics window
        word = "".join(
            [gw.get_square_letter(current_row, col) for col in range(N_COLS)]
        ).lower()

        # check if the word is in the dictionary
        if word in FIVE_LETTER_WORDS:
            # if the correct word was guessed, alert the user that they won
            if word == winning_word:
                gw.show_message("You win!")
                gw.set_current_row(7)
            else:
                total_guesses -= 1
                gw.show_message(
                    "Great job! That's a valid word. "
                    + str(total_guesses)
                    + " guesses left!"
                )
                # increment the row if they user typed in a valid word
                gw.set_current_row(current_row + 1)

        else:
            gw.show_message(
                "Not in word list. Only " + str(total_guesses) + " guesses left!"
            )

    # set up the enter key listener
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
