"""
Main driver class to run the program from the terminal.
"""
import argparse
import moves

def setup_request_commandline():

    parser = argparse.ArgumentParser()
    parser.add_argument("request", help="enter either pokemon, ability, "
                                        "or moves, you want to see")
    parser.add_argument("info", help="enter either the pokemon, ability, "
                                     "or move")
    # parser.add_argument("--e", "--move", help="enter the move(s) you want to see")
    #
    # parser.add_argument("-s", "--string", help="The string of moves")
    args = parser.parse_args()
    type_of_request = args.request
    second_position = args.info
    # print(type_of_request)
    # print(second_position)
    return type_of_request, second_position

def single_string_info_generator():
    request = setup_request_commandline()
    if request[0] == "move":
        print("USING CREATE MOVE METHOD")
        test_1 = moves.Moves.create_move_object(request[1])
        print(test_1)


def main():
    test = single_string_info_generator()
    # request = setup_request_commandline()
    #
    # test_1 = moves.Moves.create_move_object(request[1])
    # print(test_1)

if __name__ == '__main__':
    main()
