# function = A block of reusable code designed to perform a specific task.
#            Use the 'def' keyword to define a function, followed by a unique function name and parentheses ():
# Syntax: def function_name():
# Indent the code inside the function body
# Place () after the function name to invoke/call it.

# Example 1:-
# The Noob Way:
# A simple function to demonstrate basic code reusability without using parameters
def happy_birthday():
    print("Happy Birthday Milli!")
    print("You are 20 years old!")
    print()
    print("Happy Birthday Donut!")
    print("You are 7 years old!")
    print()

happy_birthday()  # Invoking/calling the function

# The Pro Way:
# Functions can accept arguments/parameters inside the parentheses.
# Arguments allow us to pass data into functions to make them more flexible.
# The order/position of parameters in both function definition and function call must match.
def happy_birthday(name, age):
    print(f"Happy Birthday {name}!")
    print(f"You are {age} years old!")
    print()

# We can pass different values for each function call
happy_birthday("Milli", 20)
happy_birthday("Donut", 7)

# Example 2:-
def display_invoice(username, amount, due_date):
    print(f"Hello {username}! Your bill of amount ${amount:.2f} is due on {due_date}")

display_invoice("Shaivi", 5000, "29th March, 2025")
