# Dictionary = A collection of {key: value} pairs. Dictionaries are ordered (as of Python 3.7+), changeable (mutable), and do not allow duplicate keys.

capitals = {
    "Japan": "Tokyo",
    "Russia": "Moscow",
    "India": "New Delhi",
    "Australia": "Sydney"
}

print(capitals.get("Japan"))  # Returns the value associated with the specified key; returns None if the key doesn't exist. Useful to safely check if a key is present.

if capitals.get("India"):  # The .get() method can also be used in conditional statements to check if a key exists
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin", "China": "Beijing"})  # Adds new {key: value} pairs to the dictionary
capitals.update({"India": "Goa"})  # Modifies or Updates the value of an existing key if it already exists
print(capitals)

capitals.pop("Australia")  # Removes the {key: value} pair with the specified key
print(capitals)

capitals.popitem()  # Removes and returns the last inserted {key: value} pair (due to ordered nature)
print(capitals)

capitals.clear()  # Clears all elements from the dictionary; don't use print along with it else it will return 'None'
print(capitals)

keys = capitals.keys()  # Returns a view object containing all keys in the dictionary; behaves like a list but is not exactly a list; technically key is an object which resembles a list
print(keys)

for key in capitals.keys():  # We can use the .keys() method with for loops as well because the keys are iterable
    print(key, end=" ")

values = capitals.values()  # Returns a view object containing all values in the dictionary; also list-like; technically value is an object which resembles a list
print(values)

for value in capitals.values():  # We can use the .values() method with for loops as well because the values are iterable
    print(value, end=" ")

items = capitals.items()  # We use this method to get all the {key:value} pairs within a dictionary ; items returns a dictionary object which resembles a 2D list of tuples ; items = [(), (), ()]
print(items)

for key, value in capitals.items():  # We can use the .items() method with for loops as well because the key:value pairs are iterable
    print(f"{key:10}: {value}")      # Allocates 10 spaces so that our output looks well formatted and structured
