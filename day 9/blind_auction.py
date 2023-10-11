# challenge start
from logo import logo

print(logo)

info_of_biders = {}
bidding_finished = False

def find_highest_bider(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid price?: $"))
    info_of_biders[name] = bid
    next_user = input("Is there any other bider available? Type 'YES' or 'NO'. \n").lower()
    if next_user == "no":
        bidding_finished = True
        find_highest_bider(info_of_biders)
    else:
        print(f"X with the bid of X is the winner")