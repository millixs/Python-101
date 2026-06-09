# Program to calculate the area of a circle using math module
# Formula: pi * radius * radius

import math

radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius * radius

# We can also use the pow() function to square the radius
area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {area:.2f}cm²")
print(f"The area of the circle is: {round(area, 2)}cm²")
