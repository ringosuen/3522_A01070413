""" This module houses the card collection."""
from datetime import date

from cards import CreditCard, RewardsCard, IdCard, BusinessCard, CardGenerator
import difflib
import time


class CardManager:
    """
    A general card manager responsible for taking care of the collection of
    available cards. It has methods to add, search, remove and display the
    collection of different cards in the program. Also has the ability to
    export the collection of added cards to an external backup file named
    MyAppName_Export_DDMMYY_HHMM.txt
    """

    def __init__(self):
        """
        Intialize the card manager with a list of Cards.
        """
        self.card_list = []

    def add_card(self):
        """
        Add a card to the database. Uses card generator class to add
        a card depending on the type.
        :return:
        """
        new_item = CardGenerator.generate_item()
        self.card_list.append(new_item)
        print("Item added successfully! Item details:")
        print(new_item)

    def remove_card(self, card_name):
        """
        Remove an existing card from the collection
        :param card_name: a string
        :precondition card_name: a unique identifier
        """
        found_item = self._retrieve_card_by_name(card_name)
        if found_item:
            self.card_list.remove(found_item)
            print(f"Successfully removed {found_item.get_name()} with "
                  f"call number: {card_name}")
        else:
            print(f"Item with card name: {card_name} not found.")
            print("Be more specific!")

    def search_card(self, name):
        """
        Searches a card from the collection.
        :return: the searched card
        """
        word = name.title()
        for item in self.card_list:
            if word == item.get_name():
                print(f"Item found: {item}")
                return item
        else:
            print("Can't find the item, be more specific!")

    def display_available_items(self):
        """
        Display all the cards in the collection.
        """
        print("Card Collection\n")
        print("Displayed by card type: ")
        print("--------------", end="\n\n")

        sorted_list = sorted(self.card_list, key=lambda card: card.value)

        for card_item in sorted_list:
            print(card_item)

    def _retrieve_card_by_name(self, card_name):
        """
        A private method that encapsulates the retrieval of a card with
        the given name from the card collection.
        :param card_name: a string
        :return: card object if found, None otherwise
        """
        found_item = None
        for card_item in self.card_list:
            if card_item.card_name == card_name:
                found_item = card_item
                break
        return found_item

    def backup(self, path):
        with open(path, 'w') as filehandle:
            for list_item in self.card_list:
                filehandle.write('%s\n' % list_item)

    def display_menu(self):
        user_input = None
        while True:
            print("\nWelcome to the card manager!")
            print("------------------------")
            print("1. Add a card")
            print("2. Find a card")
            print("3. Remove a card")
            print("4. Display Entire Collection of cards")
            print("5. Back up your data!")
            print("6. End program")

            try:
                user_input = int(input("Enter you choice (1-5): "))

                if user_input == 1:
                    self.add_card()
                elif user_input == 2:
                    # input_title = input("Enter the title of the item:")
                    # found_titles = self.search_card(input_title)
                    # print("We found the following:")
                    # if len(found_titles) > 0:
                    #     for title in found_titles:
                    #         print(title)
                    # else:
                    #     print("Sorry! We found nothing with that title")
                    user_input = input("enter title to search: ").title()
                    self.search_card(user_input)
                elif user_input == 3:
                    card_name = input("Enter the name of the card"
                                      " that you gave").title()
                    self.remove_card(card_name)
                elif user_input == 4:
                    self.display_available_items()
                elif user_input == 5:
                    print("\nBacking up your data to an external file!")
                    print("It's on the cloud now!")
                    file_name = time.strftime("CardManager_Export_%Y%m%d_%H%M.txt")
                    self.backup(file_name)
                elif user_input == 6:
                    break
                else:
                    print("Could not process input. Enter 1-6. ")
            except ValueError:
                print("Enter a number please, not a letter.")
            except TypeError:
                print("Type Error!")


def main():
    test = CardManager()
    test.display_menu()


if __name__ == '__main__':
    main()
