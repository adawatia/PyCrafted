import random as rm
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Title
title = pyfiglet.figlet_format("PaperCuts", font='larry3d')
print(Fore.BLUE + title)

# Best of rounds
while True:
    try:
        best_of_input = input(f"{Fore.YELLOW}Best of (Default: 3): ")
        best_of = int(best_of_input) if best_of_input else 3
        if best_of <= 0 or best_of % 2 == 0:
            raise ValueError("Please enter a positive odd number.")
        break
    except ValueError as e:
        print(f"{Fore.RED}Invalid input! {e}")

# Initialize game variables
choices = {"r": "rock", "p": "paper", "s": "scissors"}
score_player, score_computer = 0, 0
rounds_played = 0

# Game loop
while rounds_played < best_of:
    # Get player's choice
    player = None
    while player not in choices:
        player = input(f"{Fore.CYAN}Rock (r), Paper (p), or Scissors (s)?: ").lower()

    # Convert short input to full choice
    player_full = choices[player]

    # Computer's choice
    computer_full = rm.choice(list(choices.values()))

    # Display choices
    print(f"\n{Fore.MAGENTA}Computer: {computer_full.capitalize()}")
    print(f"{Fore.GREEN}Player: {player_full.capitalize()}")

    # Determine winner
    if player_full == computer_full:
        print(f"{Fore.YELLOW}It's a Tie!")
    elif (player_full == "rock" and computer_full == "scissors") or \
         (player_full == "paper" and computer_full == "rock") or \
         (player_full == "scissors" and computer_full == "paper"):
        print(f"{Fore.GREEN}You Win this round!")
        score_player += 1
    else:
        print(f"{Fore.RED}You Lose this round!")
        score_computer += 1

    # Update rounds
    rounds_played += 1
    print(f"{Style.BRIGHT}Scores: {Fore.GREEN}Player {score_player} - {Fore.RED}Computer {score_computer}\n")

# Final results
print(f"{Fore.CYAN}Final Scores: {Fore.GREEN}Player {score_player} - {Fore.RED}Computer {score_computer}")
if score_player > score_computer:
    print(f"{Fore.GREEN}Congratulations! You are the winner! 🎉")
elif score_computer > score_player:
    print(f"{Fore.RED}Sorry! The computer wins this time! 🤖")
else:
    print(f"{Fore.YELLOW}It's an overall tie! Well played! 🤝")
