import random
import art
from random import choice

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
def deck_builder(deck):
    """Uses a Dictionary to create a standard deck of cards"""
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8 , 9, 10, "King", "Queen", "Jack"]
    for suit in suits:
        deck[suit] = cards
    return deck

def card_to_score_converter(card):
    """Converts named cards to a numerical score"""
    named_cards = {
        "King" : 10,
        "Queen" : 10,
        "Jack" : 10,
        "Ace" : 11,
    }
    value = named_cards[card]
    return value

def ace_converter(current_score):
    """Converts the score of an Ace to 1 where needed"""
    if current_score + 11 > 21:
        ace_score = 1
    else:
        ace_score = 11
    return ace_score

def get_current_score(hand):
    """Tallies up the current cards in a hand to get the score"""
    score = 0
    for card in hand:
        if card == 11:
            ace_converter(card)
        score += card
    return score

def bust_calculator(current_score):
    """Figures out if the current score is over 21 and returns a bool for if that score would be bust"""
    if current_score > 21:
        return True
    else:
        return False

def blackjack_calculator(current_score):
    """Determines if blackjack is in hand and returns a bool representing this"""
    if current_score == 21:
        return True
    else:
        return False

def draw(deck, hand):
    """Draws a card from a deck into a hand"""
    suit = random.choice(suits)
    value = random.randint(0, 12)

    card_drawn = deck[suit][value]
    print(f"{card_drawn} of {suit}")
    if isinstance(card_drawn, str):
        card_drawn =card_to_score_converter(card_drawn)
    hand.append(card_drawn)
    return hand

def setup (deck, player_hand, dealer_hand):
    """Draws 2 cards for the player and one to the dealer and reveals them"""
    deck = deck_builder(deck)
    print("You have:")
    player_hand = draw(deck, player_hand)
    player_hand = draw(deck, player_hand)
    print("Dealer has:")
    dealer_hand = draw(deck, dealer_hand)
    return deck, player_hand, dealer_hand

def input_validator(usr_input, type):
    """Checks to make sure the inputs can be read by the program"""
    valid_inputs_hit_stand = ["hit", "stand"]
    valid_inputs_yes_no = ["y", "n"]
    if type == "hit_stand":
        while usr_input not in valid_inputs_hit_stand:
            usr_input = input("Invalid input detected please enter a valid input either 'hit' or 'stand'\n")
        return usr_input
    elif type == "yes_no":
        while usr_input not in valid_inputs_yes_no:
            usr_input = input("Invalid input detected please enter a valid input either 'y' or 'n'\n")
        return usr_input

def player_turn(deck):
    """Does the initial setup for the game and contains a loop for the players actions on their turn"""
    player_hand = []
    dealer_hand = []
    deck, player_hand, dealer_hand = setup(deck, player_hand, dealer_hand)
    score = get_current_score(player_hand)
    bust = bust_calculator(score)
    stand = False
    blackjack = blackjack_calculator(score)
    if blackjack:
        print("You have blackjack!")
        return "blackjack", dealer_hand, deck
    while not bust and not stand:
        choice = input(f"Your current total is {score} would you please type 'hit' or 'stand' to continue\n")
        choice = input_validator(choice.lower(), "hit_stand")
        if choice.lower() == "stand":
            stand = True
        if choice.lower() == "hit":
            print("You Draw:")
            draw(deck, player_hand)
            score = get_current_score(player_hand)
            bust = bust_calculator(score)
            if bust:
                print(f"You have {score} you go bust!")
            elif score == 21:
                print(f"You have {score} auto standing")
                stand = True
    if not bust:
        return score, dealer_hand, deck
    elif bust:
        return "bust", dealer_hand, deck


def dealer_turn(deck, dealer_hand, player_score):
    """Automates the dealers turn based on the players score the dealer will attempt to stand at 18"""
    player_score = bust_and_blackjack_converter(player_score)
    print("Dealer Draws:")
    draw(deck, dealer_hand)
    score = get_current_score(dealer_hand)
    print(f"Dealer has: {score}")
    bust = bust_calculator(score)
    stand = False
    won = False
    blackjack = blackjack_calculator(score)
    if blackjack:
        print("Dealer has blackjack!")
        return "blackjack"
    while not bust or not stand or not won or score >= 18:
        print("Dealer Draws:")
        draw(deck, dealer_hand)
        score = get_current_score(dealer_hand)
        bust = bust_calculator(score)
        if score > player_score and not bust:
            won = True
            return score
        elif bust:
            print(f"Dealer has {score} and goes bust")
            return "bust"
        elif score >= 18:
            print(f"Dealer has {score} and stands")
            return score
        else:
            print(f"Dealer has {score}")

def bust_and_blackjack_converter(score):
    """Converts scores with the string bust or blackjack into a numerical value that can be read by the program"""
    conditions = {
        "bust" : 22,
        "blackjack" : 23
    }
    if isinstance(score, str):
        return conditions[score]
    else:
        return score

def winner_check(player_score, dealer_score):
    """Checks to see who won the game"""
    player_score = bust_and_blackjack_converter(player_score)
    dealer_score = bust_and_blackjack_converter(dealer_score)

    if player_score == 22 and dealer_score == 22:
        print("Both bust you Tie!")
    elif player_score == 23 and dealer_score == 23:
        print("both have blackjack you Tie!")
    elif player_score == 22 and dealer_score < 22:
        print("You went bust and the dealer didn't you Lose!")
    elif player_score < 22 and dealer_score == 22:
        print("Dealer went bust and you didn't you win!")
    elif player_score == 23 and dealer_score < 23:
        print("You win with blackjack!")
    elif player_score < 23 and dealer_score == 23:
        print("Dealer wins with blackjack! you lose!")
    elif player_score > dealer_score:
        print(f"You have {player_score} against the dealers {dealer_score} you win!")
    else:
        print(f"You have {player_score} against the dealers {dealer_score} you lose!")

deck = {}
leave = False


while not leave:
    print(art.logo)
    player_score, dealer_hand, deck = player_turn(deck)
    dealer_score = dealer_turn(deck, dealer_hand, player_score)
    winner_check(player_score, dealer_score)
    leave_check = input("Would you like to play again type 'y' for yes 'n' for no\n")
    leave_check = input_validator(leave_check.lower(), "yes_no")
    if leave_check.lower() == "n":
        leave = True
