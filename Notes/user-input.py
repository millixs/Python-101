# input(): A function that prompts the user to enter data
#          We can assign the input data entered by the user to a variable, to perform further operations on it
#          Returns/Stores the entered data as a string
#          Enter the prompt within double quotes

name = input("Enter your name: ")
age = int(input("Enter your age: "))
age += 1
print(f"Hey {name}")
print("Happy Birthday!!")
print(f"You are {age} years old")
