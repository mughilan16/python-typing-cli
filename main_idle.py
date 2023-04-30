import myStrings
import time

class Typing:
    def __init__(self):
        self.strings = " "
        self.i = 0
        self.answers = []
        self.errorWords = []
        self.wrongAnswer = []
        self.menu()

    def menu(self):
        self.clear()
        print("╭────────────────────────────────────────────────────────────╮")
        print("│                          Menu                              │")
        print("│────────────────────────────────────────────────────────────│")
        print("│                                                            │")
        print("│ 1. When My Teacher Scolded Me                      12      │")
        print("│ 2. The Saddest Day of My Life                      16      │")
        print("│ 3. The Habit of Reading                            12      │")
        print("│ 4. Pratice Mistake words                                   │")
        print("│ 5. Exit                                                    │")
        print("╰────────────────────────────────────────────────────────────╯")
        choice = int(input("Enter you choice :"))
        if choice == 5:
            pass
        elif choice == 1:
            self.strings = myStrings.strings1
        elif choice == 2:
            self.strings = myStrings.strings2
        elif choice == 3:
            self.strings = myStrings.strings4
        if choice < 4:
            self.main(self.strings, 0, "Type   ", 0)
            self.errorShow()
            input("Back to menu ==>")
            self.menu()


    def errorShow(self):
            for i in range(0, len(self.errorWords)-2):
                print(i, self.errorWords[i], "  │  ", self.wrongAnswer[i])


    def clear(self):
        print("\n" * 30)

    def arrange(self):
        pass

    def check(self, words, answer):
        error = False
        words = words.split()
        answer = answer.split()
        type(words)
        type(answer)
        if len(answer) != len(words):
            missingWords = len(words) - len(answer)
            for i in range(missingWords + 1):
                answer.append(" ")
        for i in range(0, len(words)):
            if words[i] != answer[i]:
                self.errorWords.append(words[i])
                self.wrongAnswer.append(answer[i])
                error = True
        if error:
            return "Wrong  "
        return "Correct"

    def main(self,strings, i, errorMessage, totaltime):
        self.clear()
        print("╭──────────────────────────────────────────────────────────────────────────────────────────╮╭─────────╮╭──────╮╭──────────────────────╮")
        print(f"│{self.strings[i]}  ││ {errorMessage} ││ {i+1}/{len(strings)} ││ {totaltime} sec │")
        print("╰──────────────────────────────────────────────────────────────────────────────────────────╯╰─────────╯╰──────╯╰──────────────────────╯")
        start = time.time()
        answer = input(" ")
        stop = time.time()
        totaltime = int(stop - start)
        errorMessage = self.check(strings[i], answer)
        if i < len(self.strings) - 1:
            self.main(strings, i+1, errorMessage, totaltime)


if __name__ == "__main__":
    typing = Typing()
