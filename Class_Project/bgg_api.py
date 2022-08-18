#!/usr/bin/env python3
""" enter something here || Kyle Ruane """

import requests
import xmltodict
from pprint import pprint

game_list = {}
bgg_url =  "https://boardgamegeek.com/xmlapi"

# function to call API with string search
def searchgame():
    """ enter something here """

    usrinput = input("What game are you looking for?: ")
    response = requests.get(f"{bgg_url}/search?search={usrinput}")
    

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
        pprint(f"{counter} - Game: {game_list[game]}")

# function to search specific game details using id's
def search_specific_game():
    """ enter something here """
    
    usrinput = input("Looking for more info? Enter the # of the game separated by a comma (i.e 1 or 1,2,3), or type 'exit' to quit: ")
    keylist = list(game_list.keys())
    searchlist = None

    if usrinput == "exit":
        print("Exiting...")
    else:
        if usrinput.__contains__(","):
            input_list = usrinput.split(",")
            for i, item in enumerate(input_list):
                input_list[i] = keylist[(int(input_list[i]) - 1)]
            searchlist = ",".join(input_list)
        else:
            input_list = usrinput
            searchlist = str(keylist[(int(input_list) - 1)])
            
        response = requests.get(f"{bgg_url}/boardgame/{searchlist}")
        
        boardgame = xmltodict.parse(response.content)["boardgames"]["boardgame"]
        
        if isinstance(boardgame, dict):
            boardgame = [boardgame]

        for game in boardgame:
            game_id2 = (game.get("@objectid"))
            yr_pub = (game.get("yearpublished"))
            description = (game.get("description")).replace("<br/>", "").replace("&mdash", "")
            print(f"\nName: {game_list[game_id2]}({yr_pub}):\nDescription:\n{description}\n\n")

def main():
    """called at runtime"""

    print("Welcome to the gamefinder")

    
    while True:
        try:
            searchgame()
            break
        except:
            print("Your Search did not return a response, Please try again")

    while True:
        try:
            search_specific_game()
            break
        except:
            print("Please select values within the list")

main()
