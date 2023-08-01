import string
import os
# import time
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Hangman:
    played_word = ""
    gameboard = []
    gameboard_finished = []
    guess = ''
    guess_archieve = ['Guesses:']
    lives = ['Lives(8):']
    end_state = False
    word_list = ["family"]
    hangman_art = [
        "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
    ]

    def set_Word(self):
        word = random.choice(self.word_list)
        self.played_word = word

    def set_finished_board(self, word):
        word_list_finished = list(word)
        self.gameboard_finished = word_list_finished

    def set_create_board(self, word):
        word_list_playing = ['_'] * len(word)
        self.gameboard = word_list_playing

    def set_move(self, guess, location):
        self.gameboard[location] = guess

    def set_guess(self, player_guess):
        if player_guess in self.guess_archieve:
            print("You have already tried to play " + player_guess)
        elif player_guess in self.gameboard_finished:
            for position, char in enumerate(self.gameboard_finished):
                if char == player_guess:
                    self.set_move(player_guess, position)
            self.guess_archieve.append(player_guess)
        else:
            self.show_hangman()
            self.lives.append('x')
            self.guess_archieve.append(player_guess)

    def show_hangman(self):
        incorrect_guesses = len(self.lives) - 1
        if incorrect_guesses < len(self.hangman_art):
            hangman_image = self.hangman_art[incorrect_guesses]
            gui_hangman_image['text'] = hangman_image
        else:
            gui_hangman_image['text'] = "No more hangman images available."

    def get_eg_status(self):
        if len(self.lives) == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("GAME OVER!", "GAME OVER: Thanks for playing! \n Answer:\t" +
                                str(''.join([str(elem) for elem in self.gameboard_finished])))
            main_form.quit()
        elif self.gameboard == self.gameboard_finished:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("Congrats!", "You won! Thanks for playing!")
            main_form.quit()

    def get_user_guess(self, letter):
        char = str(letter)
        if len(char) == 1 and char.isalpha():
            self.set_guess(char.lower())
        else:
            print("Guess must be a single letter!")


game = Hangman()
game.set_Word()
game.set_create_board(game.played_word)
game.set_finished_board(game.played_word)

main_form = Tk()
main_form.title("Hangman")
main_form.geometry("700x600")
main_form.resizable(0, 0)

alphaList = list(string.ascii_lowercase)
game.gameboard

gui_gameboard = tk.Label(main_form, text=game.gameboard, font="Verdana 30 bold")
gui_gameboard.pack(side="top")

gui_guess_archieve = tk.Label(main_form, text=game.guess_archieve, font="Verdana 10 bold")
gui_guess_archieve.pack()
gui_guess_archieve.place(bordermode=OUTSIDE, x=200, y=555)

gui_lives = tk.Label(main_form, text=game.lives, font="Verdana 10 bold")
gui_lives.pack()
gui_lives.place(bordermode=OUTSIDE, x=200, y=580)

gui_hangman_image = tk.Label(main_form, text="", font="Verdana 20 ")
gui_hangman_image.pack()
gui_hangman_image.place(bordermode=OUTSIDE, x=400, y=100)


def btn_Click(letter):
    letter.config(state="disabled")
    game.get_user_guess(letter["text"].lower())
    gui_gameboard["text"] = game.gameboard
    gui_guess_archieve["text"] = game.guess_archieve
    gui_lives["text"] = game.lives
    game.get_eg_status()
    print(letter["text"])


def create_button(letter, xpos, ypos, index):
    button = tk.Button(main_form, text=letter.upper(), command=lambda: btn_Click(button))
    button.pack()
    button.place(bordermode=OUTSIDE, height=50, width=100, x=xpos, y=ypos)


def populate_board():
    c = 0
    startpos = 350
    xpos = 0
    ypos = startpos
    while c < 26:
        if c == 6:
            ypos = startpos + 50
            xpos = 0
        elif c == 12:
            ypos = startpos + 100
            xpos = 0
        elif c == 18:
            ypos = startpos + 150
            xpos = 0
        elif c == 24:
            ypos = startpos + 200
            xpos = 0

        create_button(alphaList[c], xpos, ypos, c)
        xpos = xpos + 100
        c = c + 1


populate_board()
main_form.mainloop()
