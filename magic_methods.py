"""
Magic Methods: Dunder methods(double underscore), __init__, __str__, __eq__
            They are automatically called by may of py built in ops
            They allows devs define or customize the behaviour of objects
"""

class Book:

    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self) -> str: # String representation of the object
        return f"{self.title} by {self.author}"
    
    def __eq__(self, value: object) -> bool: # Compare if two obj are equal
        return self.title == value.title and self.author == value.author
    
book1 = Book("The Hobbit", "J.R.R Tolken", 310)
book2 = Book("The Hobbit", "J.R.R Tolken", 310)
# book2 = Book("Harry Potter", "J.K Rowling", 740)

print(book1 == book2)