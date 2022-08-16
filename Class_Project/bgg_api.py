#!/usr/bin/env python3

import requests
import xmltodict

game_list = {}

def searchgame():
    usrinput = input("What game are you looking for?: ")
    response = requests.get(f"https://boardgamegeek.com/xmlapi/search?search={usrinput}")
    print(response.status_code)

    dict_data = xmltodict.parse(response.content)["boardgames"]["boardgame"]
    

    for game in dict_data:
        id = (game.get("@objectid"))
        if type(game.get("name")) == str:
            name = (game.get("name"))
        else:
            name = ((game.get("name")).get("#text"))
        game_list[id] = name
        
    for x in game_list:
        print(f"{x}: Game: {game_list[x]}")

def specific_game():
    usrinput2 = input("Would you like to know more about any?: ")
    response = requests.get(f"https://boardgamegeek.com/xmlapi/boardgame/{usrinput2}")
    print(response.status_code)

    dict_data2 = xmltodict.parse(response.content)["boardgames"]["boardgame"]

    for game in dict_data2:
        id2 = (game.get("@objectid"))
        yr_pub = (game.get("yearpublished"))
        description = (game.get("description")).replace("<br/>", "")
        print(f"{game_list[id2]}({yr_pub}):\n{description}\n\n")

def main():
    print("Welcome to the gamefinder")

    searchgame()
    specific_game()

main()