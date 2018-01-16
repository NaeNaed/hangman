import os
import random

def get_puzzle():
    file_names = os.listdir("puzlles")

    for i, f in enumerate(file_names):
        print(str(i+1) + ") " + f)

    choice = input("Which one? ")
    choice = int(choice)

    file = "puzlles/" + file_names[choice-1]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)

    category = lines[0]
    puzzle = random.choice(lines[1:])

    print(category)
    print(puzzle)

def start_screen():
    print("""                                               
  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
 / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
/ __  / (_| | | | | (_| | | | | | | (_| | | | |
\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       """)

def end_screen():
    print(""" _               _   _       _                 _             _ _       _ _  _         _ _____ 
| |__  _   _    /_\ | | ___ (_) __ _ _ __   __| |_ __ ___   / / |     / | || |       / |___  |
| '_ \| | | |  //_\\| |/ _ \| |/ _` | '_ \ / _` | '__/ _ \  | | |_____| | || |_ _____| |  / / 
| |_) | |_| | /  _  \ |  __/| | (_| | | | | (_| | | | (_) | | | |_____| |__   _|_____| | / /  
|_.__/ \__, | \_/ \_/_|\___|/ |\__,_|_| |_|\__,_|_|  \___/  |_|_|     |_|  |_|       |_|/_/   
       |___/              |__/                                                                """)

def get_name():
    player_name = input("What is your name? ")
    return player_name

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(player_name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        guess = input("Enter a letter " + player_name + ". ")
        guess = guess.lower()
        if len(guess) >= 2:
            print("Please enter 1 letter.")
        elif guess is not alphabet:
            print("Please enter a letter.")
        else:
            return guess
        
def get_limit():
    limit = 6
    return limit
    
def display_board(solved):
    print(solved)

def show_strikes(strikes, limit):
    print("You have " + str(strikes) + " out of " + str(limit) + " left. ")
    
def show_result():
    print("You win!")
    
def play():
    player_name = get_name()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    limit = get_limit()
    strikes = (limit - 1)

    print(solved)

    while solved != puzzle:
        letter = get_guess(player_name)

        if letter not in puzzle:
            if strikes == 0:
                print("You lose!")
                letter = 0

            else:
                strikes -= 1
                
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        show_strikes(strikes, limit)

    show_result()

start_screen()

play()

end_screen()
