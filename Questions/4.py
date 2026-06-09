# Program to calculate the circumference of a circle using math module
# Formula: 2 * pi * radius

import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference:.2f}cm")

# We can also use the round() function to round off the answer, to say upto 2 decimal places
print(f"The circumference of the circle is: {round(circumference, 2)}cm")
