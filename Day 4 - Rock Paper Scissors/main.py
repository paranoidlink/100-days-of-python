import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("Please choose either 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)

if player_choice == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("You tied!")
    elif computer_choice == 1:
        print(paper)
        print("Paper covers rock You Lose!")
    else:
        print(scissors)
        print("Rock blunts scissors You Win!")
elif player_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(rock)
        print("Paper covers rock You Win!")
    elif computer_choice == 1:
        print(paper)
        print("You tied!")
    else:
        print(scissors)
        print("Scissors cuts paper You Lose!")
elif player_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print(rock)
        print("rock blunts scissors You Lose!")
    elif computer_choice == 1:
        print(paper)
        print("Scissors cuts paper You Win!")
    else:
        print(scissors)
        print("You Tied!")
else:
    print("Invalid Input Error")