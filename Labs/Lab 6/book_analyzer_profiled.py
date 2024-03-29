"""
This module is the profiled version of the badly written code. Here the
overall structure of the badly written reamins, but it has been slightly
optimized by removing unnecessary .lower() implementations.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '')
            temp_text.append(temp_word)
        self.text = temp_text

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is not case sensitive. This method takes the longest!
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """

        # g_m = [item for item in word_list if item[0] == "M"]

        for a_word in word_list:
            if word == a_word.lower():
                return False
        return True

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text
        unique_words = []
        duplicate_words = []
        while temp_text:
            word = temp_text.pop().lower()
            if word not in duplicate_words:
                if self.is_unique(word, temp_text):
                    unique_words.append(word)
                else:
                    duplicate_words.append(word)
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == '__main__':
    main()
