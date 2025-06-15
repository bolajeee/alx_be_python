# basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"{book.title} has been checked out.")
                else:
                    print(f"{book.title} is already checked out.")
                return
        print(f"{title} not found in the library.")    
        
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"{book.title} has been returned.")
                else:
                    print(f"{book.title} was not checked out.")
                return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        if not self._books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self._books:
                status = "Checked out" if book._is_checked_out else "Available"
                print(f"{book.title} by {book.author} - {status}")