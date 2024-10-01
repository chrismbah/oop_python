"""
Nested classes are classes that are defined inside other classes
    class Outer:
        class Inner:
        
Benefits: Allows you to logically group classes that are closely related 
            Encapsulates private details that arent relevant outside of outer class
            Keeps the namespace clean and reduces possiility of naming conflicts
"""

class Company:
    class Employee:
        def __init__(self, name, position) -> None:
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name}, {self.position}"
    
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position) # Composition
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Krusty Krabs")
company.add_employee("Eugene Krabs", "Manager")
company.add_employee("Spongebob", "Cook")
company.add_employee("Squidward", "Cashier")
for employee in company.list_employees():
    print(employee)



