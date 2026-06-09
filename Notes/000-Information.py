# 📝 Python Useful Information & Commands
# This file stores random or general useful information related to Python.

# 1. The Official List of Python Built-in Modules
# Python provides an official list of all built-in modules with their functions.
# Link: https://docs.python.org/3/library/

# 2. Listing All Available Built-in Modules:
# You can run the following command in Python to display a list of all built-in modules:
help("modules")  # Shows all built-in modules available in your Python environment.

# 3. Exploring Functions Inside a Module
# Once you find a module, you can check what functions it has using `dir()`.
import math  # Replace 'math' with any module
print(dir(math))  # Lists all available functions in the module

# 4. Getting Detailed Information on a Specific Function
# The `help()` function provides documentation for any function.
help(math.sqrt)  # Shows documentation for the `sqrt()` function in the `math` module.

# 5. Getting Full Documentation for String Methods
# The following command will print all available string methods along with descriptions.
print(help(str))  # Displays a list of all built-in string methods.

# 6. Listing Available Methods in a Collection Type (Lists, Tuples, etc.)
# Syntax: print(dir(collection_name))
fruits = ["apple", "banana", "cherry"]
print(dir(fruits))  # Gives a list of methods this LIST [] named 'fruits' can perform

# 7. Getting Detailed Information on List Methods
# The `help()` function provides descriptions of all available methods for lists.
print(help(fruits))  # Gives a description of methods this LIST [] named 'fruits' can perform

# 8. Checking if a Module is Installed:
# This can be useful for verifying third-party modules before importing them.
import importlib.util
module_name = "numpy"
if importlib.util.find_spec(module_name) is not None:
    print(f"{module_name} is installed!")
else:
    print(f"{module_name} is not installed.")

# 9. Finding the File Path of an Imported Module
# This helps identify where a module is located in your system.
import os
print(os.__file__)  # Prints the location of the 'os' module

# 10. Listing Only Built-in Modules (Excluding Installed Packages)
# This filters out external packages installed via pip.
import sys
print(sys.builtin_module_names)  # Lists only built-in modules
