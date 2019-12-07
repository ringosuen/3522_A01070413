"""
Main driver class to run the program from the terminal.
"""
import argparse
import moves


def setup_request_commandline():
    """
    Setup request commandline
    :return: type of request, info, expanded, output
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("request", help="enter either pokemon, ability, "
                                        "or moves, you want to see")
    parser.add_argument("info", help="enter either the pokemon, ability, "
                                     "or move")
    parser.add_argument("-e", "--expanded", action="store_true",
                        help="View expanded list of certain stats")
    parser.add_argument("-o", "--output", help="Default out put is console.")
    try:
        args = parser.parse_args()
        # print(args.__dict__)
        type_of_request = args.request
        second_position = args.info
        pokedex_state = args.expanded
        pokedex_output = args.output
        # print(type_of_request)
        # print(second_position)
        return type_of_request, second_position, pokedex_state, pokedex_output
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class HandleRequest:
    """
    Chooses whether request input was a string or a text file.
    """

    @classmethod
    def process_single_string(cls):
        """
        Responsible for processing a single string entry. Chooses
        either Move, Pokemon or Ability request. Then checks for whether
        it needs to be expanded and where it should be outputted.
        :return: Response from the request.
        """
        request = setup_request_commandline()

        if request[0].lower() == "move" and request[3] is None:
            print("Reading move input, outputting to console")
            generate_move = moves.Moves.create_move_object(request[1])
            print(generate_move)

        elif request[0].lower() == "move" and request[3] is not None:
            generate_move = moves.Moves.create_move_object(request[1])
            print("Writing Output to file")
            with open(request[3], mode="a") \
                    as output_file:
                output_file.write(str(generate_move))
            return generate_move

        elif request[0] == "pokemon" and request[3] is None:
            print("Reading Pokemon input, outputting to console")
            generate_pokemon = moves.Pokemon.create_pokemon_object(request[1])
            print(generate_pokemon[0])
            print(f"{generate_pokemon[0].name.title()} Stats:")
            for stats in generate_pokemon[0].stats:
                print(stats)
            print(f"\n{generate_pokemon[0].name.title()} "
                  f"Moves and Level Learnt:")
            for move_, level in generate_pokemon[0].moves:
                print(f"{move_} learnt at {level}")
            if request[2] is True:
                moves.Pokemon.create_expanded_stats(request[1])
                moves.Pokemon.create_expanded_ability(request[1])
                moves.Pokemon.create_expanded_moves(request[1])

        elif request[0].lower() == "pokemon" and request[3] is not None:
            generate_pokemon = moves.Pokemon.create_pokemon_object(request[1])
            print("Writing Output to file")
            with open(request[3], mode="a") \
                    as output_file:
                output_file.write("\n" + str(generate_pokemon[0]))
                output_file.write("Stats:")
                for stats in generate_pokemon[0].stats:
                    output_file.write(str(stats))
                output_file.write("\nMoves and Level Learnt:")
                for move_, level in generate_pokemon[0].moves:
                    output_file.write("\n-" + str(move_) + " learnt at "
                                      + str(level))
            if request[2] is True:
                moves.Pokemon.create_expanded_stats(request[1])
                moves.Pokemon.create_expanded_ability(request[1])
                moves.Pokemon.create_expanded_moves(request[1])

        elif request[0].lower() == "ability" and request[3] is None:
            print("Reading input, outputting to console")
            generate_ability = moves.Ability.create_ability_object(request[1])
            print(generate_ability)
            return generate_ability
        elif request[0].lower() == "ability" and request[3] is not None:
            generate_ability = moves.Ability.create_ability_object(request[1])
            with open(request[3], mode="a") \
                    as output_file:
                output_file.write("\n" + str(generate_ability))

        else:
            print("Not a valid mode")

    @classmethod
    def process_text_file(cls, text_file):
        """
        Processes all text file inputs. Checks to see if it should output
        to the console or to an external file.
        :param text_file:
        """
        request = setup_request_commandline()
        if request[0].lower() == "move" and request[3] is None:
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                # print(file_text)
                move_list = [move.strip() for move in file_text]
            generate_moves = \
                moves.Moves.create_multiple_move_objects(move_list)
        elif request[0].lower() == "move" and request[3] is not None:
            print("Writing input_file to output file data")
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                move_list = [move.strip() for move in file_text]
            generate_moves = \
                moves.Moves.create_multiple_move_objects(move_list)

        elif request[0].lower() == "ability" and request[3] is None:
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                ability_list = [move.strip() for move in file_text]
                moves.Ability.create_multiple_ability_objects(ability_list)

        elif request[0].lower() == "ability" and request[3] is not None:
            print("Writing input_file to output file data")
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                ability_list = [move.strip() for move in file_text]
                moves.Ability.create_multiple_ability_objects(ability_list)

        elif request[0].lower() == "pokemon" and request[3] is None:
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                ability_list = [move.strip() for move in file_text]
                moves.Pokemon.create_multiple_pokemon_objects(ability_list)

        elif request[0].lower() == "pokemon" and request[3] is not None:
            print("Writing input_file to output file data")
            with open(text_file, mode="r") as move_file:
                file_text = move_file.readlines()
                ability_list = [move.strip() for move in file_text]
                moves.Pokemon.create_multiple_pokemon_objects(ability_list)


def main():
    """
    The main will do a simple check of whether the argument given is a
    single string or a text file input.
    """
    pokedex = HandleRequest()
    request = setup_request_commandline()

    if request[1].endswith(".txt"):
        print("Mode: Using text file mode")
        pokedex.process_text_file(request[1])
    elif request[1].endswith(".txt") is False:
        print("Mode: Single string mode, not text file")
        pokedex.process_single_string()

    # print(request[0])
    # print(request[1])
    # print(request[2])
    # print(request[3])
    # if request[3] is None and request[2] is True:
    #     print("Single String + Expansion")
    # elif request[3] is None:
    #     print("\nMode Detected: Single String + No Expansion")
    #     pokedex.process_single_string()
    # elif request[3] is not None and request[2] is True:
    #     print("Text File + expansion")
    # else:
    #     pokedex.process_text_file()


if __name__ == '__main__':
    main()
