"""
This module houses the main method that cues for user input to search for a
word and gets the definition of the word. Uses the file_handler class and
loads and writes data externally to a .txt file.
"""
import difflib
from file_handler import FileHandler, FileExtensions


class Dictionary:
    """
    The dictionary class is responsible for loading data into a dictionary
    and looking up the definition of a word.
    """
    def __init__(self):
        """initialize an empty dictionary"""
        self.dictionary = {}

    def query_definition(self, word):
        """
        Looks up the definition of a word. Also searches for similar words
        when the particular word is not found.
        :param word: a string
        :return: self.dictionary.get(word)
        """
        word = word.lower()
        if word not in self.dictionary:
            print("Here are some similar words: ")
            print(difflib.get_close_matches(word, self.dictionary))
        else:
            return self.dictionary.get(word)

    def load_dictionary(self, filepath):
        """
        Responsible for loading data into a dictionary.
        :param filepath: a string
        """
        try:
            data = FileHandler.load_data(filepath, FileExtensions.JSON)

            for (key, value) in data.items():
                self.dictionary.update({key: value})
        except AttributeError as e:
            print(f"Attribute Error {e}")
            exit()


def main():
    """
    Loads the data.json file and asks user for input. Input is a word
    and the program will output the definition of the word. The user
    enter exitprogram to exit the program. Search of the word is not case
    sensitive. If the definition of the word is found, then it create a new
    existing .txt file and append new words to the file.
    """
    diction = Dictionary()
    diction.load_dictionary("data.json")

    while True:
        choice = (input("Enter A Word To Search:").lower())
        if choice == "exitprogram":
            exit()
        else:
            sentence = diction.query_definition(choice)
            if sentence is not None:
                print(diction.query_definition(choice))
                print("Writing to saved_words.txt")
                FileHandler.write_lines("saved_words.txt", "\n")
                FileHandler.write_lines("saved_words.txt", choice)
                FileHandler.write_lines("saved_words.txt", " : ")
                FileHandler.write_lines("saved_words.txt", sentence)
            else:
                print("Word does not exist")


if __name__ == '__main__':
    main()
