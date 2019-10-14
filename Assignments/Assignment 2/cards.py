"""This module contains all the different types of cards and a generator
class to generate these different cards"""

from abc import ABC, abstractmethod


class Card(ABC):
    """
    Represents a card in the collection. This is an abstract base class
    that defines the basic interface all cards in the collection have to adhere
    to. These cards are identified by their type.
    """

    @abstractmethod
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Returns the name of the card
        :return: a string
        """
        return self.name.title()

    @property
    def card_name(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self.name

    @abstractmethod
    def __str__(self):
        pass


class CreditCard(Card):
    def __init__(self, name, bank, card_holder, number, expiry, value=0):
        super().__init__(name)
        self.bank = bank
        self.card_holder = card_holder
        self.number = number
        self.expiry = expiry
        self.value = value


    def __str__(self):
        return f"---- CREDIT CARD: {self.name} ----\n" \
               f"Bank: {self.bank}\n" \
               f"Card Holder: {self.card_holder}\n" \
               f"Card Number: {self.number}\n" \
               f"Expiry Date: {self.expiry}\n"

    def __len__(self):
        """
        returns the number of smurfs in the team
        :return: the length of the list
        """
        return len(self.name)

class RewardsCard(Card):
    def __init__(self, name, company, card_holder, number, value=1):
        super().__init__(name)
        self.company = company
        self.card_holder = card_holder
        self.number = number
        self.value = value

    def __str__(self):
        return f"---- REWARDS CARD: {self.name} ----\n" \
               f"Company: {self.company}\n" \
               f"Card Holder: {self.card_holder}\n" \
               f"Card Number: {self.number}\n"


class BusinessCard(Card):
    def __init__(self, name, company, address, phone, value=2):
        super().__init__(name)
        self.company = company
        self.address = address
        self.phone = phone
        self.value = value

    def __str__(self):
        return f"---- BUSINESS CARD: {self.name} ----\n" \
               f"Company or Person: {self.company}\n" \
               f"Address: {self.address}\n" \
               f"Phone Number: {self.phone}\n"


class IdCard(Card):
    def __init__(self, name, type_id, number, card_holder, value=3):
        super().__init__(name)
        self.type_id = type_id
        self.number = number
        self.card_holder = card_holder
        self.value = value

    def __str__(self):
        return f"---- ID CARD: {self.name} ----\n" \
               f"Type of ID Card: {self.type_id}\n" \
               f"ID Number: {self.number}\n" \
               f"Card Holder: {self.card_holder}\n"


class CardGenerator:
    """
    Generates different cards based on the type. A class filled with static
    methods.
    """

    @staticmethod
    def _prompt_common_information():
        """
        Prompts the user for card information that is common to all
        cards.
        :return: item_data
        """
        # call_number = input("Enter Call Number: ")
        # num_copies = int(input("Enter number of copies "
        #                        "(positive number): "))
        name = input("Enter a name for your card: ").title()
        item_data = name
        return item_data

    @staticmethod
    def generate_creditcard():
        """
        Prompts the user for credit card information and creates a credit card.
        :return: A Credit Card
        """

        item_data = CardGenerator._prompt_common_information()
        bank = input("Enter Bank Name: ").title()
        card_holder = input("Enter your name seen on the card: ").title()
        credit_number = input("Enter the credit card number: ")
        expiry_date = input("Enter the expiry date: ")

        return CreditCard(item_data, bank, card_holder, credit_number,
                          expiry_date)

    @staticmethod
    def generate_rewardscard():
        """
        Prompts the user for rewards card information and creates a rewards
        card.
        :return: A Rewards Card
        """
        item_data = CardGenerator._prompt_common_information()
        company = input("Enter the shop or business name: ").title()
        card_holder = input("Enter your name on the card: ").title()
        rewards_number = input("Enter the rewards card number: ")

        return RewardsCard(item_data, company, card_holder, rewards_number)

    @staticmethod
    def generate_idcard():
        """
        Prompts the user for ID card information and creates an ID card
        :return: An ID Card
        """

        item_data = CardGenerator._prompt_common_information()
        id_type = input("Enter the type of ID it is (eg. Care Card, Drivers"
                        "License, Social insurance card): ")
        id_number = input("Enter the number on the card: ")
        id_name = input("Enter the name on the ID card r: ")

        return IdCard(item_data, id_type, id_number, id_name,)

    @staticmethod
    def generate_businesscard():
        """
        Prompts the user for business card information and creates a business
        card.
        :return: A Business Card
        """

        item_data = CardGenerator._prompt_common_information()
        company = input("Enter company name or person's name: ")
        address = input("Enter the address of the business: ")
        phone = input("Enter the phone number: ")

        return BusinessCard(item_data, company, address, phone)

    @staticmethod
    def generate_item():
        """
        Prompts the user with a menu asking them to create either a
        credit card, rewards card, ID card or business card.
        :return: A Card
        """
        print("\nTypes of Cards to Add")
        print("--------------")
        print("1. Credit Card")
        print("2. Rewards/ Points Card")
        print("3. ID Card")
        print("4. Business Card")
        print("5. Miscellaneous Card")
        print("6. Go back")
        user_input = int(input("What item would you like to add (1-5)?"))

        new_item = None
        if user_input == 1:
            new_item = CardGenerator.generate_creditcard()
        elif user_input == 2:
            new_item = CardGenerator.generate_rewardscard()
        elif user_input == 3:
            new_item = CardGenerator.generate_idcard()
        elif user_input == 4:
            new_item = CardGenerator.generate_businesscard()
        elif user_input == 6:
            pass
        else:
            print("Invalid choice entered.")
        return new_item
