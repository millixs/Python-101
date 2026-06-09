# Program to find the hypotenuse of a right-angled triangle using math module
# Formula: c = √(a² + b²)

import math

side_a = float(input("Enter the length of the side a: "))
side_b = float(input("Enter the length of the side b: "))
mid = pow(side_a, 2) + pow(side_b, 2)
hypotenuse = math.sqrt(mid)

# We can also calculate the hypotenuse directly using:
# hypotenuse = math.hypot(side_a, side_b)

print(f"The hypotenuse of this triangle is: {hypotenuse:.3f}cm")

