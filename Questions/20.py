# Program to create a Rock Paper Scissors Game

# EXPLANATION : -
# This program utilizes the random module to allow the computer to randomly choose between "rock", "paper", and "scissors" from a
# predefined tuple called options. A while loop keeps the game running until the user chooses to quit, controlled by the boolean
# variable running. Inside the loop, the program first sets player to None, then asks the user to input their choice. To ensure valid
# input, a nested while loop checks whether the player's input is among the allowed options. It also uses .strip().lower() to handle
# any extra spaces or case mismatches—making the program more user-friendly.Once both the player and computer have valid choices, the
# program compares them using a series of conditional statements. If both choose the same option, it's a tie. If the player's choice
# beats the computer's according to the rules of the game, a win is declared. Otherwise, the player loses. After the result is printed,
# the program asks the player whether they want to play again. This is handled in two ways—Method 1 ("noob") explicitly checks for "y"
# and sets running accordingly. Method 2 ("pro") does this more concisely by directly evaluating the input in a single line. If the
# player does not enter "y", running is set to False, ending the loop. Finally, a goodbye message is printed to thank the player.

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        print("---------------------------------------------------")
        player = input("Enter your choice (rock, paper, scissors): ").strip().lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    # METHOD - 1: (noob)
    # play_again = input("Wanna play again? (y/n):  ").strip().lower()
    # if not play_again == "y":
    #     running = False

    # METHOD - 2: (pro)
    if not input("Play again? (y/n): ").strip().lower() == "y":  # If the player enters anything other than 'y', the game will stop
        running = False

print("---------------------------------------------------")
print("Thanks for playing!!!")
