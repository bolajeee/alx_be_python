# This script creates a simple number guessing game using match-case statements in Python.
import random

#Let play = "yes" intitially
play = "yes"

#loop the game
while play == "yes":
    #generate random number
    secret_number = random.randint(1,10)

    # initialize guess count
    guess_count = 0

    while True:
        try:
            #Promt user for input
            guess = int(input("Guess a number between 1 and 10: "))
            # Increment of the guess count
            guess_count += 1
        except:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue


        #Check user guess
        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it in {guess_count} guesses!")
                break
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
            case _ if guess > secret_number:
                print("“Oops, your guess is a bit high. Try again!")
            case _:
                print("Invalid input. Please enter a number between 1 and 10.")

        # Ask if the user wants to play again
        play = input("Do you want to play again? (yes/no): ").lower()
        if play not in ["yes", "no"]:
            play = input("Invalid input. Please enter 'yes' or 'no': ").lower()

print("Thanks for playing! Goodbye!")