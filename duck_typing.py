"""
Duck Typing is another way to achieve polymorphism besides inheritance
    Object must have minimum necessary attributes/methods
    "If it looks like a duck, quacks like a duck it must be a duck"
        
"""

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!!")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Car:
    alive = False
    def speak(self):
        print("Honk!!")
        

an = Animal()
animals = [Cat(), Dog(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
