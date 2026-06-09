# Program to mimic a Concession Stand, like the food counters in movie theaters

# EXPLANATION :-
# The menu is stored as a dictionary, where each item (like "fries (m)" or "pizza (1sl)") is a key and its price is the value.
# An empty list called cart is used to keep track of selected items, while total stores the running total of the bill. The program
# begins by neatly displaying the menu using a for loop. Then, a 'while True:' loop is used to continuously prompt the user for input
# This structure ensures that the loop keeps running until the user decides to quit manually. Inside the loop, the user's input is
# converted to lowercase to handle case sensitivity, and if they type 'q' the loop breaks. If the entered item exists in the menu,
# (checked using the safe .get() method, which prevents errors if the key doesn’t exist) the item is added to the cart. After exiting
# the loop, the program goes through the cart list, retrieves prices using .get(), prints each selected item, & calculates the total.
# Finally, it displays the total amount to be paid)

menu = {"fries (s)": 49,
        "fries (m)": 99,
        "samosa (4)": 99,
        "pizza (1sl)": 49,
        "sandwich (2)": 99,
        "coca-cola (s)": 99,
        "coca-cola (l)": 199,
        "popcorn-salty": 199,
        "popcorn-cheese": 249,
        "popcorn-caramel": 299}

cart = []
total = 0

print("------------MENU--------------")
for key, value in menu.items():
    print(f"{key:20}: Rs.{value}")
print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------- YOUR ORDER -----------")
for food in cart:
    total = total + menu.get(food)
    print(food)
print()
print(f"Total: Rs.{total}")
