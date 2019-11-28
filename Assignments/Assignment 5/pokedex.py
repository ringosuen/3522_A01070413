"""
Main driver class to run the program from the terminal.
"""
import argparse
import moves


def setup_request_commandline():
    """
    Setup request commandline
    :return: type of request, second_position
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("request", help="enter either pokemon, ability, "
                                        "or moves, you want to see")
    parser.add_argument("info", help="enter either the pokemon, ability, "
                                     "or move")
    # parser.add_argument("-e", "--expanded", default="print", help="View
    #                                          expanded list of certain stats")
    # parser.add_argument("-o", "--output", help="Default out put is console.")
    args = parser.parse_args()
    type_of_request = args.request
    second_position = args.info
    # print(type_of_request)
    # print(second_position)
    return type_of_request, second_position


class HandleRequest:

    @classmethod
    def process_single_string(cls):
        request = setup_request_commandline()
        if request[0] == "move":
            print("USING CREATE MOVE METHOD")
            generate_move = moves.Moves.create_move_object(request[1])
            print(generate_move)
            return generate_move

        elif request[0] == "pokemon":
            print("USING CREATE POKEMON METHOD")

        elif request[0] == "ability":
            print("USING ABILITY METHOD")

    def process_text_file(self):
        pass


def main():
    test = HandleRequest.process_single_string()


if __name__ == '__main__':
    main()
