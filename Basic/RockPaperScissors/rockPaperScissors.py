import random
import sys

print("ROCK, PAPER, SCISSORS !!!")
# These variables keep track of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # Main game loop.
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True: # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit()
        if playerMove in ['r', 'p', 's']: # More concise way to check for valid input
            break
        print("Type one of r, p, s, or q.")
        
    # Display what player chose:
    if playerMove == "r":
        print("ROCK vs... ")
    elif playerMove == "p":
        print("PAPER vs... ")
    elif playerMove == "s":
        print("SCISSORS vs...") # Corrected spelling

    # Display what computer chose.
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's' # Assign computerMove for 's' (scissors)
        print("SCISSORS")
    
    # Display & record the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties+=1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print("You win!")
        wins+=1
    else: # If it's not a win or a tie, it must be a loss
        print("You lose!")
        losses+=1