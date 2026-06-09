# We will cover some basic and most used built-in math functions in Python

z = 5
w = -7
x = 3.14

result = round(x)          # Rounds the number to the nearest integer
# result = abs(w)          # Returns the absolute (positive) value of a number -> (basically it's distance from 0)
# result = pow(2,5)        # Raises 2 to the power of 5 (2^5)
# result = max(z,w,x)      # Returns the largest value among z, w, and x
# result = min(z, w, x)    # Returns the smallest value among z, w, and x

print(result)


# We will cover some math functions by importing the math module class
import math

y = 9.4

# print(math.pi)        # Returns the value of π (3.14159...)
# print(math.e)         # Returns the value of Euler's number (2.718...)
# res = math.sqrt(x)    # Returns the square root of x
# res = math.ceil(y)    # Rounds y UP to the nearest whole number
res = math.floor(y)     # Rounds y DOWN to the nearest whole number

print(res)
