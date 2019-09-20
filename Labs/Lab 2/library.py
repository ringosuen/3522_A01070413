from book import LibraryItemGenerator, Book, Dvd, Journal
import abc
import sys
from catalogue import Catalogue
from book import LibraryItemGenerator, Book, Dvd, Journal


class Library:

    def find_item(self):
        Catalogue.search()

    @staticmethod
    def display_available_items(catalogue):
        if catalogue.item_list:
            print("The books we have made available in our library are:\n")
            for item in catalogue.item_list:
                print(item)
        else:
            print("Sorry, we have no books available in the library at the moment")


def main():
    """
    Creates a book
    """
    catalogue = Catalogue()

    # book1 = Book("title1", 22323, "author", 4)
    # dvd1 = Dvd("dvdt", 1111, "jurassic", 2, "sept 2", "japan")
    # catalogue.add_item(book1)
    # catalogue.add_item(dvd1)

    while True:
        print(""" ======LIBRARY MENU=======
            1. Add Item
            2. Remove item 
            3. Display all items
            4. Checkout item 
            5. Return item 
            6. Find item 
            7. Exit
            """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            catalogue.add_item(catalogue)
        elif choice == 2:
            user_input = int(input("enter call number: "))
            catalogue.remove_item(user_input)
        elif choice == 3:
             catalogue.display_available_items()
        elif choice == 4:
            user_input = int(input("enter call number: "))
            catalogue.check_out(user_input)
        elif choice == 5:
            user_input = int(input("enter call number: "))
            catalogue.return_item(user_input)
        elif choice == 6:
            user_input = input("enter title to search: ")
            catalogue.search(user_input)
        if choice == 7:
            sys.exit()


if __name__ == '__main__':
    main()
