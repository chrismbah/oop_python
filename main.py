class Student:

    # Class variables are defined OUTSIDE the constructor
    grad_year = 2024 
    num_students = 0

    def __init__(self, name, age) :
        self.name = name
        self.age = age
        Student.num_students += 1 # Increases as the no of obj increases

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student2 = Student("Squidward", 40)

print(student1.grad_year)
print(Student.num_students) 
