# Program to print a rectangle pattern based on the user inputs

rows = int(input("Enter the no. of rows: "))
columns = int(input("Enter the no. of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):           # Outer loop runs 'rows' times, controlling the number of rows
    for y in range(columns):    # Inner loop runs 'columns' times for each row, controlling the number of symbols per row
        print(symbol, end="")   # Prints the symbol on the same line for each iteration of the outer loop
    print()                     # Moves to a new line after printing all symbols in a row
