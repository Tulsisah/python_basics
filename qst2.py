#write a python program  to calculate area of circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def display_area(self):
        print(f"Circle - Radius: {self.radius}, Area: {self.calculate_area():.2f}")



radius = float(input("Enter the radius of the circle: "))


circle = Circle(radius)
circle.display_area()
