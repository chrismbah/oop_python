# Composition is when the composed object directly owns its components
#   which cant exist independently. It has a "owns-a" relationship

class Engine:
    def __init__(self, hp):
        self.hp = hp

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, hp, wheel_size) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(hp)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def display_car(self):
        return f"{self.make}, {self.model} {self.engine.hp} hp, {self.wheels[0].size} "
        
car = Car(make="Ford", model="Mustang", hp=500, wheel_size=18)
car = Car(make="Ferrari", model="Corvette", hp=670, wheel_size=90)
print(car.display_car())