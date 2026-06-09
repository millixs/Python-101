# if Statement: It is one of the fundamental decision-making statements.
#               Executes a block of code only if the specified condition is true.
#               The `elif` (else-if) statement checks additional conditions if the first condition is false.
#               The `else` statement executes a block of code if none of the previous conditions are met.
#               The order of conditions is crucial to ensure accurate execution.

"""
Syntax:
if condition_1_Is_true:
    print("Execute condition 1")
elif condition_2_Is_true:
    print("Execute condition 2")
else:
    print("Execute condition 3")
"""

# Example Program 1: Checking age for eligibility
age = int(input("Enter your age: "))

if age >= 100:
    print("You should've been dead by now!!")
elif age >= 18:
    print("You are eligible to sign up!!")
elif age < 0:
    print("You haven't been born yet!!")
else:
    print("You must be 18+ to sign up!!")


# Example Program 2: Simple user response-based decision
response = input("\nWould you like a slice of pizza? (y/n): ").strip().lower()
# .strip() → Removes leading and trailing spaces (e.g., " y " becomes "y").
# .lower() → Converts input to lowercase (e.g., "Y" becomes "y").

if response == "y":
    print("Here, enjoy your slice of pizza!!")
elif response == "n":
    print("Alright, no pizza for you then!")
else:
    print("Invalid response! Please enter 'y' or 'n'.")
