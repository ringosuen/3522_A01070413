"""
This module houses all the necessary code for a creating a smurf list and
it's related functions.
"""


class Smurf:
    """
    This class contains all the implementation methods to manipulate
    a list and retrieve information from the created list.
    """

    def __init__(self, smurf_members):
        self.smurf_members = smurf_members

    def __len__(self):
        """
        returns the number of smurfs in the team
        :return: the length of the list
        """
        return len(self.smurf_members)

    def __contains__(self, item):
        """
        Should return true if the the name of the smurf
        is in the team list.
        :return: bool
        """
        found = False

        for person in self.smurf_members:
            if person == item:
                found = True
        return found

    def count(self, item):
        """
        Returns the number of occurrences that the item occurs.
        :param item: an int
        :return: count
        """
        return self.smurf_members.count(item)

    def index(self, item):
        """
        Returns the position of where the item is in the list.
        :param item: an int
        :return: index
        """
        return self.smurf_members.index(item)

    def __iter__(self):
        """
        Iterates through the list.
        :return: smurf_members
        """
        return iter(self.smurf_members)

    def __reversed__(self):
        """
        Reverses the list.
        :return: list reversed
        """
        return list(reversed(self.smurf_members))

    def __getitem__(self, key):
        """
        Returns the key of where the smurf is located.
        :param key: an int
        :return: smurf
        """
        return self.smurf_members[key]

    def __str__(self):
        smurf_list = ""
        for smurf in self.smurf_members:
            smurf_list += smurf + " "
        return f"Members: {smurf_list}"


def main():
    smurf_parade = Smurf(["Brainy", "Clumsy", "Smurlette", "Greedy", "Papa",
                          "Farmer", "Grouchy", "Clumsy"])

    print(smurf_parade)
    print(f"List reversed: {reversed(smurf_parade)}")
    print(smurf_parade)
    print(f"\nNumber of smurfs: {len(smurf_parade)}")
    print(f"\nIs Clumsy part of the Smurfs? {'Clumsy' in smurf_parade}")
    clumsy_count = smurf_parade.count("Clumsy")
    clumsy_index = smurf_parade.index("Papa")
    print(f"\nThe count of Clumsy is: {clumsy_count}\n")
    print(f"The first index of Papa is position: {clumsy_index}\n")
    print(f"Who's at position 4? {smurf_parade[3]}")
    print(f"Who's at position 5? {smurf_parade[4]}\n")
    print("Iterate through the list:")

    # i = iter(smurf_parade)
    # length = len(smurf_parade)
    # counter = 0
    # while counter < length:
    #     print(next(i))
    #     length -= 1

    for smurf in smurf_parade:
        print(smurf)

    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # smurf_parade.__iter__()


if __name__ == '__main__':
    main()
