# week-07 -> measurements.py

import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * math.pow(radius, 2)

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * math.pow(radius, 3)

# Function to convert Fahrenheit to Celsius
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to solve a quadratic equation
def quadratic(a=1, b=-7, c=10):
    discriminant = math.pow(b, 2) - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    else:
        return ("Complex Roots",)

# Function to calculate the distance between two points
def distance(x1=1, y1=1, x2=4, y2=5):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Function to print all test results
def print_tests():
    print("Rectangle Area (length=12, width=13):", rectangle_area(12, 13))
    print("Circle Area (radius=5):", circle_area(5))
    print("Sphere Volume (radius=9):", sphere_volume(9))
    print("100 Celsius to Fahrenheit:", to_fahrenheit(100))
    print("0 Celsius to Fahrenheit:", to_fahrenheit(0))
    print("212 Fahrenheit to Celsius:", to_celsius(212))
    print("32 Fahrenheit to Celsius:", to_celsius(32))
    print("Quadratic equation x^2 - 7x + 10 = 0 roots:", quadratic(1, -7, 10))
    print("Quadratic equation x^2 - x - 2 = 0 roots:", quadratic(1, -1, -2))
    print("Default Quadratic equation roots:", quadratic())
    print("Distance (2, 5) to (7, 17):", distance(2, 5, 7, 17))
    print("Default Distance (1, 1) to (4, 5):", distance())

# Function to test individual functions with input parameters
def test_functions():
    length = float(input("Enter length for rectangle: "))
    width = float(input("Enter width for rectangle: "))
    print("Rectangle Area:", rectangle_area(length, width))

    radius = float(input("Enter radius for circle: "))
    print("Circle Area:", circle_area(radius))

    radius = float(input("Enter radius for sphere: "))
    print("Sphere Volume:", sphere_volume(radius))

    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    print("Celsius:", to_celsius(fahrenheit))

    celsius = float(input("Enter Celsius temperature: "))
    print("Fahrenheit:", to_fahrenheit(celsius))

    a = float(input("Enter a for quadratic equation: "))
    b = float(input("Enter b for quadratic equation: "))
    c = float(input("Enter c for quadratic equation: "))
    print("Quadratic Roots:", quadratic(a, b, c))

    x1 = float(input("Enter x1 for distance calculation: "))
    y1 = float(input("Enter y1 for distance calculation: "))
    x2 = float(input("Enter x2 for distance calculation: "))
    y2 = float(input("Enter y2 for distance calculation: "))
    print("Distance:", distance(x1, y1, x2, y2))

if __name__ == "__main__":
    print_tests()
    # Uncomment below line to test functions interactively
    # test_functions()
