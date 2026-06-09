# Program to validate user input
# 1. Must not exceed 12 characters.
# 2. Must not contain spaces.
# 3. Must contain only letters (no digits or special characters).

username = input("Enter your username: ").strip()

if len(username) > 12:  # len() checks the number of characters
    print("The username can't be more than 12 characters!")

elif " " in username:  # Checking for spaces using 'in' (alternative: .find() != -1)
    print("The username can't contain spaces!")

elif not username.isalpha():  # .isalpha() ensures only letters are allowed (no digits/special characters)
    print("The username can't contain digits or special characters!")

else:
    print(f"Welcome {username}!")
