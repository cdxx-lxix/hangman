import time

class Messages:
    def displayHidden(self, hidden_word):
        print(f"::: {hidden_word} ::: \n")

    def displayMessage(self, state: str, word_to_guess="", hint = "", hidden = ""):
        if state == "win":
            print(f"Поздравляю! Вы верно угадали слово - {word_to_guess} \n")

        elif state == "failure":
            print(f"Мдауш. Попробуйте свои знания вновь, а слово было - {word_to_guess} \n")

        elif state == "accept":
            print("Ваше слово принято. \n"
                  "Теперь передайте контроль второму игроку. \n")
            for i in range(1, 6):
                time.sleep(1)
                print(i)
            print(f"В этом слове {len(word_to_guess)} букв")
            print("Подсказка: " + hint)
            print(hidden)

        elif state == "start":
            print("Добро пожаловать в игру Виселица! \n"
                  "Правила просты: \n"
                  "1. Введите своё слово, количество попыток и подсказку по желанию. Потом передайте управление второму игроку. \n "
                  "2. У второго игрока есть возможность угадывать по букве или целое слово сразу. \n"
                  "После победы или поражения можно начать новую игру или выйти \n \n")