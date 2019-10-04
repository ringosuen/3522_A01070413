"""
This module is responsible for reading a file and handles any error
with the the file type or file not being found. It also houses a write to file
method.
"""

import json
from enum import Enum
from pathlib import Path


class FileExtensions(Enum):
    """This is an Enum class for TXT and JSON extensions"""
    TXT = 1
    JSON = 2


class InvalidFileTypeError(Exception):
    """
    This class handles Invalid File Type Errors.
    """
    def __init__(self, invalid_file_type_error):
        """Initiliaze an invalid file type error exception"""
        super.__init__(invalid_file_type_error)
        self.invalidFileType = invalid_file_type_error


class FileHandler:
    """
    This class is to load data from file as well as writing to an external
    file.
    """
    @staticmethod
    def load_data(path, file_type):
        """
        Loads data based on the file called and the file type being either TXT
        or JSON. Also respinsible for raising any exceptions if they occur.
        :param path: a string
        :param file_type: an enum extension
        :return: data
        """
        my_file = Path(path)
        try:
            if my_file.is_file():
                if file_type.name == "JSON":
                    with open(my_file, "r") as read_file:
                        data = json.load(read_file)
                        # print(f"File Data: \n{data}")
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
                    raise InvalidFileTypeError("InvalidFileType")
            else:
                raise FileNotFoundError("Can't find file.")
        except InvalidFileTypeError as e:
            print("Invalid File Type")
        except FileNotFoundError as e:
            print(f"File not Found {e}")
        except TypeError as e:
            print(f"Type error {e}")
        except AttributeError as e:
            print(f"Attribute Error {e}")

    @staticmethod
    def write_lines(path, lines):
        """
        A method to write specified input and output it to an external file as
        a .txt file.
        :param path: a string
        :param lines: a string
        """
        with open(path, mode='a') as my_text_file:
            my_text_file.write(str(lines))
