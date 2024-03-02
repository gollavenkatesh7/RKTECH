#  Task -4
#  Number Guessing


import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")

    # Set the range for the random number
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)

    # Set the maximum number of attempts
    max_attempts = 5
    attempts = 0

    print(f"\nI have selected a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Try Again! Your guess was too small.")
        else:
            print("Try Again! Your guess was too high.")

    else:
        print(f"Better Luck Next Time! The correct number was {secret_number}.")

# Run the game
guess_the_number()
