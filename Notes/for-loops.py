# For-loop: Executes a block of code a fixed number of times
#          We can iterate over a range, string, sequence, etc.
# Syntax: for x in range(start, stop, step):
#         -> 'x' is a counter that changes in each iteration

# Difference between For and While loops?
# - For loops are generally used when we know how many times we want to iterate.
# - While loops are better when the number of iterations is unknown, like when waiting for valid user input.


# Example 1: Basic for-loop to print numbers from 1 to 10
for x in range(1, 11):  # Iterates from 1 to 10 (11 is exclusive)
    print(x)
print()

# Example 2: Printing a countdown along with a message after exiting the loop
for y in reversed(range(1, 11)):  # Iterates from 10 down to 1
    print(y)
print("HAPPY NEW YEAR!!")  # Printed after the loop ends
print()

# Example 3: Using a step value to print every 3rd number from 1 to 10
for x in range(1, 11, 3):  # Start at 1, step by 3 until 10
    print(x)
print()

# Example 4: Iterating over a string (useful for parsing characters)
# "Parsing" means reading and processing each part of something one by one.
# In this case, we are taking each character in the credit_card string one by one and printing it.
credit_card = "5129-6708-0085-1980"
for x in credit_card:  # 'x' holds the current character in each iteration
    print(x)
print()

# Continue Keyword: Skips a particular iteration and moves to the next
# Syntax: continue
for x in range(1, 21):
    if x == 13:  # If x is 13, skip this iteration
        continue  # Moves to the next iteration without printing 13
    print(x)
print()

# Break Keyword: Terminates the loop entirely when a condition is met
# Syntax: break
for x in range(1, 21):
    if x == 13:  # If x is 13, exit the loop immediately
        break  # Stops execution, so numbers after 12 won’t print
    print(x)
print()
