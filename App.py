from Messages import *
import time


class App():
    def __init__(self, word_to_guess: str, number_of_lives: str, hint: str):
        self.word_to_guess = word_to_guess.lower()
        self.number_of_lives = number_of_lives
        self.hint = hint
        self.hidden_word = "*" * len(self.word_to_guess)
        self.victory_state = False
        self.msg = Messages()

    def uncoverLetters(self, guess):
        result = ""
        for i in range(len(self.word_to_guess)):
            if self.word_to_guess[i] == guess:
                result = result + guess
            else:
                result = result + self.hidden_word[i]

        return result

    def makeGuess(self):
        player_input = input("Введите букву или слово целиком: ")
        self.guessCheck(player_input)
        if player_input in self.word_to_guess:
            self.hidden_word = self.uncoverLetters(player_input)
            self.msg.displayHidden(self.hidden_word)
        else:
            self.livesController()



    def guessCheck(self, input):
        if input == self.word_to_guess:
            self.msg.displayMessage("win", self.word_to_guess)
            self.victory_state = True


    def livesController(self):
        if self.number_of_lives == 0:
            self.msg.displayMessage("failure", self.word_to_guess)
            self.victory_state = True
        else:
            self.number_of_lives -= 1
            print(f"У вас осталось жизней: {self.number_of_lives}")

    def checkVictory(self):
        return self.victory_state
