"""
A chain of responsibility lab. Runs through the behaviour of the pattern by
validating checks before it either decrypts or encrypts something. Run
through the command line.
"""

import argparse
import abc
import enum
from des import DesKey


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.
    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class BaseCryptoHandler(abc.ABC):
    """
    Baseclass for all handlers that handle encryption and decryption.
    """

    def __init__(self):
        self.encryption_start_handler = EncryptHandler
        self.decryption_start_handler = DecryptHandler

    # def execute_request(self, request: Request):
    #     if request.encryption_state == CryptoMode.EN:
    #         encrypttest1 = EncryptHandler()
    #         encrypttest1.set_decryption_start_handler(request)
    #     if request.encryption_state == CryptoMode.DE:
    #         decrypttest2 = DecryptHandler()
    #         decrypttest2.set_decryption_start_handler(request)
    #         # decrypttest2.handle_request(request)

    @abc.abstractmethod
    def handle_request(self, request: Request):
        """
        Each handler would have a specific implementation of either encryption
        or decryption.
        """
        pass

    def set_encryption_start_handler(self, handler):
        self.encryption_start_handler = handler

    def set_decryption_start_handler(self, handler):
        self.decryption_start_handler = handler


class EncryptHandler(BaseCryptoHandler):
    """
     This handler ensures that the encryption is done properly. Whether it
     is a file or a string data.
     """

    def handle_request(self, request: Request):
        """
        Checks to see if the key exist. If there is data_input then it
        will convert it to Bytes, encrypting it.
        :param request : Request
        """
        print("Encryption Request")

        key0 = request.key.encode("utf-8")

        if request.encryption_state == CryptoMode.EN:
            if request.key and request.data_input:
                print("Converting data string to bytes")
                key1 = DesKey(key0)
                encoded_input = request.data_input.encode("utf-8")
                request.result = key1.encrypt(encoded_input, padding=True)
                print(request.result)
                return request.result
            if request.key and request.input_file:
                print("Converting string file to encrypted file")
                with open(request.input_file, mode="r") \
                        as encrypt_input_file:
                    key1 = DesKey(key0)
                    file_text = encrypt_input_file.readlines()
                    file_text1 = str(file_text).encode("utf-8")
                    request.result = key1.encrypt(file_text1, padding=True)
                with open("encryptedFile.txt", mode="wb") \
                        as output_file:
                    output_file.write(request.result)
        if request.data_input and request.input_file:
            print("Data cannot be encrypted, cannot contain both")
        else:
            return "Data cannot be encrypted"


class DecryptHandler(BaseCryptoHandler):
    """
     This handler ensures that the decryption is done properly. Whether it
     is a file or a string data.
     """

    def handle_request(self, request: Request):
        """
        Checks to see if there is a encryptedFile to decrypt. Or it also
        decrypts a byte back to a string.
        """

        key0 = request.key.encode("utf-8")

        print("Decryption Request")

        if request.output and request.data_input:
            key1 = DesKey(key0)
            encoded_input = request.data_input.encode("utf-8")
            request.result = key1.encrypt(encoded_input, padding=True)
            print(request.result)
            print("========================")
            print("Decoding the data byte:")
            decoded_byte = key1.decrypt(request.result, padding=True)
            decoded_string = decoded_byte.decode("utf-8")
            print(decoded_byte)
            print(decoded_string)
        elif request.output:
            with open(request.input_file, mode="rb") \
                    as encrypt_input_file:
                key1 = DesKey(key0)
                file_text = encrypt_input_file.readlines()
                print(file_text[0])
                file_text1 = key1.decrypt(file_text[0])
                print(file_text1)
                decrypted_file = file_text1.decode("utf-8")
                print(decrypted_file)
            with open("decryptedFile.txt", mode="w") as output_file:
                output_file.write(decrypted_file)


def main(request: Request):
    """
    Checks whether the mode is EN or DE.
    """
    if request.encryption_state == CryptoMode.EN:
        encrypttest1 = EncryptHandler()
        encrypttest1.handle_request(request)
    if request.encryption_state == CryptoMode.DE:
        decrypttest2 = DecryptHandler()
        decrypttest2.handle_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
