class Book:

    def __init__(self, content):
        self.content = content


class Formatter:

    def format(self, book):
        return book.content


class Printer:

    def get_book(self, book, formatter):
        return formatter.format(book)


book = Book("book")
formatter = Formatter()
printer = Printer()

print(printer.get_book(book, formatter))
