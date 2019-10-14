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
        pass

    def remove_card(self):
        """
        Removes a card from the database depending o
        :return:
        """

    def search_card(self):
        #FIGURE OUT FIND ITEMS BASED ON TITLE? CONTAINS TITLE?
        """
        Searches a card from the collection.
        :return: the searched card
        """

    def display_available_items(self):
        #NEED TO FIGURE OUT HOW TO DISPLAY BY TYPE!!! THIS WILL JUST DISPLAY EACH CARD IN A LIST
        """
        Display all the cards in the collection.
        """
        print("Card Collection")
        print("--------------", end="\n\n")
        for card_item in self.card_list:
            print(card_item)