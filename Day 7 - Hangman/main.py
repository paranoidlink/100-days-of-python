import random
import hangman_words
import hangman_art

#Initial Setup
stages = hangman_art.stages
word_list = hangman_words.word_list
lives = 6
chosen_word = random.choice(word_list)
placeholder = []
for char in chosen_word:
    placeholder.append("_")

#Function to check if the game should continue or not
def game_over(display):
    if lives == 0:
        print(f"Out of Lives you Lose the correct word was {chosen_word}")
        return True
    for char in display:
        if char == "_":
            return  False
    print(f"You win the word was {str(display)}!")
    return True

#Final Setup and start the game
display = placeholder
guesses = []
print(hangman_art.logo)
print(stages[lives])
print(str(display))

#Gameplay
while not game_over(display):
    guess = input("Please guess a letter\n").lower()
    #Validate if the guess was already made and force to pick another letter if so
    for check in guesses:
        while guess == check:
            guess = input(f"You've already guessed the letter {guess} please enter a new guess\n")
    guesses.append(guess)
    #Round Setup
    correct = False
    counter = 0

    #Figure out if the Guess was correct
    for char in chosen_word:
        if char == guess:
            correct = True
            display[counter] = guess
        counter += 1
    if correct:
        print(stages[lives])
        print("Right")
        print(str(display))
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        print("Wrong")
        lives -= 1
        print(stages[lives])
        print(str(display))
        print(f"****************************{lives}/6 LIVES LEFT****************************")
