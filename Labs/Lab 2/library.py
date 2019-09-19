from book import book
class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, call_number):
        if call_number in self.book_list:
            print("The book you requested has now been removed")
            self.book_list.remove(call_number)

    def find_books(self, title):
        for book in self.book_list:
            if book.title == title:
                return book

    def check_out(self, call_number):
        if call_number in self.book_list:
            print("The book you have requested has now been checked out")
            self._num_copies -= 1
        else:
            print("The book you have requested is not currently available")

    def return_book(self, call_number):
        if call_number in self.book_list:
            print("The book you have requested has now been checked out")
            self._num_copies += 1
            print("You have returned you book")

    def display_availible_books(self):
        if self.book_list:  # if list of books is not empty
            print("The books we have made available in our library are:\n")
            for book in self.book_list:
                print(book)
        else:
            print("Sorry, we have no books available in the library at the moment")


def main():
    """
    Creates a book
    """
    book1 = Library()


if __name__ == '__main__':
    main()