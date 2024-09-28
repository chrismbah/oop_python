"""
    Abstract Classes: A class that can't be instantiated on its own
        - Meant to be subclassed
        - They can have abstract methods which can be declared but have no implementation
    
    
    Benefits:
        - Prevents instantiation of a class itself
        - Requires children to use inherited abstract methods
"""

from abc import ABC, abstractmethod
"""
    This decorator is used when you create a class that is not meant to be instantiated on its own but serves as a blueprint for other classes. 
    The abc (Abstract Base Class) module provides the @abstractmethod decorator.
    NB: One must define the complete method for each class 
"""

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")
        
class Bicycle(Vehicle):

    def go(self):
        print("You drive the bicycle")
    def stop(self):
        print("You stop the bicycle")
        
class Boat(Vehicle):

    def go(self):
        print("You sail the boat")    
    def stop(self):
        
        print("You anchor the boat")

car = Car()
bike = Bicycle()
boat = Boat()
car.stop()
bike.stop()
boat.stop()
