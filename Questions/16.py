# Program to create a 2D keypad, like the one typically found on a phone

# NOTE :-
# Since we want the numbers arranged in a specific order, we cannot use sets {} (which are unordered)
# We can use either lists or tuples for this structure
# Tuples are generally faster and more memory-efficient than lists, so we prefer them here

num_pad = ((1, 2, 3),  # A 2D tuple containing all the numbers and symbols typically found on a numpad
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))  # The '*' and '#' symbols must be in quotes to be treated as characters

# To format the output like an actual numpad, we need to use a nested for-loop
for row in num_pad:
    for element in row:
        print(element, end=" ")  # end="space" ensures that all the elements get printed in the same line
    print()  # Moves to the next line after each row is printed, to make our output look exactly like a numpad
