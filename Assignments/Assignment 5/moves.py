import aiohttp
import asyncio
import ssl
import json


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
               f"Long Effect: \n{self.effect}\n\n" \
               f"Short Effect: {self.short_effect}\n\n" \
               f"Pokemon that has this ability " \
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


def main():
    move_list = ["pound", "flamethrower", "earthquake"]
    async_move = \
        asyncio.run(RequestApi.process_multiple_move_requests(move_list))
    string_convert = json.dumps(async_move)
    print(string_convert)
    moves_convert_json = json.loads(string_convert)
    print("\n")
    for move in moves_convert_json:
        move_name = move["name"]
        move_id = move["id"]
        move_gen = move["generation"]
        move_accuracy = move["accuracy"]
        move_pp = move["pp"]
        move_power = move["power"]
        move_type = move["type"]
        move_damage_class = move["damage_class"]
        move_short_effect = move["effect_entries"][0]["short_effect"]
        print(move_name, move_id, move_gen, move_accuracy,
              move_pp, move_power, move_type, move_damage_class,
              move_short_effect)

    flamethrower = Moves.create_move_object("flamethrower")
    print(flamethrower)

    intimidate = Ability.create_ability_object("drizzle")
    print(intimidate)


if __name__ == '__main__':
    main()
