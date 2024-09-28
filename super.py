"""
    super() = A function used in a child class to call methods from a parent class (superclass)
    Allows one to extend the functionality of the inherited methods    
"""

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"} ")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius ** 2} {self.color} and {"filled" if self.is_filled else "not filled"} ")
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
circle = Circle(color="red", is_filled=False, radius=5)
square = Square(color="green", is_filled=True, width=4)

print(circle.color, circle.is_filled, circle.radius, circle.describe() )
print(square.color, square.is_filled, square.width )