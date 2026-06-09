# While-loop: Executes some code WHILE a condition remains true
# - Unlike an if statement, which executes once if the condition is true,
#   a while loop keeps executing as long as the condition is satisfied.
# - It can be **potentially infinite** if not handled properly.
# - Useful for **validating user input** by repeatedly prompting until valid data is provided.
# - Proper indentation is crucial; incorrect indentation may cause errors.

# Difference between if statement and while loop:
# - `if` statement executes **once** if the condition is true.
# - `while` loop executes **repeatedly** as long as the condition remains true.


# Example 1: Ensuring user enters a valid name (input validation)
name = input("Enter your name: ")
while name == "":  # Loop continues while name is empty
    print("You did not enter your name")
    name = input("Enter your name: ")  # Overwrites the previous variable's value
print(f"Hello {name}\n")  # Executes after a valid name is entered

# Example 2: Ensuring age is not negative (input validation)
age = int(input("Enter your age: "))
while age < 0:  # Loop continues while age is negative
    print("Age can't be negative")
    age = int(input("Enter your age: "))  # Overwrites the previous variable's value
print(f"You are {age} years old\n")  # Executes when a valid age is entered

# Example 3: Taking multiple user inputs until they choose to quit
food = input("Enter a food you like (q to quit): ")
while not food == "q":  # Loop continues until the user enters 'q'
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")  # Overwrites previous value
print("Goodbye!\n")  # Executes when user quits

# Example 4: Ensuring number is within a valid range
num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:  # Loop continues while input is out of range
    print(f"{num} is not valid")
    num = int(input("Enter another number between 1 - 10: "))  # Overwrites previous value
print(f"Your number is {num}\n")  # Executes when a valid number is entered
