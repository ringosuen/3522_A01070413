import aiohttp
import asyncio
import ssl
import json
import pokedex


class Pokemon:
    """
    stats, abilities, moves can be expanded for further information
    """

    def __init__(self, name: str, id: int, height: int, weight: int,
                 stats: list, types: list, abilities: list, moves: list):
        self.name = name
        self.id_ = id
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    """modified one"""

    def __str__(self):
        return f"\nPokemon Name: {self.name.title()}\n" \
               f"Pokemon ID: {self.id_}\n" \
               f"Pokemon Height: {self.height} decimeters\n" \
               f"Pokemon Weight: {self.weight} hectograms\n" \
               f"Pokemon Type: {self.types}\n" \
               f"Pokemon Abilities: {self.abilities}\n"

    @classmethod
    def get_move_url(cls, pokemon_name: str):
        pokemon_object = \
            asyncio.run(
                RequestApi.process_single_pokemon_request(pokemon_name))
        pokemon_dump = json.dumps(pokemon_object)
        pokemon = json.loads(pokemon_dump)

        ability_url = [item["ability"]["url"] for item in pokemon["abilities"]]
        print(ability_url)

        return ability_url

    @classmethod
    def create_pokemon_object(cls, pokemon_name_: str):
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

        final_ability_object = Pokemon(pokemon_name,
                                       pokemon_id,
                                       pokemon_height,
                                       pokemon_weight,
                                       pokemon_stats,
                                       pokemon_type,
                                       pokemon_abilities,
                                       moves)

        return final_ability_object, ability_url


class Ability:
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


class Moves:

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
    def create_multiple_pokemon_objects(cls, pokemon_name: list):
        request = pokedex.setup_request_commandline()
        async_move = \
            asyncio.run(
                RequestApi.process_multiple_ability_requests(pokemon_name))
        string_convert = json.dumps(async_move)
        pokemon_convert_json = json.loads(string_convert)

        print("\n")
        for pokekmon in pokemon_convert_json:
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

    @classmethod
    def create_multiple_ability_objects(cls, ability_name_: list):
        request = pokedex.setup_request_commandline()
        async_move = \
            asyncio.run(RequestApi.process_multiple_ability_requests(ability_name_))
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

    @classmethod
    def create_multiple_move_objects(cls, move_name_: list):
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

    @classmethod
    async def get_data(cls, id_: str, url: str,
                       session: aiohttp.ClientSession) -> dict:
        """
        An async coroutine that executes GET http request. The response is
        converted to a json. The HTTP request and the json conversion are
        asynchronous processes that need to be awaited.
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
        This function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}"

        async with aiohttp.ClientSession() as session:
            response = await RequestApi.get_data(id_, url, session)

            # print(response)
            return response

    @classmethod
    async def process_single_ability_request(cls, id_) -> dict:
        """
        This function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/ability/{}"

        async with aiohttp.ClientSession() as session:
            response = await RequestApi.get_data(id_, url, session)

            # print(response)
            return response

    @classmethod
    async def process_single_move_request(cls, id_) -> dict:
        """
        This function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param id_: an int
        :return: dict, json response
        """
        url = "https://pokeapi.co/api/v2/move/{}"

        async with aiohttp.ClientSession() as session:
            response = await RequestApi.get_data(id_, url, session)

            # print(response)
            return response

    @classmethod
    async def process_multiple_move_requests(cls, requests: list) -> list:
        """
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
        :param requests: a list of int's
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
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
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
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
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
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
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
    move_list = ["tackle", "flamethrower", "earthquake"]
    Moves.create_multiple_move_objects(move_list)
    # # url_list = ['https://pokeapi.co/api/v2/ability/27/', 'https://pokeapi.co/api/v2/ability/34/']
    # ability_Vile = Pokemon.create_pokemon_object("vileplume")
    # url_list = ability_Vile[1]
    # async_ability_expanded = \
    #     asyncio.run(
    #         RequestApi.expanded_process_multiple_pokemon_requests(url_list))
    # ability_expanded_dump = json.dumps(async_ability_expanded)
    # # print(string_convert)
    # ability_expanded_query = json.loads(ability_expanded_dump)
    # print("\nHERE'S THE EXPANDED ABILITY FROM ABOVE, SEE BELOW:")
    # for ability in ability_expanded_query:
    #     ability_name = ability["name"]
    #     ability_id = ability["id"]
    #     ability_gen = ability["generation"]["name"]
    #     ability_long_effect = ability["effect_entries"][0]["effect"]
    #     ability_short_effect = ability["effect_entries"][0]["short_effect"]
    #     ability_pokemon = "\n-".join([item["pokemon"]["name"] for item in
    #                                   ability["pokemon"]])
    #     # print(ability_name, ability_id, ability_gen,ability_long_effect, ability_short_effect, ability_pokemon)
    #     final_ability_object = Ability(ability_name, ability_id, ability_gen,
    #                                    ability_long_effect,
    #                                    ability_short_effect,
    #                                    ability_pokemon)
    #     print(final_ability_object)

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
