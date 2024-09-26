"""
Multiple inheritance: Inherit from more than one parent class
    >>> C(A, B)

Multi level inheritance: Inherit from one parent which inherits from another parent
    >>> C(B) <- B(A) <- A
"""

# Multi level inheritance
class Animal:
    def __init__ (self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
        
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator): # Multiple inheritance
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Mihawk")
fish = Fish("Nemo")

fish.flee()
rabbit.flee()
fish.hunt()
hawk.eat()
rabbit.sleep()