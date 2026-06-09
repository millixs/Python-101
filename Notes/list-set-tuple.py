# Collection: A single "variable" used to store multiple values.
#  List  = [] Ordered and mutable (changeable). Allows duplicate values.
#  Set   = {} Unordered and immutable (unchangeable), but elements can be added/removed. No duplicate values.
#  Tuple = () Ordered and immutable. Allows duplicate values. Faster than lists.

# Normal Variable Example:
fruit = "mango"  # A variable named 'fruit' storing a single string value "mango"
print(fruit)  # Output: mango

# Collection 1: LIST []
fruits = ["mango", "apple", "banana", "orange", "kiwi", "cherry"]
# A variable named 'fruits' storing a LIST [] of strings (multiple fruit names)

print(fruits)  # Prints the entire list within square brackets
print(fruits[3])  # Access an element using its index (indexing starts from 0)
print(fruits[2:4])  # Slice notation: prints elements from index 2 to 3 (end index is excluded)
print(fruits[0:5:2])  # Prints elements from index 0 to 4 with a step of 2
print(fruits[::-1])  # Prints the list in reverse order using a step of -1

print(len(fruits))  # Prints the total number of elements in the list
print("apple" in fruits)  # Checks if "apple" is present in the list (returns True/False)

# Lists are mutable, meaning elements can be modified after creation.
fruits[2] = "melon"  # Changing "banana" to "melon"

# List operations:
fruits.append("pineapple")  # Adds "pineapple" to the end of the list; don't use print along with it else it will return 'None'
fruits.remove("kiwi")  # Removes "kiwi" from the list; don't use print along with it else it will return 'None'
fruits.insert(0, "grapes")  # Inserts "grapes" at index 0; don't use print along with it else it will return 'None'
fruits.sort()  # Sorts the list in ascending (alphabetical) order; don't use print along with it else it will return 'None'
fruits.reverse()  # Reverses the list order; use .sort() first for reverse alphabetical order; don't use print along with it else it will return 'None'
print(fruits.index("apple"))  # Returns the index of "apple"
print(fruits.count("banana"))  # Counts occurrences of "banana" in the list
fruits.clear()  # Clears all elements from the list; don't use print along with it else it will return 'None'

# Iterating over a list:
for fruit in fruits:  # We can name our counter anything hence: x -> fruit for better readability
    print(fruit, end="...")  # Prints each element separated by "..."


# Collection 2: SET {}
cars = {"Audi R8", "BMW M4", "Ford Mustang", "Toyota Supra", "Tesla Model 3", "Lamborghini Huracán"}
# A SET {} is an unordered collection of unique elements.

print(len(cars))  # Prints the number of elements in the set
print("Audi R8" in cars)  # Checks if "Audi R8" is present in the set (returns True/False)

# Set operations:
cars.add("Porsche 911")  # Adds an element to the set; don't use print along with it else it will return 'None'
cars.remove("BMW M4")  # Removes "BMW M4" from the set; don't use print along with it else it will return 'None'
print(cars.pop())  # Removes and returns a random element from the set
cars.clear()  # Clears all elements from the set; don't use print along with it else it will return 'None'
print(cars)  # # Since a set {} is unordered, so elements appear in a random order each time it's printed. Indexing isn't possible as set elements don’t have fixed positions.

# Iterating over a set:
for car in cars:
    print(car, end="...")


# Collection 3: TUPLE ()
bikes = ("Yamaha YZF-R1", "Kawasaki Ninja H2", "BMW S1000RR", "Suzuki Hayabusa", "Honda CBR1000RR-R")
# A TUPLE () is an ordered but immutable collection.

print(bikes)  # Prints the entire tuple within round brackets
print(len(bikes))  # Prints the number of elements in the tuple
print("Suzuki Hayabusa" in bikes)  # Checks if "Suzuki Hayabusa" is present in the tuple (returns True/False)
print(bikes.count("Yamaha YZF-R1"))  # Counts occurrences of "Yamaha YZF-R1" in the tuple

# Iterating over a tuple:
for bike in bikes:
    print(bike, end="...")

