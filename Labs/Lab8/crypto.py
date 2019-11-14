import des
import argparse
import abc
import enum
import ast


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

    def __init__(self):
        self.encryption_start_handler = None
        self.decryption_start_handler = None

    def execute_request(self, request: Request):
        pass

    @abc.abstractmethod
    def handle_request(self, request: Request):
        pass

    # @abc.abstractmethod
    # def handle_crypto(self, form: EnrolmentApplicationForm) -> (str, bool):
    #     pass

    def set_encryption_start_handler(self, handler):
        self.encryption_start_handler = handler

    def set_decryption_start_handler(self, handler):
        self.decryption_start_handler = handler


class EncryptHandler(BaseCryptoHandler):

    def handle_request(self, request: Request):
        string_encrypt = request.data_input.encode("utf-8")
        # file_encrypt = request.input_file.encode("utf-8")
        print("Encryption Request")
        if request.data_input and request.input_file:
            print("Data cannot be encrypted, cannot contain both")
        if request.key and request.data_input:
            print("Converting string to bytes")
            print(string_encrypt)
        # if not self.encryption_start_handler:
        #     return "", True
        # return self.encryption_start_handler.execute_request(request)
        # else:
        #     return "Data cannot be encrypted", False

    # def encryption(self, string):
    #     byte_string = string.encode("utf-8")
    #     type(byte_string)
    #     print(byte_string)


class DecryptHandler(BaseCryptoHandler):

    def handle_request(self, request: Request):
        pass


# class Crypto:
#
#     def __init__(self):
#         self.encryption_start_handler = None
#         self.decryption_start_handler = None
#
#     def execute_request(self, request: Request):
#         pass


def main(request: Request):
    test_str = "this is hard coded please delete"
    test1 = EncryptHandler()
    test1.handle_request(request)
    # test1.encryption(test_str)



if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)