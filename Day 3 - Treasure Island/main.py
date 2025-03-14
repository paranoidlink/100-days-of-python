print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Would you like to go Left or Right\n")
if direction.lower() == "left":
    swim = input("You go to the left and find a river would you like to swim across or wait?\n")
    if swim.lower() == "wait":
        door = input("As you wait you are teleported ino a room with three doors, do you go through the Blue door the Red door or the Yellow door?\n")
        if door.lower() == "yellow":
            print("Congrats you found the treasure!")
        elif door.lower() == "blue":
            print("As you go through the blue door a starving tiger jumps on you and eats you Game Over!")
        elif door.lower() == "red":
            print("As you go through the red door you notice the door quickly locks behind you and the room ignites you burn to death Game Over!")
        else:
            print("You decide to not go through any of the doors and slowly starve to death Game Over!")
    else:
        print("You decide to try and swim across the river but get attacked by a trout halfway through and drown Game Over!")
else:
    print("You take one step to the right and find yourself falling down a bottomless pit Game Over!")