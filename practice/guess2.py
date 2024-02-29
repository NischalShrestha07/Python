import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    while True:
        # Ask the user to guess the number
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try guessing higher.")
        else:
            print("Too high! Try guessing lower.")

# Call the function to start the game
guess_number()
