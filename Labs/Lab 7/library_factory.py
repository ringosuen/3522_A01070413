import abc
import difflib


class Item(abc.ABC):

    @abc.abstractmethod
    def __init__(self, call_num, title, num_copies):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self.call_num = call_num
        self.title = title
        self.num_copies = num_copies

    def get_call_number(self):
        """
        Gets the call number from item.
        :return: call number
        """
        return self.call_num

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self.call_num

    def get_title(self):
        """
        Returns the title of the item
        :return: a string
        """
        return self.title.title()

    def check_availability(self):
        """
        Checks the availability based on number of copies availibilty.
        :return: True if > 0, False if < 0
        """
        if self.num_copies > 0:
            return True
        else:
            return False

    def increment_number_of_copies(self):
        """
        Set's the number of copies of an item
        :param value: a positive integer
        """
        self.num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an item
        :param value: a positive integer
        """
        self.num_copies -= 1

    @abc.abstractmethod
    def __str__(self):
        pass


class Book(Item):
    def __init__(self, call_num, title, num_copies, author):
        """
           Initializes a Book library item with title, call number, author,
           and number of coppies
           :param title: a string
           :param call_number: an int
           :param author: a string
           :param num_copies: an int
           """
        super().__init__(call_num, title, num_copies)
        self.author = author

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self.author}"


class DVD(Item):
    """
    Represents a single DVD in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, release_date,
                 region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"


class Journal(Item):
    """
    Represents a single journal in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, publisher,
                 issue_num):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param publisher: a string
        :param issue_num: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._publisher = publisher
        self._issue = issue_num

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Publisher: {self._publisher}" \
               f"Issue #: {self._issue}"


class ItemFactory(abc.ABC):
    @staticmethod
    def generate_item() -> Item:
        """
        Prompts the user with a menu asking them to create either a
        book, DVD or Journal
        :return: An Item.
        """
        print("\nItem Generator")
        print("1. Book")
        print("2. DVD")
        print("3. Journal")
        print("4. Quit")
        user_input = int(input("What item would you like to add (1-4)?"))

        new_item = None
        if user_input == 1:
            new_item = BookFactory.generate_book()
        elif user_input == 2:
            new_item = DvdFactory.generate_dvd()
        elif user_input == 3:
            new_item = JournalFactory.generate_journal()
        elif user_input == 4:
            pass
        else:
            print("Invalid choice entered.")
        return new_item

    @staticmethod
    def _prompt_common_information():
        """
        Prompts the user for item information that is common
        :return: a tuple
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies: "))
        item_data = (call_number, title, num_copies)
        return item_data


class BookFactory(ItemFactory):
    @staticmethod
    def generate_book() -> Item:
        """
        Prompts the user for book information and creates a book item.
        :return: A Book
        """
        item_data = ItemFactory._prompt_common_information()
        author = input("Enter Author Name: ")
        return Book(item_data[0], item_data[1], item_data[2], author)


class DvdFactory(ItemFactory):
    @staticmethod
    def generate_dvd() -> Item:
        """
        Prompts the user for DVD information and creates a DVD item.
        :return: A DVD
        """
        item_data = ItemFactory._prompt_common_information()
        release_date = input("Enter release date: ")
        region_code = input("Enter region code: ")
        return DVD(item_data[0], item_data[1], item_data[2],
                   release_date, region_code)


class JournalFactory(ItemFactory):
    @staticmethod
    def generate_journal() -> Item:
        """
        Prompts the user for Journal information and creates a Journal item.
        :return: A Journal
        """
        item_data = ItemFactory._prompt_common_information()
        publisher = input("Enter publisher name: ")
        issue_num = input("Enter issue number: ")
        return Journal(item_data[0], item_data[1], item_data[2],
                       publisher, issue_num)


class Catalogue:
    """
    A Catalogue is responsible for maintaining the collection of items
    found in a library. This class allows users to add, search, retrieve
    and remove items from the collection.
    """

    def __init__(self, item_list):
        """
        Intialize the catalogue with a list of Items.
        :param item_list: a sequence of Item objects.
        """
        self._item_list = item_list

    def display_catalogue_menu(self):
        """
        Display the interactive Catalogue menu. The user is given
        the choice to add, remove, find and display items in the
        catalogue.
        """
        user_input = None
        while user_input != "b":
            print("\nWelcome to the Catalogue!")
            print("------------------------")
            print("1. Find item")
            print("2. Add item")
            print("3. Remove item")
            print("4. Display Entire Catalogue")
            print("5. Back")
            user_input = int(input("Enter you choice (1-5): "))

            if user_input == 1:
                input_title = input("Enter the title of the item:")
                found_titles = self.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 2:
                self.add_item()

            elif user_input == 3:
                call_number = input("Enter the call number of the item")
                self.remove_item(call_number)

            elif user_input == 4:
                self.display_available_items()

            elif user_input == 5:
                break
            else:
                print("Could not process input. ")

            user_input = input("Would you like to do anything else? "
                               "Enter C to continue and B to go back.")
            user_input = user_input.lower()

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the catalogue.
        :param call_number: a string
        :return: Item object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._item_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the catalogue with a unique call number.
        """
        new_item = ItemFactory.generate_item()
        found_item = self._retrieve_item_by_call_number(
            new_item.call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{new_item.call_number}. It already exists. ")
        else:
            self._item_list.append(new_item)
            print("Item added successfully! Item details:")
            print(new_item)

    def remove_item(self, call_number):
        """
        Remove an existing item from the catalogue
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"Item with call number: {call_number} not found.")

    def display_available_items(self):
        """
        Display all the items in the catalogue.
        """
        print("Catalogue List")
        print("--------------", end="\n\n")
        for library_item in self._item_list:
            print(library_item)

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the catalogue.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the catalogue.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False


class Library:
    """
    The Library consists of a catalogue of items and provides an
    interface for users to check out, return and find items.
    """

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def access_catalogue(self):
        """
        Access the library's catalogue menu.
        """
        self.catalogue.display_catalogue_menu()

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the catalogue.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.catalogue.reduce_item_count(call_number)
        if status:
            print("Checkout complete!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the catalogue.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.catalogue.increment_item_count(call_number)
        if status:
            print("Item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        catalogue, check out or return an item.
        """
        user_input = None
        while user_input != 4:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Access Catalogue")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Quit")
            user_input = int(input("Please enter your choice (1-3)"))

            if user_input == 1:
                self.access_catalogue()
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

        print("See you later. Thanks for coming")


def generate_test_items():
    """
    Return a list of items with dummy data.
    :return: a list
    """
    item_list = [
        Book("123", "Harry Potter 1", 2, "J K Rowling"),
        DVD("9999", "Pokemon 1st moveie",
            2, "2001-03-21", 2),
        Journal("7777", "Python", 2,
                "Python Publisher", 87)
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_items()
    my_catalogue = Catalogue(item_list)
    my_library = Library(my_catalogue)
    my_library.display_library_menu()


if __name__ == '__main__':
    main()
