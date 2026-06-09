# return = A statement used to end a function and send a value (result) back to the caller.
# Syntax: return <something>
# It's used to pass data back to the place where the function was invoked.
# The returned value can be stored in a variable, passed to another function, or printed directly.

# Example 1 :-
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

# When we call these functions inside print(), visualize it as print(<result>)
print(add(69, 96))        # Becomes print(165)
print(subtract(77, 42))   # Becomes print(35)
print(multiply(4.55, 6.83))  # Becomes print(31.0765)
print(divide(999, 11))    # Becomes print(90.8181...)

# Example 2 :-
def create_name(first, last):
    first = first.capitalize()  # Capitalizes the first letter of the first name
    last = last.capitalize()    # Capitalizes the first letter of the last name
    return first + " " + last   # Returns the full name as a single string

# Method 1 - Directly printing the returned full name
print(create_name("donut", "sood"))

# Method 2 - Storing the returned value in a variable before printing
full_name = create_name("milli", "sood")
print(full_name)
