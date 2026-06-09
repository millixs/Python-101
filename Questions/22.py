# Program to create a Random Password Generator

import random
import string

characters = string.ascii_letters + string.digits + "@"
# print(characters)     # To check all the characters we are gonna be using in our randomly generated password

password_length = int(input("Enter the Password Length: "))
password = ''.join(random.choice(characters) for _ in range(password_length))

print("Password:", password)
