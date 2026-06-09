# Variable: A container for storing a value (string, integer, float, boolean)
#           A variable behaves as if it is the value it holds.
#           Each variable should have a unique name.
#           The assignment operator '=' is used to assign values.

# Strings: A sequence of characters enclosed in single or double quotes
first_name = "Milli"
food = 'pizza'
email = "dxnut2359@fake.com"

# f-string: Used to insert variable values within a string (formatted string literals)
print(f"Hey {first_name}")
print(f"You like {food}")
print(f"Your email is {email}\n")

# Integers: Whole numbers without decimals. If enclosed in quotes, they become strings.
age = 19
year = 2005
print(f"Your age is {age}")
print(f"Your birth year is {year}\n")

# Floats: Numbers with decimal points
price = 400.79
cgpa = 8.9
distance = 5.7
print(f"Total price of the item: ${price}")
print(f"Your current CGPA is {cgpa}")
print(f"You ran {distance:.2f} km\n")  # Use(:.xf) for formatting the float to a specific number of decimal places

# Booleans: Represent True or False. The first letter must be capitalized.
is_student = True
for_sale = False
print(f"Are you a student?: {is_student}")
print(f"Is your apartment on sale?: {for_sale}\n")

# Example of boolean usage in an if statement
is_online = True
if is_online:
    print("Milli is online")  # Executes if is_online is True
else:
    print("Milli is offline")  # Executes if is_online is False
