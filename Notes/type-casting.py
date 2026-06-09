# Type-casting: The process of converting a variable from one data type to another.
#               This is especially useful when handling user input, where type conversion is needed.
#               Common functions: str(), int(), float(), bool()

name = "Milli Sood"    # string
age = 19               # integer
gpa = 8.9              # float
is_student = True      # boolean

# string --> boolean
name = bool(name)     # Reassign 'name' and typecast it to boolean
print(name)           # Returns True if the string is non-empty; if empty (""), it returns False
print(type(name))     # Returns the type of the variable, which is now boolean

# integer --> string
age = str(age)       # Reassign 'age' and typecast it to string
print(age)           # Returns '19' as a string; arithmetic operations won't work directly on it
print(type(age))     # Returns string

# float --> integer
gpa = int(gpa)       # Reassign 'gpa' and typecast it to integer
print(gpa)           # Returns 8, removing the decimal portion (truncation, not rounding)
print(type(gpa))     # Returns integer

# integer --> float
age = float(age)     # Reassign 'age' and typecast it to float
print(age)           # Returns 19.0, adding a decimal portion
print(type(age))     # Returns float

# boolean --> string
is_student = str(is_student)    # Reassign 'is_student' and typecast it to string
print(is_student)               # Returns 'True', but as a string and not a boolean value
print(type(is_student))         # Returns string
