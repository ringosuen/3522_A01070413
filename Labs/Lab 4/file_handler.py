import json
from enum import Enum
from pathlib import Path


class FileExtensions(Enum):
    TXT = 1
    JSON = 2


class InvalidFileTypeError:
    pass


class FileHandler:
    @staticmethod
    def load_data(path, file_type):
        # try:
        my_file = Path(path)
        if my_file.is_file():
            if file_type.name == "JSON":
                with open(my_file, "r") as read_file:
                    data = json.load(read_file)
                    print(f"File Data: \n{data}")
                    return data

            elif file_type.name == "TXT":
                with open(my_file, mode='r') as my_text_file:
                    data = my_text_file.read()
                    print(f"File Data:\n{data}")
                    my_text_file.seek(0)
                    data = my_text_file.read()
                    print(f"Printing data after seeking to "
                          f"the beginning:\n {data}")
        else:
            raise FileNotFoundError("Can't find file.")

    # @staticmethod
    # def read_json():
    #     with open("data.json", "r") as read_file:
    #         data = json.load(read_file)
    #         # data = read_file.read()
    #
    #         for line in data:
    #             print(line)
    #         # print(f"File Data: \n{data}")

    # @staticmethod
    # def read_sample_txt_with():
    #     """
    #     Reads data from sample1.txt. This method utilizes the with block to
    #     do so. A with block allows us to safely conduct file operations. If
    #     there is any exception, the file is closed automatically. It also
    #     demonstrates how to reset the file pointer if we want to read
    #     multiple times.
    #     """
    #     print("\nReading the test.txt file using a with block")
    #     print("----------------------------------------------")
    #     with open("test.txt", mode='r') as my_text_file:
    #         data = my_text_file.read()
    #         print(f"File Data:\n{data}")
    #
    #         data = my_text_file.read()
    #         print(f"Printing Data again: {data}")
    #         my_text_file.seek(0)
    #         data = my_text_file.read()
    #         print(f"Printing data after seeking to the beginning:\n {data}")

    @staticmethod
    def write_lines(path, lines):
        print("Writing to saved_words.txt using write mode")
        with open(path, mode='w') as my_text_file:
            my_text_file.write(lines)

    def write_sample3_append_mode(*args):
        """
        Writes data to a file by opening the file in append mode. In this
        mode, if the file does not exist, it gets created. More importantly,
        if the file has any pre-existing data, opening the append mode will
        not overwrite this data. Any calls to file.write() will add the data
        to the end. (Unless you change the file pointer using file.seek()
        :param args: Variable list argument, any number of string arguments.
        """
        print("Writing tp saved_words.txt using append mode")
        with open("sample3.txt", mode='a') as my_text_file:
            for line in args:
                my_text_file.write(line)


def main():
    # read_sample_txt_with()
    # FileHandler.read_json()
    FileHandler.load_data("data.json", FileExtensions.JSON)


if __name__ == '__main__':
    main()
