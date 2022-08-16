#!/usr/bin/env python3
""" enter something here || Kyle Ruane """

import requests
import xmltodict

game_list = {}

# function to call API with string seach
def searchgame():
    """ enter something here """

    usrinput = input("What game are you looking for?: ")
    response = requests.get(f"https://boardgamegeek.com/xmlapi/search?search={usrinput}")
    print(response.status_code)

    dict_data = xmltodict.parse(response.content)["boardgames"]["boardgame"]
    counter = 0
    for game in dict_data:
        game_id = (game.get("@objectid"))
        if isinstance(game.get("name"), str):
            name = (game.get("name"))
        else:
            name = ((game.get("name")).get("#text"))
        game_list[game_id] = name
    for game in game_list:
        counter += 1
        print(f"{counter} - Game: {game_list[game]}")

# function to search specific game details using id's
def specific_game():
    """ enter something here """

    usrinput2 = input("Would you like to know more about any?: ")
    input_list = usrinput2.split(",")

    keylist = list(game_list.keys())
    for i, item in enumerate(input_list):
        input_list[i] = keylist[(int(input_list[i]) - 1)]
    print(input_list)

    searchlist = ",".join(input_list)

    response = requests.get(f"https://boardgamegeek.com/xmlapi/boardgame/{searchlist}")
    print(response.status_code)

    dict_data2 = xmltodict.parse(response.content)["boardgames"]["boardgame"]

    for game in dict_data2:
        game_id2 = (game.get("@objectid"))
        yr_pub = (game.get("yearpublished"))
        description = (game.get("description")).replace("<br/>", "")
        print(f"Name: {game_list[game_id2]}({yr_pub}):\nDescription: {description}\n\n")

def main():
    """called at runtime"""

    print("Welcome to the gamefinder")

    searchgame()
    specific_game()

main()
