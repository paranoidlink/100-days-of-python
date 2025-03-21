import art
print(art.logo)
print("Welcome to the secret auction program")
#Ask the user for input
def user_input():
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid £"))
    more_bidders = input("Are there any other bidders? type 'yes' or 'no'.\n")
    return name, bid, more_bidders

name, bid, more_bidders = user_input()
#Save data into dictionary {name: price}
auction = {
    name : bid,
}
#Check Whether new bids need to be added
while more_bidders == "yes":
    print("\n" * 20)
    name, bid, more_bidders = user_input()
    auction[name] = bid
#Compare bids in dictionary
highest_bid = 0
highest_bidder = ""
for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid = auction[bidder]
        highest_bidder = bidder
print(f"{highest_bidder} wins the auction with a bid of £{highest_bid}")


