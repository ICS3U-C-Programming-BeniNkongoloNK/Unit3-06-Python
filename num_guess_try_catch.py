#!/usr/bin/env python3
# Created By: Beni
# Date: March 27, 2025
# Guess the number, but with a try catch

import random

def main():

    correct_guess = random.randint(0, 9)
    valid_input = False

    # As long as the user does not put in a valid input, this code will repeat
    while not valid_input:
        # Gets users guess
        guess_string = input("Pick a number between 0-9: ")
    # Check if guess(as a string) can be converted to a integer
        try:
        # If it can be converted
            guess_int = int(guess_string)
            valid_input = True
            if guess_int == correct_guess:
                print("You got lucky this time!")
            else:
                print("See I told you you wouldn't get it. The number was {}!".format(
                    correct_guess))

        except Exception:
                # If it cannot be converted, try inputting again
                print("That is not a valid input, try again")
        
        finally:
        # After try catch is done being executed print "thank you for playing"
            print("Play again soon")

if __name__ == "__main__":
    main()