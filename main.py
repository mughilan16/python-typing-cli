from myStrings import strings1, strings2, strings3  # Strings for paragraph
from myStrings import strings4  # For words
from time import time  # To calculate Time
from arrange import arrangeMain, arrangei, arrangeWords, arrangespeed  # This for arranging
from menu import printMenu, clear, missedWordsTest
from menu import typingMain, wordtypingMenu  # Menu
from menu import mmwMenu, mmwWrong, mmwCorrect  # mw - Mistake Words
from random import randint 

class Typing:
    def __init__(self):
        self.strings = str()   # Main string
        self.i = int()   # For string counting
        self.answers = list()   # To store answers for check
        self.missedWords = list()   # To store Mistake words
        self.wrongAnswer = list()   # To Store mistake answer
        self.speeds = list()   # To store speed of test
        
    def menu(self):
         # This function is from Menu
        printMenu()   # printMenu function print the main menu
        try:
            choice = int(input("Enter you choice : "))  # Taking the user choice
        except ValueError:  # for other value other than num
            choice = 1  # Giving a default value to choice
        except KeyboardInterrupt:  # for quit with ctrl + c
            choice = 6  # For exit
            
        if choice == 1:
            self.strings = strings1  # Variable from myStrings.py
            self.main(self.strings, 0, " Type  ", 0, 0)  # Calling main method
             # This function is from Menu
            self.result()  # This function from Menu
        elif choice == 2:
            self.strings = strings2  # Variable from myStrings.py
            self.main(self.strings, 0, " Type  ", 0, 0)
            self.result()  # This function from Menu
        elif choice == 3:
            self.strings = strings3  # Variable from myStrings.py
            self.main(self.strings, 0, " Type  ", 0, 0)
            self.result()  # This function from Menu
        elif choice == 4:
            self.mwTest()  # This function from Menu
        elif choice == 5:
            self.strings = strings4  # Variable from myStrings.py
            self.wordsTyping()  # This function from Menu
        
    def mwTest(self):
            j = 1  # J for count missedWords
            missedWords2 = list()  # variable for store missedWords temp
            answer = str()
            if len(self.missedWords) > 0:
                start = time()
                for i in self.missedWords:
                    j, answer2 = missedWordsTest(i, self.missedWords, j)
                    if answer2 == i:
                        missedWords2.append(i)
                    answer += i
                self.missedWords = missedWords2
                stop = time()
                clear()  # This function from Menu
                totaltime = int(stop - start)
                print(f"Time : {totaltime} sec ")
                speed = int((len(answer)/5)/(totaltime/60))
                print(f"Speed : {speed} wpm")
            else:
                clear()
                print("No Mistake :)")
            self.menu()
        
    def wordsTyping(self):
        words = []
        answers = []
        errorWordsWordword = []
        errorWordsWordanswer = []
        speeds = []
        speed = 0
        totaltime = 0
        num = int(input("Enter number of words you wanna type: "))
        for i in range(num):
            string_i = arrangei(i)
            length = len(self.strings) - 1
            word = self.strings[randint(0, length)]
            words.append(word)
            speed_string = arrangespeed(speed)
            wordtypingMenu(word, string_i, num, speed_string)
            start = time()
            answer = (input(" "))
            answers.append(answer)
            stop = time()
            totaltime = stop - start
            if totaltime != 0:
                speed = int((len(answer)/5)/(totaltime/60))
            else:
                speed = 0
            speeds.append(speed)
        word=[]
        answer=[]
        for i in range(len(words)-1):
            answer = answers[i].split()
            word = words[i].split()
            if answer[1] != word[1]:
                errorWordsWordword.append(word[0])
                errorWordsWordanswer.append(answer[1])
        if errorWordsWordword != 0:
            wordsWrong, answerwrong = arrangeWords(errorWordsWordanswer\
                    , errorWordsWordword)
            mmwWrong(answerwrong, wordsWrong)  # This function from Menu
        else:
            mmwCorrect()  # This function from Menu
        mmwMenu(speeds)  # This function from Menu
        self.menu()
        
    def result(self):
        try:
            if len(self.missedWords) != 0:
                answers2, words2 = arrangeWords(self.missedWords, self.wrongAnswer)
                mmwWrong(answers2, words2)  # This function from Menu
            else:
                mmwCorrect()  # This function from Menu
            mmwMenu(self.speeds)  # This function from Menu
            self.menu()
        except KeyboardInterrupt:
            self.menu()
        
    def check(self, words, answer):
        error = False
        words = words.split()
        answer = answer.split()
        if len(answer) != len(words):
            missingWords = len(words) - len(answer)
            for i in range(missingWords + 1):
                answer.append(" ")
        for i in range(0, len(words)):
            if words[i] != answer[i]:
                self.missedWords.append(words[i])
                self.wrongAnswer.append(answer[i])
                error = True
        if error: return " Wrong "
        return "Correct"
     
    def main(self,strings, i, errorMessage, totaltime, speed):
        string_i, string_time, speedString = arrangeMain(i, totaltime, speed)
        length = len(self.strings)
        typingMain(self.strings[i], errorMessage, string_i,\
                string_time, speedString, length)  # This function from Menu
        start = time()  # Record time
        answer = input(" ")
        stop = time()  # Record time
        totaltime = int(stop - start)  # Stop - Start gives the time between them
        if totaltime != 0:
            speed = int((len(answer)/5)/(totaltime/60))
        else:
            speed = 0
        self.speeds.append(speed)
         #  check method split words and find mistake
        errorMessage = self.check(strings[i], answer)
        if i < len(self.strings) - 1:
            self.main(strings, i+1, errorMessage, totaltime, speed)

if __name__ == "__main__":
    typing = Typing()
    try:
        typing.menu()
    except KeyboardInterrupt:
        typing.result()  

