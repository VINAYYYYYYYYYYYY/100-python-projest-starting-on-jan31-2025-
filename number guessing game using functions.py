import random

def guess_the_number():
    number = random.randint(1, 100)  # Generate a random number
    attempts = 5  # Number of allowed guesses

    print("Welcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    for _ in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess > number:
            print("Go lower!")
        elif guess < number:
            print("Go higher!")
        else:
            print("How the F you got it bro!")
            return  # Exit the function when the guess is correct

    print(f"You're out of attempts! The number was {number}.")

# Call the function to start the game
guess_the_number()