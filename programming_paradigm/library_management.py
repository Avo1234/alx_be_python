class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_to_shelves(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Formats the book as 'Title by Author'."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                # We use the Book's own method to handle the state change
                if book.is_available():
                    book.check_out()
                return # Stop searching once found

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_to_shelves()
                return # Stop searching once found

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)

