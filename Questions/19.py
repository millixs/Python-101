# Program to create a Number Guessing Game

# EXPLANATION : -
# The program starts by importing the random module to generate a random number within a range using 'random.randint(lowest_num,
# highest_num)' which ensures that the chosen number is unpredictable and includes both endpoints of the range. A variable guesses
# is initialized to keep track of the number of attempts, and a boolean flag Is_running controls the main loop of the game.The game
# uses a while loop to repeatedly prompt the user for input until the correct number is guessed. The input() is first checked using
# .isdigit() to ensure the user has entered a valid number & not text or special characters — this is a good input validation approach
# to avoid crashes or logical errors. If the guess is a number, it's converted to an integer and compared against the generated answer.
# Game provides feedback like "Too high!" or "Too low!" to guide the user. If the guess is outside the valid range, the program reminds
# the user to stay within bounds. Upon a correct guess, the game displays a congratulatory message along with the no. of attempts taken
# and exits the loop by setting Is_running to False.

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
Is_running = True

print("-------NUMBER-GUESSING-GAME-------")
print(f"Select a number between {lowest_num} and {highest_num}")

while Is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():  # Return True if the string is a digit string, False otherwise.
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"\nCORRECT! The answer was {answer}")
            print(f"Number of Guesses: {guesses}")
            print("----------------------------------")
            Is_running = False

    else:
        print("INVALID GUESS!")
        print(f"Please select a number between {lowest_num} and {highest_num}")
