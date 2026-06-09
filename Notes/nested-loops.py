# Nested Loops: A loop inside another loop (outer loop → inner loop).
# Proper indentation is crucial for correct execution.

# Type 1: While-loop inside another while-loop
# WARNING: This creates an infinite loop, so do not run it!
x = 1
y = 1
while x > 0:  # Outer while-loop
    while y > 0:  # Inner while-loop
        print("Do Something!")
print()

# Type 2: For-loop inside a while-loop
# WARNING: This also creates an infinite loop, so do not run it!
while x > 0:  # Outer while-loop
    for y in range(9):  # Inner for-loop
        print("Do Something!")
print()

# Type 3: While-loop inside a for-loop
# WARNING: This too results in an infinite loop, so do not run it!
for x in range(3):  # Outer for-loop
    while y > 0:  # Inner while-loop
        print("Do Something!")
print()

# Type 4: For-loop inside another for-loop (Proper Example)
# This executes without an infinite loop
for x in range(3):              # Outer loop runs 3 times (x = 0, 1, 2)
    for y in range(1, 10):      # Inner loop iterates from 1 to 9
        print(y, end="")        # Prints numbers 1 to 9 on the same line for each iteration of the outer loop
    print()                     # Moves to a new line after each outer loop iteration
