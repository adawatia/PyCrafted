import random  # Import random module for generating secret number

# Game configuration constants
NUM_DIGITS = 3  # Number of digits in the secret number
MAX_GUESSES = 10  # Maximum number of guesses allowed


def main():
    # Print game instructions explaining the rules and clue system
    print(f"""Bagels, a deductive logic game.
By Al Sweigart.L

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""")

    while True:  # Outer loop for multiple game rounds
        # Generate a secret number with no repeated digits
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:  # Inner loop for guess attempts
            # Validate user input: ensure it's a decimal number of correct length
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}")
                guess = input('> ')

            # Get and display clues for the current guess
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            # Check for correct guess or max guesses reached
            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        # Ask if player wants to play again
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_num():
    # Create a list of digits 0-9 and shuffle them
    # This ensures no repeated digits in the secret number
    numbers = list(str(i) for i in range(10))
    random.shuffle(numbers)
    # Take the first NUM_DIGITS digits to form the secret number
    return ''.join(numbers[:NUM_DIGITS])


def get_clues(guess, secret_num):
    # If guess is exactly correct, return winning message
    if guess == secret_num:
        return "You got it!"

    # List to store clues for the guess
    clues = []

    # Check each digit in the guess
    for i in range(len(guess)):
        # If digit is in the correct position
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        # If digit is in the secret number but wrong position
        elif guess[i] in secret_num:
            clues.append("Pico")

    # If no clues, no digits are correct
    if not clues:
        return "Bagels"
    else:
        # Sort clues to ensure consistent output
        clues.sort()
        return " ".join(clues)


# Ensure the game only runs if the script is directly executed
if __name__ == "__main__":
    main()