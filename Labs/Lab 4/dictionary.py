import json
from file_handler import FileHandler, FileExtensions


class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def query_definition(self, word):
        # if word in self.dictionary:
        return f"{word} : {self.dictionary.get(word)}"

        #use alt word = word and make upper and lower cases

    def load_dictionary(self, filepath):
        data = FileHandler.load_data(filepath, FileExtensions.JSON)
        # filepath = open(filepath)
        # data = json.load(filepath)
        #
        # filepath.close()
        for (key, value) in data.items():
            self.dictionary.update({key: value})


def main():
    # read_sample_txt_with()
    # FileHandler.read_json()
    # print(dict.dictionary)
    # dict.load_dictionary("data.json")

    dict = Dictionary()
    dict.load_dictionary("data.json")

    print(dict.query_definition("interior"))


if __name__ == '__main__':
    main()
