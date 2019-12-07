"""
This Module houses the Pokemon, Ability, Moves and RequestApi classes.
It's purpose is to process the command given from the Pokedex Driver class.
"""
import aiohttp
import asyncio
import ssl
import json
import pokedex


class Pokemon:
    """
    Anything to do with a Pokemon object in in this class.
    Stats, abilities, moves can be expanded for further information
    """

    def __init__(self, name: str, id: int, height: int, weight: int,
                 stats: list, types: list, abilities: list, moves: list):
        """
        Initiates a Pokemon object.
        :param name: str
        :param id: int
        :param height: int
        :param weight: int
        :param stats: list
        :param types: list
        :param abilities: list
        :param moves: list
        """
        self.name = name
        self.id_ = id
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        return f"\nPokemon Name: {self.name.title()}\n" \
               f"Pokemon ID: {self.id_}\n" \
               f"Pokemon Height: {self.height} decimeters\n" \
               f"Pokemon Weight: {self.weight} hectograms\n" \
               f"Pokemon Type: {self.types}\n" \
               f"Pokemon Abilities: {self.abilities}\n"

    @classmethod
    def create_pokemon_object(cls, pokemon_name_: str):
        """
        Creates a pokemon object
        :param pokemon_name_:
        :return: Pokemon
        """
        pokemon_object = \
            asyncio.run(
                RequestApi.process_single_pokemon_request(pokemon_name_))
        pokemon_dump = json.dumps(pokemon_object)
        pokemon = json.loads(pokemon_dump)

        pokemon_name = pokemon["name"]
        pokemon_id = pokemon["id"]
        pokemon_height = pokemon["height"]
        pokemon_weight = pokemon["weight"]
        stat_name = [item["stat"]["name"] for item in pokemon["stats"]]
        base_stat = [item["base_stat"] for item in pokemon["stats"]]

        pokemon_stats = list(zip(stat_name, base_stat))
        pokemon_type = [item["type"]["name"] for item in pokemon["types"]]
        pokemon_abilities = [item["ability"]["name"] for item in
                             pokemon["abilities"]]

        move = [item1["move"]["name"] for item1 in pokemon["moves"]]
        level = [item1["version_group_details"][0]["level_learned_at"] for
                 item1 in pokemon["moves"]]
        moves = list(zip(move, level))

        stat_url = [item["stat"]["url"] for item in pokemon["stats"]]
        move_url = [item1["move"]["url"] for item1 in pokemon["moves"]]
        ability_url = [item["ability"]["url"] for item in pokemon["abilities"]]

        final_pokemon_object = Pokemon(pokemon_name,
                                       pokemon_id,
                                       pokemon_height,
                                       pokemon_weight,
                                       pokemon_stats,
                                       pokemon_type,
                                       pokemon_abilities,
                                       moves)

        return final_pokemon_object, ability_url, stat_url, move_url

    @classmethod
    def create_multiple_pokemon_objects(cls, pokemon_name: list):
        """
        Creates multiple pokemon objects
        :param pokemon_name:
        :return: Pokemon
        """
        request = pokedex.setup_request_commandline()
        async_move = \
            asyncio.run(
                RequestApi.process_multiple_pokemon_requests(pokemon_name))
        string_convert = json.dumps(async_move)
        pokemon_convert_json = json.loads(string_convert)

        print("\n")
        for pokemon in pokemon_convert_json:
            pokemon_name = pokemon["name"]
            pokemon_id = pokemon["id"]
            pokemon_height = pokemon["height"]
            pokemon_weight = pokemon["weight"]
            stat_name = [item["stat"]["name"] for item in pokemon["stats"]]
            base_stat = [item["base_stat"] for item in pokemon["stats"]]

            pokemon_stats = list(zip(stat_name, base_stat))
            pokemon_type = [item["type"]["name"] for item in pokemon["types"]]
            pokemon_abilities = [item["ability"]["name"] for item in
                                 pokemon["abilities"]]

            move = [item1["move"]["name"] for item1 in pokemon["moves"]]
            level = [item1["version_group_details"][0]["level_learned_at"] for
                     item1 in pokemon["moves"]]
            moves = list(zip(move, level))

            final_pokemon_object = Pokemon(pokemon_name,
                                           pokemon_id,
                                           pokemon_height,
                                           pokemon_weight,
                                           pokemon_stats,
                                           pokemon_type,
                                           pokemon_abilities,
                                           moves)
            if request[0].lower() == "pokemon" and request[3] is None:
                print(final_pokemon_object)
                print(f"{final_pokemon_object.name.title()} Stats:")
                for stats in final_pokemon_object.stats:
                    print(stats)
                print(f"\n{final_pokemon_object.name.title()} "
                      f"Moves and Level Learnt:")
                for move_, level in final_pokemon_object.moves:
                    print(f"{move_} learnt at {level}")
            if request[0].lower() == "pokemon" and request[3] is not None:
                with open(request[3], mode="a") \
                        as output_file:
                    output_file.write("\n")
                    output_file.write(str(final_pokemon_object))
                    output_file.write("Stats:")
                    for stats in final_pokemon_object.stats:
                        output_file.write(str(stats))
                    output_file.write("\nMoves and Level Learnt:")
                    for move_, level in final_pokemon_object.moves:
                        output_file.write("\n-" + str(move_) + " learnt at "
                                          + str(level))

    @classmethod
    def create_expanded_ability(cls, pokemon_name__: str):
        """
        When expanded mode is applied, it will call this method to expand the
        ability URL taken from Pokemon Object.
        :param pokemon_name__:
        :return: Ability
        """
        request = pokedex.setup_request_commandline()
        ability_url = Pokemon.create_pokemon_object(pokemon_name__)
        ability_url_list = ability_url[1]
        async_ability_expanded = \
            asyncio.run(
                RequestApi.expanded_process_multiple_pokemon_requests(
                    ability_url_list))
        ability_expanded_dump = json.dumps(async_ability_expanded)
        ability_expanded_query = json.loads(ability_expanded_dump)
        print("\n---------------"
              "EXPANDED ABILITY INCLUDED-----------------------------")
        for ability in ability_expanded_query:
            ability_name = ability["name"]
            ability_id = ability["id"]
            ability_gen = ability["generation"]["name"]
            ability_long_effect = ability["effect_entries"][0]["effect"]
            ability_short_effect = ability["effect_entries"][0]["short_effect"]
            ability_pokemon = "\n-".join([item["pokemon"]["name"] for item in
                                          ability["pokemon"]])
            final_ability_object = Ability(ability_name, ability_id,
                                           ability_gen,
                                           ability_long_effect,
                                           ability_short_effect,
                                           ability_pokemon)
            if request[3] is None:
                print(final_ability_object)
            elif request[3] is not None:
                with open(request[3], mode="a") as output_file:
                    output_file.write("\n\n-----EXPANDED ABILITY-----\n")
                    output_file.write(str(final_ability_object))
    @classmethod
    def create_expanded_stats(cls, pokemon_name_1: str):
        """
        Expandes the stats of each Pokemon object using the Stats URL.
        :param pokemon_name_1:
        :return: Stats
        """
        request = pokedex.setup_request_commandline()
        stats_url = Pokemon.create_pokemon_object(pokemon_name_1)
        stats_url_list = stats_url[2]
        async_stats_expanded = \
            asyncio.run(
                RequestApi.expanded_process_multiple_pokemon_requests(
                    stats_url_list))
        stats_expanded_dump = json.dumps(async_stats_expanded)
        stats_expanded_query = json.loads(stats_expanded_dump)
        print("\n---------------"
              "EXPANDED STATS INCLUDED-----------------------------")
        for stat in stats_expanded_query:
            stat_name = stat["name"]
            stat_id = stat["id"]
            stat_is_battle_only = stat["is_battle_only"]
            final_stat_object = Stats(stat_name, stat_id, stat_is_battle_only)
            # print(final_stat_object)
            # print(request[2])
            if request[3] is None:
                print(final_stat_object)
            elif request[3] is not None:
                with open(request[3], mode="a") as output_file:
                    output_file.write("\n\n-----EXPANDED STAT-----\n")
                    output_file.write(str(final_stat_object))

    @classmethod
    def create_expanded_moves(cls, pokemon_name_2: str):
        """
        Exapnds the moves of each Pokemon using the move URL. Crerates
        a move object.
        :param pokemon_name_2:
        :return: Move
        """
        request = pokedex.setup_request_commandline()
        moves_url = Pokemon.create_pokemon_object(pokemon_name_2)
        moves_url_list = moves_url[3]
        async_ability_expanded = \
            asyncio.run(
                RequestApi.expanded_process_multiple_pokemon_requests(
                    moves_url_list))
        ability_expanded_dump = json.dumps(async_ability_expanded)
        ability_expanded_query = json.loads(ability_expanded_dump)
        print("\n---------------EXPANDED MOVES INCLUDED----"
              "-------------------------")
        for move in ability_expanded_query:
            move_name = move["name"]
            move_id = move["id"]
            move_gen = move["generation"]["name"]
            move_accuracy = move["accuracy"]
            move_pp = move["pp"]
            move_power = move["power"]
            move_type = move["type"]["name"]
            move_damage_class = move["damage_class"]["name"]
            move_short_effect = move["effect_entries"][0]["short_effect"]
            final_move_object = Moves(move_name, move_id, move_gen,
                                      move_accuracy,
                                      move_pp,
                                      move_power, move_type, move_damage_class,
                                      move_short_effect)
            if request[3] is None:
                print(final_move_object)
            elif request[3] is not None:
                with open(request[3], mode="a") as output_file:
                    output_file.write("\n\n-----EXPANDED MOVE-----\n")
                    output_file.write(str(final_move_object))


class Stats:
    """
    This is the stats field of a Pokemon.
    """
    def __init__(self, stat_name, stat_id, is_battle_only):
        self.stat_name = stat_name
        self.stat_id = stat_id
        self.is_battle_only = is_battle_only

    def __str__(self):
        return f"\nStat Name: {self.stat_name.title()}\n" \
               f"Stat ID: {self.stat_id}\n" \
               f"Is Battle Only: {self.is_battle_only}"


class Ability:
    """
    This is the ability and it's the attributes. It is not expandable.
    """
    def __init__(self, name: str, id: int, generation: str, effect: str,
                 short_effect: str, pokemon: str):
        self.name = name
        self.id_ = id
        self.gen = generation
        self.effect = effect
        self.short_effect = short_effect
        self.pokemon = pokemon

    def __str__(self):
        return f"\nAbility Name: {self.name.title()}\n" \
               f"Ability ID: {self.id_}\n" \
               f"Ability Generation: {self.gen}\n" \
               f"Long Effect: {self.effect}\n" \
               f"\n\nShort Effect: {self.short_effect}\n" \
               f"\nPokemon that has this ability " \
               f"listed below:\n-{self.pokemon.title()}\n"

    @classmethod
    def create_ability_object(cls, ability_name_: str):
        """
        Creates one ability object.
        :param ability_name_:
        :return: Ability
        """
        ability_object = \
            asyncio.run(
                RequestApi.process_single_ability_request(ability_name_))
        dump = json.dumps(ability_object)
        ability = json.loads(dump)

        ability_name = ability["name"]
        ability_id = ability["id"]
        ability_gen = ability["generation"]["name"]
        ability_long_effect = ability["effect_entries"][0]["effect"]
        ability_short_effect = ability["effect_entries"][0]["short_effect"]
        ability_pokemon = "\n-".join([item["pokemon"]["name"] for item in
                                      ability["pokemon"]])

        final_ability_object = Ability(ability_name, ability_id, ability_gen,
                                       ability_long_effect,
                                       ability_short_effect,
                                       ability_pokemon)

        return final_ability_object

    @classmethod
    def create_multiple_ability_objects(cls, ability_name_: list):
        """
        Creates multiple ability objects.
        :param ability_name_:
        :return: Ability : list
        """
        request = pokedex.setup_request_commandline()
        async_move = \
            asyncio.run(
                RequestApi.process_multiple_ability_requests(ability_name_))
        string_convert = json.dumps(async_move)
        ability_convert_json = json.loads(string_convert)

        print("\n")
        for ability in ability_convert_json:
            ability_name = ability["name"]
            ability_id = ability["id"]
            ability_gen = ability["generation"]["name"]
            ability_long_effect = ability["effect_entries"][0]["effect"]
            ability_short_effect = ability["effect_entries"][0]["short_effect"]
            ability_pokemon = "\n-".join([item["pokemon"]["name"] for item in
                                          ability["pokemon"]])

            final_ability_object = Ability(ability_name, ability_id,
                                           ability_gen,
                                           ability_long_effect,
                                           ability_short_effect,
                                           ability_pokemon)
            if request[0].lower() == "ability" and request[3] is None:
                print(final_ability_object)
            if request[0].lower() == "ability" and request[3] is not None:
                with open(request[3], mode="a") \
                        as output_file:
                    output_file.write(str(final_ability_object))


class Moves:
    """
    This is the Moves class that contains all the attributes needed for Moves.
    """

    def __init__(self, name: str, id: int, generation: str, accuracy: int,
                 pp: int, power: int, type_: str, damage_class: str,
                 effect: str):
        self.name = name
        self.id_ = id
        self.gen = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type_ = type_
        self.damage_class = damage_class
        self.effect = effect

    def __str__(self):
        return f"\nMove Name: {self.name.title()}\n" \
               f"Move ID: {self.id_}\n" \
               f"Move Generation: {self.gen}\n" \
               f"Move Accuracy: {self.accuracy}\n" \
               f"Move PP: {self.pp}\n" \
               f"Move Power: {self.power}\n" \
               f"Move Type: {self.type_}\n" \
               f"Special or Physical: {self.damage_class}\n" \
               f"Short Effect: {self.effect}\n"

    @classmethod
    def create_move_object(cls, move_name_: str):
        """
        Creates one move object.
        :param move_name_:
        :return: Move
        """
        move_object = \
            asyncio.run(RequestApi.process_single_move_request(move_name_))
        dump = json.dumps(move_object)
        move = json.loads(dump)

        move_name = move["name"]
        move_id = move["id"]
        move_gen = move["generation"]["name"]
        move_accuracy = move["accuracy"]
        move_pp = move["pp"]
        move_power = move["power"]
        move_type = move["type"]["name"]
        move_damage_class = move["damage_class"]["name"]
        move_short_effect = move["effect_entries"][0]["short_effect"]

        final_object = Moves(move_name, move_id, move_gen, move_accuracy,
                             move_pp,
                             move_power, move_type, move_damage_class,
                             move_short_effect)

        return final_object

    @classmethod
    def create_multiple_move_objects(cls, move_name_: list):
        """
        Creates multiple Move objects into a list.
        :param move_name_:
        :return: Move : list
        """
        request = pokedex.setup_request_commandline()
        async_move = \
            asyncio.run(RequestApi.process_multiple_move_requests(move_name_))
        string_convert = json.dumps(async_move)
        moves_convert_json = json.loads(string_convert)

        print("\n")
        for move in moves_convert_json:
            move_name = move["name"]
            move_id = move["id"]
            move_gen = move["generation"]["name"]
            move_accuracy = move["accuracy"]
            move_pp = move["pp"]
            move_power = move["power"]
            move_type = move["type"]["name"]
            move_damage_class = move["damage_class"]["name"]
            move_short_effect = move["effect_entries"][0]["short_effect"]
            final_move_object = Moves(move_name, move_id, move_gen,
                                      move_accuracy,
                                      move_pp,
                                      move_power, move_type, move_damage_class,
                                      move_short_effect)
            if request[0].lower() == "move" and request[3] is None:
                print(final_move_object)
            if request[0].lower() == "move" and request[3] is not None:
                with open(request[3], mode="a") \
                        as output_file:
                    output_file.write(str(final_move_object))


class RequestApi:
    """
    All the async methods and API related code is in this class.
    """

    @classmethod
    async def get_data(cls, id_: str, url: str,
                       session: aiohttp.ClientSession) -> dict:
        """
        Async coroutine that executes GET http request. Gets information from
        the URL. The response will be converted to a json type. Uses to await
        for the async processes.
        :param id_: an int
        :param url: a string, the unformatted url (missing parameters)
        :param session: a HTTP session
        :return: a dict, json representation of response.
        """
        target_url = url.format(id_)
        response = await session.request(method="GET", url=target_url,
                                         ssl=ssl.SSLContext())
        # print("Response object from aiohttep:\n", response)
        # print("Response object type:\n", type(response))
        json_dict = await response.json()
        return json_dict

    @classmethod
    async def process_single_pokemon_request(cls, id_) -> dict:
        """
        Processes a single string input as "id" field. Must be a Pokemon name.
        A async coroutine that can await another async coroutine.
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}"

        try:
            async with aiohttp.ClientSession() as session:
                response = await RequestApi.get_data(id_, url, session)

                # print(response)
                return response
        except Exception:
            print("Invalid Pokemon Entered! Try Again")
            exit()

    @classmethod
    async def process_single_ability_request(cls, id_) -> dict:
        """
        Processes a single ability name and requests the info from the url
        given with the appropriate parameter id.
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/ability/{}"

        try:
            async with aiohttp.ClientSession() as session:
                response = await RequestApi.get_data(id_, url, session)

                return response
        except Exception:
            print("Invalid Ability Entered! Try Again")
            exit()


    @classmethod
    async def process_single_move_request(cls, id_) -> dict:
        """
        Processes a single move name and requests the info from the url
        given with the appropriate parameter id.
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/move/{}"
        try:
            async with aiohttp.ClientSession() as session:
                response = await RequestApi.get_data(id_, url, session)

                # print(response)
                return response
        except Exception:
            print("Invalid Move Entered! Try Again")
            exit()

    @classmethod
    async def process_multiple_move_requests(cls, requests: list) -> list:
        """
        Processes a multiple move names and requests the info from the url
        given with the appropriate parameter id.
        Uses asyncio.gather to run multiple async coroutines concurrently.
        :param requests: a list of str
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/move/{}"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [RequestApi.get_data(id_, url, session)
                                for id_ in requests]
            responses = await asyncio.gather(*async_coroutines)
            # for response in responses:
            #     print(response)
            return responses

    @classmethod
    async def process_multiple_ability_requests(cls, requests: list) -> list:
        """
        Processes a multiple ability names and requests the info from the url
        given with the appropriate parameter id.
        Uses asyncio.gather to run multiple async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/ability/{}"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [RequestApi.get_data(id_, url, session)
                                for id_ in requests]
            responses = await asyncio.gather(*async_coroutines)
            # for response in responses:
            #     print(response)
            return responses

    @classmethod
    async def process_multiple_pokemon_requests(cls, requests: list) -> list:
        """
        Processes a multiple pokemon names and requests the info from the url
        given with the appropriate parameter id.
        Uses asyncio.gather to run multiple async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [RequestApi.get_data(id_, url, session)
                                for id_ in requests]
            responses = await asyncio.gather(*async_coroutines)
            # for response in responses:
            #     print(response)
            return responses

    @classmethod
    async def expanded_process_multiple_pokemon_requests(cls,
                                            requests: list) -> list:
        """
        Processes a multiple queries based on an URL. Requests the
        info from the url given.
        Uses asyncio.gather to run multiple async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "{}"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [RequestApi.get_data(id_, url, session)
                                for id_ in requests]
            responses = await asyncio.gather(*async_coroutines)
            # for response in responses:
            #     print(response)
            return responses


def main():
    pass
    # Pokemon.create_expanded_moves("vileplume")
    # Pokemon.create_expanded_ability("vileplume")
    # Pokemon.create_expanded_stats("vileplume")

    # flamethrower = Moves.create_move_object("flamethrower")
    # print(flamethrower)
    #
    # intimidate = Ability.create_ability_object("1")
    # print(intimidate)
    #
    # ditto = Pokemon.create_pokemon_object("vileplume")
    # print(ditto[0])


if __name__ == '__main__':
    main()
