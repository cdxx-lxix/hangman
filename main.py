from Hangman import *

if __name__ == '__main__':
    game = Hangman()
    while game.state:
        game.startGame()
