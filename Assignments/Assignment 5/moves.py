import aiohttp
import asyncio
import ssl
import json

async def get_moves_data(id_: str, url: str, session: aiohttp.ClientSession) -> dict:
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
    print("Response object from aiohttep:\n", response)
    print("Response object type:\n", type(response))
    json_dict = await response.json()
    return json_dict

async def process_single_request(id_) -> dict:
    """
    This function depicts the use of await to showcase how one async
    coroutine can await another async coroutine
    :param id_: an int
    :return: dict, json response
    """
    # url = "https://swapi.co/api/people/{}/"
    url = "https://pokeapi.co/api/v2/move/{}"

    async with aiohttp.ClientSession() as session:
        response = await get_moves_data(id_, url, session)
        for key in response:
            print(key)
        jprint(response)
        return response

async def process_requests(requests: list) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async coroutines concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """
    url = "https://pokeapi.co/api/v2/move/{}"
    async with aiohttp.ClientSession() as session:
        async_coroutines = [get_moves_data(id_, url, session)
                            for id_ in requests]
        responses = await asyncio.gather(*async_coroutines)
        for response in responses:
            print(response)
        return responses

def jprint(obj):
    """
    Create and print a formatted string of the Python JSON object
    """
    #
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def main():
    move_list = ["pound", "flamethrower", "earthquake"]
    async_move = asyncio.run(process_requests(move_list))

    print("-"*900)
    move1 = asyncio.run(process_single_request("pound"))


if __name__ == '__main__':
    main()