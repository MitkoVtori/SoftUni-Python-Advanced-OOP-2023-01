class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.page = pages


class Library:

    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return "No such book"

    def add_book(self, book):
        self.books.append(book)


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Reader(Person):
    def __init__(self, name, age, address, current_book):
        super().__init__(name, age, address)
        self.current_book = current_book
        self.current_page = None

    def turn_page(self):
        if self.current_page:
            self.current_page += 1
            return
        self.current_page = 1

