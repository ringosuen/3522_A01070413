"""
This module represents how an abstract base class can be used to
enforce objects to implement a common interface.
"""
import abc


class LibraryItemGenerator(abc.ABC):
    """
    An Abstract Base Class that provides a simple interface that all
    items need to implement. Any class that inherits from this
    class MUST implement all the @abstractmethods and
    @abstractclassmethods.
    """
    def __init__(self, title, call_number, author, num_copies):
        self._title = title
        self._call_number = call_number
        self._author = author
        self.num_copies = num_copies

    def get_call_number(self):
        return self._call_number

    def get_title(self):
        return self._title

    def get_num_copies(self):
        return self.num_copies

    @abc.abstractmethod
    def check_availability(self):
        if self.num_copies > 0:
            return True
        else:
            return False

    def __str__(self):
        return (f"Book Title: {self._title}, Call number: {self._call_number}, "
                f"Author: {self._author},"
                f"Number of copies available: {self.num_copies}")


class Book(LibraryItemGenerator):
    def __init__(self, title, call_number, author, num_copies):
        super().__init__(title, call_number, author, num_copies)


class Dvd(LibraryItemGenerator):
    def __init__(self, title, call_number, author, num_copies, release_date, region_code):
        self._release_date = release_date
        self._region_code = region_code
        super().__init__(title, call_number, author, num_copies)

    def __str__(self):
        return (f"Dvd Title: {self._title} , Call number: {self._call_number}, "
                f"Author: {self._author}, "
                f"Number of copies available: {self.num_copies}, "
                f"Release date: {self._release_date}, "
                f"Region code: {self._region_code} ")


class Journal(LibraryItemGenerator):
    def __init__(self, title, call_number, author, num_copies, name, issue_num, publisher):
        self._name = name
        self._issue_num = issue_num
        self._publisher = publisher
        super().__init__(title, call_number, author, num_copies)

    def __str__(self):
        return (f"Journal Title: {self._title} , call number: {self._call_number}, "
                f"Author: {self._author},"
                f" Number of copies available {self.num_copies}, "
                f"Name: {self._name}, "
                f"Publisher: {self._publisher}, "
                f"Issue Number: {self._issue_num}. ")
