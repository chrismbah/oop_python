class Animal:
    def __init__(self, name, is_alive = True):
        self.name = name
        self.is_alive = is_alive
    def eat(self):
        """Prints that the animal is eating."""
        print(f"{self.name} is eating ")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Tom", False)
mouse = Mouse("Jerry")

print(dog.name, dog.is_alive, dog.eat())
print(cat.name, cat.is_alive)
print(mouse.name, mouse.is_alive)