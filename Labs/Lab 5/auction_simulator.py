"""
This module demonstrates the use of the Observer Design Pattern by
simulating an Auction between bidders.
"""
import random


class Auction:
    """
    This class represent an auction object. It is responsible for setting up
    and starting an auction for an item with a starting price.
    """
    def __init__(self, bidders, item, starting_price):
        """
        Initializes a new Auction with a list of bidders, item and starting
        price.
        :param bidders: list
        :param item: string
        :param starting_price: int
        """

        self.bidders = bidders
        self.item = item
        self.starting_price = starting_price

    def run_auction(self):
        """
        Starts the timer countdown. At the end of this countdown all the
        subscribed callbacks are executed.
        """
        pass


class Auctioneer:
    """
    The Auctioneer is the core that represents an auction of bidders.
    It is observed by other bidders otherwise known as observers. If the bid
    probability allows the bidder to keep bidding, then all the bidders would
    be notified.
    """

    def __init__(self, highest_current_bid):
        """
        initializes a new Auctioneer with the current highest current
        bid state. It also initializes an empty list of bidders.
        :param highest_current_bid: int
        """

        self.bidder = []
        self.highest_current_bid = highest_current_bid
        self.highest_bidder = "starting price"

    def execute_callbacks(self):
        """
        Executes all the callbacks in the list of observer callbacks.
        Passes the current bidder state as the argument to these
        callbacks.
        """
        for observer in self.bidder:
            observer(self)


class Bidders:
    """
    Represents a bidder which acts as an observer to the auctions being placed.
    """

    def __init__(self, name, budget, bid_increase_perc):
        """
        Initializes a new Bidder with name, budget and bid increase %.
        Bid probability is using a random value between 0,1.
        :param name: string
        :param budget: int
        :param bid_increase_perc: int
        """

        self.name = name
        self.budget = budget
        self.bid_probability = random.random()
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __str__(self):
        return f"{self.name}"

    def __call__(self, auctioneer):
        """
        This is the protocol that allows an object to be called and
        passed around as functions. This method accepts an auctioneer.
        :param auctioneer: an object
        """
        if self is auctioneer.highest_bidder:
            print(f"\nThe highest bidder is {self.name}"
                  f" with ${self.highest_bid}")
            return
        if auctioneer.highest_current_bid * self.bid_increase_perc \
                > self.budget:
            return
        # if self.bid_probability > 0.2:
        #     return
        print(
            f"{self.name} bidded: "
            f"${auctioneer.highest_current_bid * self.bid_increase_perc} "
            f"in response to"
            f" {auctioneer.highest_bidder}'s "
            f"${auctioneer.highest_current_bid}")
        auctioneer.highest_current_bid = \
            auctioneer.highest_current_bid * self.bid_increase_perc
        auctioneer.highest_bidder = self
        self.highest_bid = auctioneer.highest_current_bid


def main():
    """
    prompts for user input for an item and item price.
    prompts the user to enter amount of bidders there are. Then asks user
    to enter name, their budget and then bidder increase percentage.
    :return: a bidder list
    """
    bidders_list = []
    auction_item = input("What item is being auctioned? ")
    auction_price = float(input("What is the price of the item? "))
    num_people = int(input("How many people you want to add"))

    while len(bidders_list) < num_people:
        bidder_name = input("\nAdd a bidder's name: ")
        bidder_budget = float(
            input(f"Enter {bidder_name.capitalize()}'s budget: "))
        bidder_increase_percent = float(input(
            f"Enter {bidder_name.capitalize()}'s increasing bid percentage: "))
        bidder_increase_percent = bidder_increase_percent / 100.0

        bidder = Bidders(bidder_name, bidder_budget, bidder_increase_percent)

        bidders_list.append(bidder)

    auction = Auction(bidders_list, auction_item, auction_price)
    a1 = Auctioneer(auction.starting_price)
    a1.bidder = bidders_list

    temp_max = 0.0
    check_after = auction.starting_price
    while temp_max != check_after:
        a1.execute_callbacks()
        temp_max = check_after
        check_after = a1.highest_current_bid

    print("\nHighest Bids Per bidder: ")
    for bidder in a1.bidder:
        print(f"{bidder.name}, {bidder.highest_bid}")


if __name__ == '__main__':
    main()
