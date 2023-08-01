from hangman_game.hangman import Hangman

game = Hangman()
game.set_Word()
game.set_create_board(game.played_word)
game.set_finished_board(game.played_word)
