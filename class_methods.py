"""
Class Methods allow operations related to the class itself
Takes (cls) as the first param, which reps the class itself

Instance Methods : Best for ops on instances of class (objects)
Static Methods: Best for utility functions that dont need access to class data
Class Methods: Best for class level data or require access to class itself

"""

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    def get_info(self): # Instance method
        return f"{self.name} - {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        return f"Average GPA: {cls.total_gpa / cls.count: .2F}" if cls.count != 0 else 0
    
student1 = Student("Chris",3.6)
student2 = Student("John",4.6)
student3 = Student("Fave",3.9)

print(Student.get_count())
print(Student.get_avg_gpa())
