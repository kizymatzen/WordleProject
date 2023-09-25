# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from tkinter import *
from WordleDictionary import FIVE_LETTER_WORDS
from WordleDictionaryPort import FIVE_LETTER_WORDS_PORT
from WordleGraphics import (
    WordleGWindow as EnglishWordle,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    get_current_word,
    color_word_row,
)
from WordleGraphicsPort import WordleGWindow as PortugueseWordle, N_COLS, N_ROWS


def wordle():
    def show():
        if clicked.get() == "English":
            gw = EnglishWordle()
            winning_word = random.choice(FIVE_LETTER_WORDS)
            print(winning_word)
            total_guesses = 6

            def enter_action(s):
                nonlocal total_guesses

                current_row = gw.get_current_row()

                word = get_current_word(gw, current_row)

                if is_valid_word(word):
                    color_word_row(word, winning_word, current_row, gw)
                    if word == winning_word:
                        gw.show_message("You win!")
                        gw.set_current_row(7)
                    else:
                        total_guesses -= 1
                        gw.show_message(
                            f"Great job that's a valid word! {total_guesses} guesses left!"
                        )
                        gw.set_current_row(current_row + 1)
                else:
                    gw.show_message(
                        f"Not in word list. Only {total_guesses} guesses left!"
                    )

            def is_valid_word(word):
                return word in FIVE_LETTER_WORDS

            gw.add_enter_listener(enter_action)

        #  ----------------------- portuguese wordle version ----------------------------

        # Portuguese wordle version
        elif clicked.get() == "Portuguese":
            gw = PortugueseWordle()
            winning_word = random.choice(FIVE_LETTER_WORDS_PORT)
            print(winning_word)
            total_guesses = 6

            def enter_action(s):
                nonlocal total_guesses

                current_row = gw.get_current_row()

                word = get_current_word(gw, current_row)

                if is_valid_word(word):
                    color_word_row(word, winning_word, current_row, gw)
                    if word == winning_word:
                        gw.show_message("You win!")
                        gw.set_current_row(7)
                    else:
                        total_guesses -= 1
                        gw.show_message(
                            f"Great job that's a valid word! {total_guesses} guesses left!"
                        )
                        gw.set_current_row(current_row + 1)
                else:
                    gw.show_message(
                        f"Not in word list. Only {total_guesses} guesses left!"
                    )

            def is_valid_word(word):
                return word in FIVE_LETTER_WORDS_PORT

            gw.add_enter_listener(enter_action)

    root = Tk()
    root.geometry("200x200")

    options = ["English", "Portuguese"]

    clicked = StringVar()
    clicked.set("English")

    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    button = Button(root, text="click me", command=show).pack()

    root.mainloop()


if __name__ == "__main__":
    wordle()


#  ----------------------- helper functions ----------------------------


def get_current_word(gw, row):
    return "".join([gw.get_square_letter(row, col) for col in range(N_COLS)]).lower()


def is_valid_word(word):
    return word in FIVE_LETTER_WORDS


def color_word_row(word, winning_word, row, gw):
    highlighted_letters = set()

    for index, letter in enumerate(word):
        if letter == winning_word[index]:
            gw.set_square_color(row, index, CORRECT_COLOR)
        elif letter in winning_word and letter not in highlighted_letters:
            gw.set_square_color(row, index, PRESENT_COLOR)
            highlighted_letters.add(letter)
        else:
            gw.set_square_color(row, index, MISSING_COLOR)
