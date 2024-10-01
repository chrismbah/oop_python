# Aggregation represents a relationship where one object (the whole) 
#   contains references to one or more INDEPENDENT objects (parts)

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
        

class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        
library = Library("New York Pulic Library")

book1 = Book(title="Harry Potter", author="J.K. Rowling")
book2 = Book(title="The Hobbit", author="J.R.R Tolken")
book3 = Book(title="Half of a Yellow Sun", author="Chimamanda Ngozi ")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print(library.list_books())