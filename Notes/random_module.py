# The random module in Python provides access to a variety of useful functions for generating random values.
# It is especially useful in projects involving randomness or unpredictability—like games (e.g., number-guessing, rock-paper-scissors).
# I have even used it in my QuoteAPI project in order to display a random quote.
# It is a built-in module in Python, so no additional installation is required.

import random

low = 1
high = 100

print(random.randint(1, 6))  # Returns a random integer between 1 and 6 (inclusive of both endpoints)
print(random.randint(low, high))  # We can also enter variable names (containing numbers) in place of integers

print(random.random())  # Returns a random floating-point number in the range [0.0, 1.0)

options = ("rock", "paper", "scissors")
print(random.choice(options))  # Randomly selects and returns an element from a non-empty sequence

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)  # Shuffles the elements of the list in place. It modifies the original list and returns None, so the list has to be printed separately
print(cards)
