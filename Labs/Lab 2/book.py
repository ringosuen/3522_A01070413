class Book:
    def __init__(self, title, call_number, author, num_copies):
        self._title = title
        self._call_number = call_number
        self._author = author
        self._num_copies = num_copies

    def check_availibility(self):
        if self._num_copies > 1:
            return self._num_copies
        else:
            return 0

    def __str__(self):
        return (f"Title: {self._title} , call numer: {self._call_number}, "
                f"Author: {self._author} wrote the book."
                f" Number of copies available {self._num_copies}")

