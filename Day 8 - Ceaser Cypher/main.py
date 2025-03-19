from typing import final
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, direction):
    #Initial Setup
    new_text = []

    for char in original_text.lower():
        #Add any spaces or special characters without changing them
        if char in special_characters:
            new_text.append(char)
            continue
        #Check if we're encoding or decoding
        if direction == "decode":
            adjusted_position = alphabet.index(char) - shift_amount
            new_text.append(alphabet[adjusted_position])
            continue
        #Check if the number would go out of bounds after shifting and loop back around the alphabet if so
        if alphabet.index(char) + shift_amount > 25:
            adjusted_position = (shift_amount - 26) + alphabet.index(char)
        else:
            adjusted_position = alphabet.index(char) + shift_amount
        #add the letter from the alphabet list at the index of the shifted position into the new text list
        new_text.append(alphabet[adjusted_position])
    #Convert the new text list back into a string and print
    final_text = "".join(new_text)
    print(final_text)

caesar(text, shift, direction)
restart = input("Would you like to run the decoder again? type y for yes n for no\n")
while restart == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Would you like to run the decoder again? type y for yes n for no\n")