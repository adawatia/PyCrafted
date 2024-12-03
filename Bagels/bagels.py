import random

NUM_DIGITS = 5
MAX_GUESSES = 12

def main():
    print(""" Bagels, a deductive logic game.
          By Al Sweigart.
          
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:    That means:
            Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct and in the right position.
            Bagels       No digit is correct.
            
            For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.'''.format(NUM_DIGITS))
          """)
    
    while True: #Main loop
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to it. ")
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or guess.isdecimal():
                print(f"Guess # {numGuesses}")
                guess = input('>')
                