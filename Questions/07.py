# Python Calculator Program

operator = (input("Enter the operator you would like to use (+ - * / % or x for multiplication): ").strip().lower())

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Allow 'x' or 'X' as multiplication
if operator == "x":
    operator = "*"

result = None

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
elif operator == "%":
    if num2 == 0:
        print("Error: Modulo by zero is not allowed!")
    else:
        result = num1 % num2
else:
    print("INVALID OPERATOR ENTERED")

# Print result if a valid operation was performed
if result is not None:
    print("Result:", round(result, 3))
