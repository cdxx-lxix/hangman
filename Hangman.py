from App import *
from Messages import *
import sys, subprocess


class Hangman:

    def __init__(self, state = True):
        self.state = state
        self.victory_state = False

    def startGame(self):

        msg = Messages()
        msg.displayMessage("start")
        input = self.inputWithCheck()
        if input[2]: hint = input[2]
        else: hint = 'не предоставлена'
        game = App(input[0], int(input[1]), hint)
        msg.displayMessage("accept", game.word_to_guess, game.hint)
        while not self.victory_state:
            game.makeGuess()
            self.victory_state = game.checkVictory()
            if self.victory_state:
                self.playAgain()



    def playAgain(self):
        repeat = input("Играть снова? да \ нет: ").lower()
        if repeat == 'да':
            self.victory_state = False
            self.clear()
            self.startGame()
        else:
            self.state = False

    def inputWithCheck(self):
        player_input = input("Введите в таком формате 'слово(str), кол-во жизней(int), подсказка(опционально, str)' вашу загадку: ").lower()
        if not player_input:
            player_input = input("Вы ничего не ввели. Если хотите играть следуйте правилам!: ")
        player_input = self.makeList(player_input)
        return player_input

    def makeList(self, input):
        input.strip()
        input = input.split(",", 2)
        return input

    def clear(self):
        os = sys.platform
        if os == 'win32':
            subprocess.run('cls', shell=True)
        elif os == 'linux' or 'darwin':
            subprocess.run('clear', shell=True)
