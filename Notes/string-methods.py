# String Methods: Useful methods and functions that can be used on strings

name = input("Enter your name: ").strip()  # .strip() removes leading and trailing spaces
phone_no = input("Enter your phone number: ").strip()
print()

# String Length and Searching
print(len(name))  # Returns the length of the string, including spaces
print(name.find("o"))  # Returns the first occurrence index of "o", or -1 if not found
print(name.rfind("p"))  # Returns the last occurrence index of "p", or -1 if not found
print()

# String Formatting
print(name.capitalize())  # Capitalizes only the first letter, rest remain lowercase
print(name.upper())  # Converts the entire string to uppercase
print(name.lower())  # Converts the entire string to lowercase
print()

# String Validation
print(name.isdigit())  # Returns True if the string contains only digits, else False
print(name.isalpha())  # Returns True if the string contains only alphabets (no spaces)
print()

# String Manipulation
print(phone_no.count("-"))  # Counts the number of dashes ('-') in the phone number
print(phone_no.replace("-", " "))  # Replaces dashes with spaces in the output

# Get full documentation on string methods
# print(help(str))  # Prints all the string methods along with their descriptions
