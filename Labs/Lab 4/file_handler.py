import json
from enum import Enum
from pathlib import Path


class FileExtensions(Enum):
    TXT = 1
    JSON = 2


class InvalidFileTypeError(Exception):
    def __init__(self, invalid_file_type_error):
        super.__init__(invalid_file_type_error)
        self.invalidFileType = invalid_file_type_error


class FileHandler:
    @staticmethod
    def load_data(path, file_type):
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
                raise FileNotFoundError("Can't find file.")
        except FileNotFoundError as e:
            print(f"File not Found {e}")
        except TypeError as e:
            print(f"Type error {e}")
        except AttributeError as e:
            print(f"Attribute Error {e}")

    @staticmethod
    def write_lines(path, lines):
        # print("Writing to saved_words.txt using write mode")
        with open(path, mode='a') as my_text_file:
            my_text_file.write(str(lines))

#
# def main():
#     pass
#     # read_sample_txt_with()
#     # FileHandler.read_json()
#     # FileHandler.load_data("data.json", FileExtensions.JSON)
#
#
# if __name__ == '__main__':
#     main()
