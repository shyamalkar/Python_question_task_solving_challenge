"""1. Circle Area Calculator (Arithmetic)Write a program that takes the radius of a circle as input from the user.
 Calculate and print its area using the formula: Area = π × r². Use π ≈ 3.14159 and convert the input string to a float.
"""

# circle area calculator (arithmetic)
pi = 3.14159

radius = float(input("Enter the radius of the circle:"))


area = pi * radius ** 2
print("The area of the circle is:", area)

# Explanation 
"""
inputs() gets the radius as a string. 
float() converts into a decimal number.
radius ** 2 calculates the square of the radius 
the area is computed using pi * r sqare
"""