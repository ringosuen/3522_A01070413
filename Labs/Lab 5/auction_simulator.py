import random


class Auction:
    def __init__(self, bidders, item, starting_price):
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
    '''
    this is the core!!!!
    '''

    def __init__(self, highest_current_bid):
        self.bidder = []
        self.highest_current_bid = highest_current_bid
        self.highest_bidder = "starting price"

    def execute_callbacks(self):
        """
        Executes all the callbacks in the list of observer callbacks.
        Passes the current light state as the argument to these
        callbacks.
        """
        for observer in self.bidder:
            observer(self)


class Bidders:
    """
    the observer to the auctions being placed.
    """

    def __init__(self, name, budget, bid_increase_perc):
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
        passed around as functions. this method can accept any number
        of parameters.
        :param message: a string
        """
        if self is auctioneer.highest_bidder:
            return
        if auctioneer.highest_current_bid * self.bid_increase_perc > self.budget:
            return
        if self.bid_probability > 0.5:
            return
        print(
            f"{self.name} bidded: ${auctioneer.highest_current_bid * self.bid_increase_perc} in response to"
            f" {auctioneer.highest_bidder}'s ${auctioneer.highest_current_bid}")
        auctioneer.highest_current_bid = auctioneer.highest_current_bid * self.bid_increase_perc
        auctioneer.highest_bidder = self
        self.highest_bid = auctioneer.highest_current_bid

    def react_to_price(self, traffic_light):
        pass


def main():
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

    print(f"/nHighest Bidder: ")

    print("/nHighest Bids Per bidder: ")
    for bidder in a1.bidder:
        print(f"{bidder.name}, {bidder.highest_bid}")


if __name__ == '__main__':
    main()
