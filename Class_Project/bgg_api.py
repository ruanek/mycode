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

    for game in dict_data:
        game_id = (game.get("@objectgame_id"))
        if type(game.get("name")) == str:
            name = (game.get("name"))
        else:
            name = ((game.get("name")).get("#text"))
        game_list[game_id] = name
    for game in game_list:
        print(f"{game}: Game: {game_list[game]}")

# function to search specific game details using id's
def specific_game():
    """ enter something here """

    usrinput2 = input("Would you like to know more about any?: ")
    response = requests.get(f"https://boardgamegeek.com/xmlapi/boardgame/{usrinput2}")
    print(response.status_code)

    dict_data2 = xmltodict.parse(response.content)["boardgames"]["boardgame"]

    for game in dict_data2:
        game_id2 = (game.get("@objectid"))
        yr_pub = (game.get("yearpublished"))
        description = (game.get("description")).replace("<br/>", "")
        print(f"{game_list[game_id2]}({yr_pub}):\n{description}\n\n")

def main():
    """called at runtime"""

    print("Welcome to the gamefinder")

    searchgame()
    specific_game()

main()
