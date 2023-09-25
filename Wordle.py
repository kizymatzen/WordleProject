# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from tkinter import *
from WordleDictionary import FIVE_LETTER_WORDS
from WordleDictionaryPort import FIVE_LETTER_WORDS_PORT
from WordleGraphics import WordleGWindow as EnglishWordle, N_COLS, N_ROWS
from WordleGraphicsPort import WordleGWindow as PortugueseWordle, N_COLS, N_ROWS


def wordle():
    # English wordle version
    def show():
        if clicked.get() == "English":
            gw = EnglishWordle()

            guess_count = 0  # initialize the guess count

            # pick a random word from FIVE_LETTER_WORDS
            random_word = random.choice(FIVE_LETTER_WORDS)

            # display the random_word in the first row
            for col in range(N_COLS):
                gw.set_square_letter(0, col, random_word[col])

            def enter_action(s):
                nonlocal guess_count  # allow modification of the guess count
                # print(gw.get_current_row())

                current_row = gw.get_current_row()

                # collect the word from the graphics window
                word = "".join(
                    [gw.get_square_letter(current_row, col) for col in range(N_COLS)]
                ).lower()

                # check if the word is in the dictionary
                if word in FIVE_LETTER_WORDS:
                    gw.show_message("Great job! That's a valid word.")
                else:
                    gw.show_message("Not in word list.")

                gw.set_current_row(current_row + 1)  # move to the next row
                guess_count += 1  # increment guess count

            # set up the enter key listener
            gw.add_enter_listener(enter_action)

        # Portuguese wordle version
        elif clicked.get() == "Portuguese":
            gwp = PortugueseWordle()

            guess_count = 0  # initialize the guess count

            # pick a random word from FIVE_LETTER_WORDS
            random_word = random.choice(FIVE_LETTER_WORDS_PORT)

            # display the random_word in the first row
            for col in range(N_COLS):
                gwp.set_square_letter(0, col, random_word[col])

            def enter_action(s):
                nonlocal guess_count  # allow modification of the guess count
                # print(gw.get_current_row())

                current_row = gwp.get_current_row()

                # collect the word from the graphics window
                word = "".join(
                    [gwp.get_square_letter(current_row, col) for col in range(N_COLS)]
                ).lower()

                # check if the word is in the dictionary
                if word in FIVE_LETTER_WORDS:
                    gwp.show_message("Great job! That's a valid word.")
                else:
                    gwp.show_message("Not in word list.")

                gwp.set_current_row(current_row + 1)  # move to the next row
                guess_count += 1  # increment guess count

            # set up the enter key listener
            gwp.add_enter_listener(enter_action)

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
