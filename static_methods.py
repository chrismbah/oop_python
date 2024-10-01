# Static methods is a method that belongs to a class rather than any object from that class (instance)
# Usually used for general utility functions

# Instance methods are best for ops on instances of the class
# Static methods are best for utility functions that dont need access to class data
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
    
print(Person.is_adult(20))
