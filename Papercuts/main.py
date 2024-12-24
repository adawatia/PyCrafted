import random as rm
import pyfiglet
from colorama import Fore
import os

"""
    1. Add ASCII Art
    2. Add Scoreboard
"""
title = pyfiglet.figlet_format("PaperCuts",font='larry3d')
print(Fore.BLUE + title)
player = None
choices = ("rock","paper","scissors")
computer = rm.choice(choices)
while player not in choices:
    player = input("Rock,Paper or Scissors?: ").lower()
    
if player == computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")
elif player == choices[0]:
    if computer == choices[1]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Lose!")
    elif computer == choices[2]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Win!")
elif player == choices[1]:
    if computer == choices[0]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Win!")
    elif computer == choices[2]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Lose!")
elif player == choices[2]:
    if computer == choices[0]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Lose!")
    elif computer == choices[1]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Win1")