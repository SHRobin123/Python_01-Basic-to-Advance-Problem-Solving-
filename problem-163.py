#Library Management System

class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def show(self):
        status = "Available" if self.available else "Issued"
        print(self.name, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name):
        b = Book(name)
        self.books.append(b)

    def issue_book(self, name):
        for b in self.books:
            if b.name == name and b.available:
                b.available = False
                print(name, "Issued")
                return
        print("Book not available")

    def return_book(self, name):
        for b in self.books:
            if b.name == name:
                b.available = True
                print(name, "Returned")
                return

    def show_books(self):
        print("Library Books:")
        for b in self.books:
            b.show()


# system create
lib = Library()

lib.add_book("Math")
lib.add_book("Physics")

lib.issue_book("Math")
lib.return_book("Math")

lib.show_books()

'''
output:-

Math Issued
Math Returned
Library Books:
Math - Available
Physics - Available
'''