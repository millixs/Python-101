"""
Argument - They are the values passed to a function when it is called.
They provide the function with the data it needs to perform its specified operations.
Arguments are written inside the parentheses of a function call and correspond to the parameters defined in the function’s declaration.

Types of Arguments : -
1) Positional Arguments – Passed in the same order as defined in the function parameters.
2) Default Arguments – Parameters that assume a default value if no argument is provided.
3) Keyword Arguments – Arguments passed using parameter names, allowing any order.
4) Arbitrary Arguments – Used when the number of arguments is unknown; captured using *args (for non-keyword) or **kwargs (for keyword args).
"""


# POSITIONAL ARGUMENTS : -
# Positional arguments are arguments that must be passed to a function in the correct positional order.
# That means the order in which values are passed must match the order of parameters in the function definition.

# Example :-
def greet(greeting, name):
    print(f"{greeting} {name} ♡")
    print("Welcome to the Club!!")
    print()
# Correct order – 'greeting' and 'name' are in the intended positions
greet("Good Evening", "Milli")
# Incorrect order – Swapping arguments leads to unexpected output
greet("Kevin", "Good Morning")


# DEFAULT ARGUMENTS : -
# Default arguments are function parameters that assume a default value if no argument is provided during the function call.
# It means having a default value for certain parameters
# Default is used when that argument is omitted
# Makes our function more flexible, reduces the number of arguments
# NOTE: Non-default arguments should be written before the default arguments to avoid syntax errors
# It means the arguments which do not have any default value should be written first in the function definition and call
# Example: In 'def count(end, start=0):' end comes before start as it is a non-default argument

# Example 1:-
def net_price(list_price, discount=0.0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)
# Function call with only the required argument; 'discount' and 'tax' use default values
print(net_price(500))
# Function call where all arguments are explicitly provided, overriding the default values
print(net_price(700, 0.1, 0))

# Example 2:-
import time
def count(end, start=0):
    for i in range(start, end + 1):  # We wrote end+1 because the second argument is exclusive, so our timer does not stop 1 second before as we start from 0
        print(i)
        time.sleep(1)  # Introduces a 1-second delay between prints, simulating a countdown or timer
    print("DONE!")
# Here the value of end = 5
count(5)
# Here the value of end = 30 and the value of start = 15
count(30, 15)


# KEYWORD ARGUMENTS : -
# Keyword or Named arguments are a way of passing arguments to a function by explicitly specifying which parameter they should be assigned to.
# Syntax: parameter_name = value
# Example : - In 'print(x, end = " ")' : end = " " is a keyword argument found within the built-in function call
# Keyword arguments improve readability and reduce ambiguity by clearly indicating which value corresponds to which parameter
# It is basically an argument preceded by an identifier, which enhances the readability of our code
# NOTE: Positional arguments should be written before the Keyword arguments to avoid syntax errors
# It means the positional arguments should be written first in the function definition and call
# Example: In 'greetings("Hello", title= "Mr.", first_name="Dinkey", last_name="Donut")' Hello comes first as it is a positional argument

# Example 1: -
def greetings(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")
greetings("Hello", title="Mr.", last_name="Donut", first_name="Dinkey")

# Example 2:-
def get_phone(country_code, ten_digit_num):
    return f"{country_code}-{ten_digit_num}"
print(get_phone(91, ten_digit_num="8219808133"))


# ARBITRARY ARGUMENTS: -
# Arbitrary arguments allow us to pass a variable (unspecified) number of arguments to a function.
# There are two types of arbitrary arguments:
# 1) *args    → Arbitrary Positional Arguments
# 2) **kwargs → Arbitrary Keyword Arguments
# NOTE: * is known as the "unpacking operator"

# *args : -
# Allow us to pass multiple non-key arguments
# Used when we don't know how many positional arguments will be passed.
# Internally, Python packs all the passed positional arguments into a tuple.
# We can perform all valid tuple operations on 'args'.

# Example 1: -
def add(*args):
    total = 0
    for arg in args:  # we can iterate over the tuple 'args' using a for loop
        total += arg
    return total
print(add(6, 4, 5, 8.3))  # We can pass any number of positional arguments (of numeric types in this case)

# Example 2: -
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Lionel", "Andrés", "Messi", "Cuccitini")  # Accepts any number of positional string arguments

# **kwargs : -
# Allow us to pass multiple keyword arguments (in the form key=value)
# Used when we don't know how many keyword arguments will be passed.
# Internally, Python packs these keyword arguments into a dictionary.
# We can perform all dictionary operations on 'kwargs'.

# Example 1: -
def display_address(**kwargs):
    for key, value in kwargs.items():  # .items() allows us to iterate over the dictionary's key:value pairs
        print(f"{key:10} : {value}")
# We can pass any number of keyword arguments (key=value format)
display_address(house_name="Sansar Villa",
                landmark="Near High Court",
                area="The Mall",
                city="Shimla",
                state="Himachal Pradesh",
                zip="171001")


# Example: Using both *args and **kwargs in a function
# NOTE: *args (positional arguments) must always appear before **kwargs in a function definition.
#       This is required to avoid syntax errors.
def shipping_label(*args, **kwargs):
    # Printing all positional arguments (e.g., titles or names)
    for arg in args:
        print(arg, end=" ")
    print()
    # Printing all keyword argument values (e.g., address details)
    for value in kwargs.values():
        print(value, end=" ")
# Calling the function with positional and keyword arguments
shipping_label("Ms.", "Milli", "Sood",
               house_name="Sansar Villa",
               city="Shimla",
               state="H.P.",
               zip="171001")
