import difflib

from file_handler import FileHandler, FileExtensions


class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def query_definition(self, word):

        if word not in self.dictionary:
            print(difflib.get_close_matches(word, self.dictionary))
        else:
            return self.dictionary.get(word)

    def load_dictionary(self, filepath):
        try:
            data = FileHandler.load_data(filepath, FileExtensions.JSON)

            for (key, value) in data.items():
                self.dictionary.update({key: value})
        except AttributeError as e:
            print(f"Attribute Error {e}")
            exit()


def main():
    dict = Dictionary()
    dict.load_dictionary("data.json")

    while True:
        choice = (input("Enter A Word To Search:").lower())
        if choice == "exitprogram":
            exit()
        else:
            sentence = dict.query_definition(choice)
            if sentence is not None:
                print(dict.query_definition(choice))
                print("Writing to saved_words.txt")
                FileHandler.write_lines("saved_words.txt", "\n")
                FileHandler.write_lines("saved_words.txt", choice)
                FileHandler.write_lines("saved_words.txt", " : ")
                FileHandler.write_lines("saved_words.txt", sentence)
            else:
                print("Word does not exist")


if __name__ == '__main__':
    main()
