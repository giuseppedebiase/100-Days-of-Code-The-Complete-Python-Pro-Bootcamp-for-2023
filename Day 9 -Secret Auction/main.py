#In a secret auction the offering of each bidder reamins unkown to the rest of the bidders until the end, when a winner is declared.
#To use this code for this purpose each participant will write their name and their offer and then pass the device to another participant.
#this code exercise was written on replit, a browser IDE
from replit import clear

import art
print(art.logo)
print("Welcome to the secret auction program.")

#creates a dictionary for the bidders where the keys are the participant's names and the values are the offerings
bidders = {}
Auction = True
while Auction == True:
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  #this line will create a set a new entry for the dictionary
  bidders[name] = bid
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ")
  #the clear function replit clears the console, in this case the next participant of the auction won't know what the previous one wrote
  clear()
  #if there are no other participant the programs stops asking for names and bids so that it can declare a winner
  if answer == "no"
    Auction = False

#in a secret auction if two winner bid the same amount than the winner is the first bidder
#the following lines (27-29) will create a list of of the bids (the values in the bidders dictionary)
list = []
for key in bidders:
  list.append(bidders[key])

#the following lines (32-36) will find the max value among the bids (32) and then check for every value in the bidders dictionary for a match (34-35), 
#when it founds one the cycle breaks (37, otherwise the winner would be the second bidder who offered the same amount) 
max_bid = max(list)
for key in bidders:
  if bidders[key] == max_bid:
    winner = key
    break

winner_offering = bidders[winner]
print(f"The winner is {winner} with a bid of ${winner_offering}.")
