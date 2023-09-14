import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5, "red")
circle2 = Circle(3, "blue")
circle3 = Circle(7, "green")

print(f"Circle 1: Radius = {circle1.radius}, Color = {circle1.color}")
print(f"Area of a circle 1: {circle1.calculate_area()}")
print(f"Circumference of a circle 1: {circle1.calculate_circumference()}")

print(f"Circle 2: Radius = {circle2.radius}, Color = {circle2.color}")
print(f"Area of a circle 2: {circle2.calculate_area()}")
print(f"Circumference of a circle 2: {circle2.calculate_circumference()}")

print(f"Circle 3: Radius = {circle3.radius}, Color = {circle3.color}")
print(f"Area of a circle 3: {circle3.calculate_area()}")
print(f"Circumference of a circle 3: {circle3.calculate_circumference()}")