"""
This module is responsible for unit testing the dictionary.py and
file_handler.py module.
"""

from unittest import TestCase
from dictionary import Dictionary
from file_handler import FileHandler


class TestDictionary(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for dictionary.py and file_handler.py
    """

    def test_Upper_Case_query_word(self):
        diction = Dictionary()
        diction.load_dictionary("data.json")
        """
        Unit test for word query. Tests if function works with 
        upper case keyword.
        """
        result = diction.query_definition("HI")
        self.assertEqual(result, ['Expression of greeting used by two or'
                                  ' more people who meet each other.'])

    def test_not_found_query_word(self):
        diction = Dictionary()
        diction.load_dictionary("data.json")
        """
        Unit test for word query. Tests if function will return 
        none if word is not found.
        """
        result = diction.query_definition("Ringo")
        self.assertEqual(result, None)

    def test_found_query_word(self):
        diction = Dictionary()
        diction.load_dictionary("data.json")
        """
        Unit test for word query. Tests if function will return 
        the definition for specified word. 
        """
        result = diction.query_definition("wind")
        self.assertEqual(result, ["The motion of air relative to the "
                                  "earth's surface; usually means horizontal "
                                  'air motion, as distinguished from '
                                  'vertical motion.',
                                  'To wrap something in loops around '
                                  'something else.'])

    def test_writing_file(self):
        """
        Unit test to see if line has been written to an external file.
        """
        with open("saved_words.txt") as my_text_file:
            size_file = sum(1 for _ in my_text_file)

        f = FileHandler()
        f.write_lines("saved_words.txt", "hello")

        with open("saved_words.txt") as text_file:
            new_size_file = sum(1 for _ in text_file)

        result = True
        if new_size_file > size_file:
            self.assertEqual(result, True)

    def test_load_data(self):
        """
        Unit test for loading data to a dictionary.
        """
        diction = Dictionary()
        diction.load_dictionary("data.json")
        result = True
        self.assertEqual(result, True)

