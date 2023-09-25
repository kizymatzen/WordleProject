"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR
)


def wordle():
    gw = WordleGWindow()
    winning_word = random.choice(FIVE_LETTER_WORDS)
    print(winning_word)
    total_guesses = 6

    def enter_action(s):
        nonlocal total_guesses
        current_row = gw.get_current_row()
        word = get_current_word(gw, current_row)

        if is_valid_word(word):
            # color the word if it is valid. This will color the word even if they win too.
            gw.color_word_row(word, winning_word, current_row)
            if word == winning_word:
                gw.show_message("You win!")
                gw.set_current_row(6)
            else:
                total_guesses -= 1
                if(total_guesses == 0):
                    gw.show_message("Better luck next time!")
                else:
                    gw.show_message(
                        f"Great job that's a valid word! {total_guesses} guesses left!"
                    )
                gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"Not in word list. Only {total_guesses} guesses left!")

    gw.add_enter_listener(enter_action)


def get_current_word(gw, row):
    return "".join([gw.get_square_letter(row, col) for col in range(N_COLS)]).lower()


def is_valid_word(word):
    return word in FIVE_LETTER_WORDS

if __name__ == "__main__":
    wordle()