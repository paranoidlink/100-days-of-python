import random
import art

def input_validator(usr_input, type):
    """Function to ensure all the user inputs work with the program"""
    if type == "difficulty":
        while usr_input.lower() not in ("easy", "hard"):
            usr_input = str(input("invalid input detected please enter either 'easy' or 'hard'\n"))
    elif type == "guess":
        guess_check = False
        while not guess_check:
            try:
                int(usr_input)
            except TypeError:
                usr_input = input("Invalid Input detected please enter a whole number between 1 and 100\n")
            else:
                guess_check = True
        while int(usr_input) <= 0 or int(usr_input) > 100:
            usr_input = input("Invalid Input detected please enter a whole number between 1 and 100\n")
    elif type == "replay":
        while usr_input.lower() not in ("y", "n"):
            usr_input = input("Invalid Input detected please enter either 'y' or 'n'\n")
    if isinstance(usr_input, str):
        usr_input = usr_input.lower()
    return usr_input

def difficulty_selector():
    """Function that allows the user to select how hard they want the game to be"""
    difficulty_choice = str(input("Select a difficulty type either 'easy' or 'hard'\n"))
    input_validator(difficulty_choice, "difficulty")
    if difficulty_choice == "easy":
        lives = 10
    elif difficulty_choice == "hard":
        lives = 5
    return lives

def game_setup():
    """Prints the initial messaging for the game has the user pick difficulty and the computer selects a number"""
    print(art.logo)
    print("Welcome to the number guesser")
    lives = difficulty_selector()
    target = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    return target, lives

def guess(current_lives, current_target):
    """Has the user guess a number and checks it against the one chosen by the computer and determines if they match"""
    won = False
    guess = input("Please type your guess\n")
    guess = input_validator(guess, "guess")
    if int(guess) == current_target:
        print(f"Congrats the number I was thinking of was {current_target} you Win!")
        won = True
    else:
        current_lives -= 1
        if current_lives > 0:
            print(f"Nope the number I'm thinking of isn't {guess} you have {current_lives} lives remaining try again!")
        else:
            print(f"Oh no you ran out of lives the number I was thinking of was {current_target}")
    return current_lives, won

def play_again():
    """Asks the user if they'd like to replay the game"""
    response = str(input("Would you like to play again type 'y' for yes 'n' for no\n"))
    response = input_validator(response, "replay")
    if response == "y":
        return False
    elif response == "n":
        return True

leave = False
while not leave:
    target, lives = game_setup()
    while lives > 0:
        lives, won = guess(lives, target)
        if won:
            leave = play_again()
            break
    if lives == 0:
        leave = play_again()

