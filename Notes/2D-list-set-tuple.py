# 2D: Two-Dimensional
# A 2D collection (list) is just a collection (list) made up of other collections (lists)
# Example: 2d_list = [list1, list2, list3]
# It's really useful when we need a grid or matrix-like structure for storing data—similar to an Excel spreadsheet.
# In Python, a 2D collection can also be a list of tuples, a tuple of tuples, a tuple of sets, etc.

meats = ["chicken", "beef", "fish"]
fruits = ["kiwi", "mango", "orange"]
vegetables = ["broccoli", "kale", "cabbage"]

groceries = [meats, fruits, vegetables]  # groceries is a 2D list containing other lists (meats, fruits, vegetables)
print(groceries)  # Prints all 3 lists within groceries in one line, separated by commas
print(groceries[0])  # Prints the 'meats' list, which is at index [0] in groceries
print(groceries[1][0])  # Prints 'kiwi', the element at index [0] in 'fruits', which is at index [1] in groceries

# Using a single for-loop, we can iterate over the rows (i.e., inner lists) in a 2D list
# Each individual list gets printed on a separate line
for collection in groceries:
    print(collection)
print()

# When declaring a 2D list, it's not necessary to name each of the inner (1D) lists separately
groceries_2 = [["lamb", "beef", "pork"],
               ["apple", "banana", "kiwi"],
               ["carrot", "turnip", "potato"]]
print(groceries_2)

# Using a nested for-loop, we can iterate over every individual element in the 2D list
# Each element gets printed on a separate line
for collection in groceries_2:
    for food in collection:
        print(food)
