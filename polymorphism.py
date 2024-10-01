"""
Polymorphism : Greek word that means to have many forms 

Two ways to achieve Polymorphism
    1. Inheritance = An object could be treated of the same type as a parent class
    2. Duck Typing = An object must have necessary attributes/methods
"""
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
class Pizza(Circle):
    def __init__(self, topping, radius) -> None:
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(5,7), Pizza("pepperoni", 20)]
for shape in shapes:
    print(f"{shape.area()} cm2")