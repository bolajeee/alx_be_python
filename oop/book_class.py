# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that notifies when a Book instance is deleted."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """User-friendly string representation of the Book object."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (you can remove this block if the script is meant to be imported as a module)
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))     # Human-readable string
    print(repr(book1))    # Developer-friendly representation

    del book1             # Triggers __del__ method
