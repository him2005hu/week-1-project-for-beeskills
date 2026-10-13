import random

print("Welcome to The Perfect Guess Game!")

# Generate a random number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0

while True:

    guess = int(input("Guess a number between 1 and 100: "))

    attempts += 1

    if guess < secret_number:
        print("Higher number please.")

    elif guess > secret_number:
        print("Lower number please.")

    else:
        print("Congratulations! You guessed the correct number.")
        print("The number was:", secret_number)
        print("Total attempts:", attempts)
        break