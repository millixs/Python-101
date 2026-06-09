# Conditional Expression (Ternary Operator):-
# A one-line shortcut for an if-else statement.
# It evaluates a condition and returns one of two values based on the result.
# Syntax: "value_if_true" if condition else "value_if_false"

# Example 1: Checking if a number is positive or negative, and even or odd
num = int(input("Enter a number: "))
print(f"{num} is Positive" if num >= 0 else f"{num} is Negative")
print(f"{num} is Even\n" if num % 2 == 0 else f"{num} is Odd\n")

# Example 2: Finding the larger of two numbers
a, b = 98, 56
print(f"Larger number: {a if a > b else b}\n")

# Example 3: Checking if a person is an adult or child
age = int(input("Enter your age: "))
print("ADULT\n" if age >= 18 else "CHILD\n")

# Example 4: Assigning access level based on user role
user_role = "admin"
access_level = "Full-Access" if user_role == "admin" else "Limited-Access\n"
print(access_level)
