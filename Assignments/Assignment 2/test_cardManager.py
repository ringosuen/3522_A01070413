from unittest import TestCase
from card_handler import CardManager
from cards import Card, CreditCard, BusinessCard, IdCard, \
    RewardsCard, CardGenerator


class TestCardManager(TestCase):
    def test_add_card(self):
        """
        Unit test for adding a card. Tests if function works with
        will add an item to the card_list. Test will fail if the is empty.
        """
        card_test = CardManager()
        result = card_test.card_list
        card_test.add_card()
        for item in result:
            return item
        self.assertEqual(result, [1])

    def test_not_found_remove_card(self):
        """
        Unit test for not removing a card because it cannot find the name.
        :return: None
        """

        card_test = CardManager()
        # card_test.card_list = CreditCard("Remove me", "test", "test",
        #                                  "test", "test")
        result = card_test.remove_card("Remove Me")
        self.assertEqual(result, None)

    def test_not_found_search_card(self):
        """
        Unit test for not being able to find card.
        :return: None
        """
        card_test = CardManager()
        result = card_test.search_card("Find Me")
        self.assertEqual(result, None)

    def test_backup(self):
        pass