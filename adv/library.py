class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def check_in(self):
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable: {self.is_available}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id

    def __str__(self):
        return f"Name: {self.name}\nPatron ID: {self.patron_id}"


class Transaction:
    def __init__(self, book, patron):
        self.book = book
        self.patron = patron
        self.checked_out = False

    def check_out(self):
        if self.book.check_out():
            self.checked_out = True
            return True
        else:
            return False

    def check_in(self):
        self.book.check_in()
        self.checked_out = False

    def __str__(self):
        return f"Transaction Details:\nBook: {self.book.title}\nPatron: {self.patron.name}\nChecked Out: {self.checked_out}"
    
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

print(book.__str__())