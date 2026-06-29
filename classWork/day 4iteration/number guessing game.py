secret_number = 37   # The secret number to be guessed

print("Guess the secret number!")

while True:   # Loop will continue until the correct guess is made
    guess = int(input("Enter your guess: "))   # Take user input and convert to integer

    if guess == secret_number:   # Check if guess is equal to secret number
        print("Correct! You guessed the number.")
        break   # Exit the loop when the correct guess is found
    elif guess > secret_number:   # If guess is greater than secret number
        print("Too high! Try again.")
    else:   # If guess is smaller than secret number
        print("Too low! Try again.")
