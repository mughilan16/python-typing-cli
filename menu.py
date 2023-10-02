from termcolor import colored
from os import system
from arrange import arrangespeed

main_color = "cyan"
second_color = "green"

def printMenu():
    clear()
    print(colored("╭────────────────────────────────────────────────────────────╮", main_color))
    print(colored("│                          Menu                              │", main_color))
    print(colored("│────────────────────────────────────────────────────────────│", main_color))
    print(colored("│                                                            │", main_color))
    print(colored("│ 1. Sentence 1                                              │", main_color))
    print(colored("│ 2. Sentence 2                                              │", main_color))
    print(colored("│ 3. Sentence 3                                              │", main_color))
    print(colored("│ 4. Pratice Mistake words                                   │", main_color))
    print(colored("│ 5. Words                                                   │", main_color))
    print(colored("│ 6. Exit                                                    │", main_color))
    print(colored("╰────────────────────────────────────────────────────────────╯", main_color))

def clear():
    system("cls")

# Paragraph Typing
def typingMain(strings, errorMessage, string_i, string_time, speedString, length):
    clear()
    print(colored( "╭──────────────────────────────────────────────────────────────────────────────────────────╮",main_color)+colored("╭─────────╮", second_color)+colored("╭───────╮", main_color)+colored("╭─────────╮", second_color)+colored("╭─────────────╮", main_color))
    print(colored(f"│                                     Type the below word                                  │",main_color)+colored("│ Result  │", second_color)+colored("│ Line  │", main_color)+colored("│  Time   │", second_color)+colored("│ Speed(wpm)  │",main_color))
    print(colored( "│──────────────────────────────────────────────────────────────────────────────────────────│",main_color)+colored("│─────────│", second_color)+colored("│───────│", main_color)+colored("│─────────│", second_color)+colored("│─────────────│", main_color))
    print(colored(f"│{strings}  │", main_color)+colored(f"│ {errorMessage} │", second_color)+colored(f"│ {string_i}/{length}  │", main_color)+colored(f"│{string_time} sec  │", second_color)+colored(f"│{speedString} wpm      │",main_color))
    print(colored( "╰──────────────────────────────────────────────────────────────────────────────────────────╯",main_color)+colored("╰─────────╯", second_color)+colored("╰───────╯", main_color)+colored("╰─────────╯", second_color)+colored("╰─────────────╯", main_color))

def mmwWrong(words, answer):
            clear()
            print(colored("╭────────────────────╮╭────────────────────────────────╮", main_color))
            print(colored("│ Words              ││  Mistake Words                 │", main_color))
            print(colored("│────────────────────││────────────────────────────────│", main_color))
            j = 0
            for i in words:
                print(colored(f"│ {answer[j]}   ││   {i}             │", main_color))
                j += 1                
            print(colored("╰────────────────────╯╰────────────────────────────────╯", main_color))

def mmwCorrect():
    clear()
    print(colored("╭──────────────────────────────────────────────────────╮", main_color))
    print(colored("│ No Errors :)                                         │", main_color))
    print(colored("╰──────────────────────────────────────────────────────╯", main_color))


def mmwMenu(speeds):
    try:speed = sum(speeds)/len(speeds)
    except ZeroDivisionError : speed = 0
    speed2 = arrangespeed(int(speed))
    print(colored("╭──────────────────────────────────────────────────────╮", main_color))
    print(colored(f"│ Average Speed is {speed2} words per minute                │", main_color))
    print(colored("╰──────────────────────────────────────────────────────╯", main_color))
    print(colored("Enter to menu --->", main_color), end="")
    input()

# Errors test
def missedWordsTest(i, errorWords, j):
    clear()
    print(colored( "╭──────────────────────────────────────────────────────────────────────────────────────────╮", main_color), colored("╭─────────╮", second_color))
    print(colored(f"│{i}  ││ {j}/{len(errorWords)} ││", main_color))
    print(colored( "╰──────────────────────────────────────────────────────────────────────────────────────────╯", main_color), colored("╰─────────╯", second_color))
    answer = input(" ")
    j += 1
    return j, answer

# Words test

def wordtypingMenu(word, string_i, num, speed):
    clear()
    print(colored("╭───────────╮╭─────────╮╭─────────╮", main_color))
    print(colored("│ Type word ││  Word   ││  Speed  │", main_color))
    print(colored("│───────────││─────────││─────────│", main_color))
    print(colored(f"│{word}  ││ {string_i}/{num}   ││ {speed} wpm │", main_color))
    print(colored("╰───────────╯╰─────────╯╰─────────╯", main_color))

