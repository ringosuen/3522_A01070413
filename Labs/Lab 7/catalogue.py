"""This module handles basic library tasks for items in COMP3522 Lab 02"""
from book import LibraryItemGenerator, Book, Dvd, Journal
import sys


class Catalogue:
    """
    The Catalogue class is responsible for the addition,
    removal, search, checkout,
    return and displaying all items in a library.
    """

    def __init__(self):
        """
        Initializes a library item list.
        """
        self.item_list = []

    def add_item(self, item):
        """
        Adds an item to the item list. Uses classes
        from ItemListGenerator to determine whether it is a book,
        dvd or journal item.
        :param item: a list
        :return: an a book, dvd or journal item
        """

        while True:
            print(""" ======Add MENU=======
                   1. Add Book
                   2. Add DVD
                   3. Add Journal
                   4. Return to main menu
                   """)
            choice = int(input("Enter Choice:"))
            if choice == 1:
                item = Book(input("Enter title: "),
                            int(input("Enter call number: ")),
                            input("Enter author: "),
                            int(input("Enter number of copies: ")))
            if choice == 2:
                item = Dvd(input("Enter title"),
                           int(input("Enter call number: ")),
                           input("Enter author"),
                           int(input("Enter number of copies: ")),
                           input("Enter release date: "),
                           int(input("Region Code: ")))
            if choice == 3:
                item = Journal(input("Enter title: "),
                               int(input("Enter call number: ")),
                               input("Enter author:"),
                               int(input("Enter number of copies: ")),
                               input("Enter name: "),
                               int(input("Enter issue number: ")),
                               input("Enter publisher: "))
            if choice == 4:
                break

            self.item_list.append(item)

    def remove_item(self, call_number):
        """
        Remove specified item by call number from item list.
        :param call_number: an int
        :return: new list with removed object
        """
        for item in self.item_list:
            if call_number == item.get_call_number():
                print("The item you requested has now been removed")
                self.item_list.remove(item)

    def search(self, title):
        """
        Search for item based on title input.
        :param title: a string
        :return: found item
        """
        for item in self.item_list:
            if title == item.get_title():
                print(f"Item found: {item}")
                return item
            else:
                print("can't find item")

    def check_out(self, call_number):
        """
        Check out item, decreases number of copies by 1.
        :param call_number: an int
        """
        for item in self.item_list:
            if call_number == item.get_call_number():
                print("The item you have requested has now been checked out")
                item.num_copies -= 1
            else:
                print("The item you have requested is not currently available")

    def return_item(self, call_number):
        """
        Return item, increases number of copies by 1.
        :param call_number: an int
        """
        for item in self.item_list:
            if call_number == item.get_call_number():
                print("The item you have requested has now been returned")
                item.num_copies += 1
            else:
                print("The item you have requested is not currently available")

    def display_available_items(self):
        """
        Displays all items added to item list.
        :return: item list
        """
        if self.item_list:
            print("The items we have made available in our library are:\n")
            for item in self.item_list:
                print(item)
        else:
            print("Sorry, we have no books available "
                  "in the library at the moment")
