# Program to create a Shopping Cart in Python

# EXPLANATION : -
# The program initializes three variables: an empty list foods to store the names of food items,
# an empty list prices to store their corresponding prices, and a total variable set to zero to
# keep track of the total cost. It then enters an infinite while loop, continuously prompting the
# user to enter a food item. If the user inputs "q" (case-insensitive), the loop breaks, ending
# input collection. Otherwise, the program asks for the price of the entered food item, converts
# it to a floating-point number, and adds both the food name and price to their respective lists.
# After exiting the loop, the program prints a formatted shopping cart, displaying all the food
# items in a single line. It then iterates through the prices list, adding each price to the
# total variable. Finally, it prints the total amount payable with two decimal places.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("----- YOUR CART -----")

for food in foods:
    print(food, end="  ")

for price in prices:
    total += price

print()
print(f"Total Amount Payable: ${total:.2f}")
