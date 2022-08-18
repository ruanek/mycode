#!/usr/bin/env python3
""" enter something here || Kyle Ruane """

# importing requests for api requests and xmltodict for xml to dict conversion
import requests
import xmltodict

# defining global variables to be used in multiple functions
game_list = {}
BGG_URL =  "https://boardgamegeek.com/xmlapi"

# function to call API with string search
def searchgame():
    """ Uses the BGG XML API to Search for games by name and by AKAs """

    # requesting user input
    usrinput = input("What game are you looking for? Enter your search, or type 'q' to quit: ")

    # conditional to allow user to escape this function
    if usrinput.lower() == "q":
        print("Skipping...")
    else:
        # combining the url and usrinput to make the api call
        response = requests.get(f"{BGG_URL}/search?search={usrinput}")
        # using xmltodict to convert the xml response from the api to a dictionary
        game_dict = xmltodict.parse(response.content)["boardgames"]["boardgame"]
        counter = 0
        # iterating through game_dict to set variables to be used for printing and
        # adding to game_list
        for game in game_dict:
            game_id = (game.get("@objectid"))
            # conditional to handle game entries that are nested due to xmltodict conversion
            # from api data
            if isinstance(game.get("name"), str):
                name = (game.get("name"))
            else:
                name = ((game.get("name")).get("#text"))
            # adding dictionary item to game_list
            game_list[game_id] = name
        # iterating through gamelist to print to the user
        for game in game_list:
            counter += 1
            print(f"{counter} - Game: {game_list[game]}")

# function to search specific game details using id's
def search_specific_game():
    """ Uses the BGG XML API to Retrieve information about a particular game or games """

    # requesting user input
    usrinput = input("\nLooking for more info?\nEnter the # of the game separated by a comma" \
        " (i.e 1 or 1,2,3), or type 'q' to quit: ")
    # defining variables to be used throughout the function
    keylist = list(game_list.keys())
    searchlist = None

    # conditional to allow user to escape this function
    if usrinput.lower() == "q":
        print("Skipping...")
    else:
        # conditional to handle single or multiple user input seperated by a comma
        if "," in usrinput:
            # converting a string to a list using .split()
            input_list = usrinput.split(",")
            # iterating through input_list
            for i, item in enumerate(input_list):
                # re-assigning "user friendly" value in input list to game id used by the api
                input_list[i] = keylist[(int(item) - 1)]
            # converting list to string seperated by commas
            searchlist = ",".join(input_list)
        else:
            input_list = usrinput
            # converting list to string seperated by commas and,
            # re-assigning "user friendly" value in input list to game id used by the api
            searchlist = str(keylist[(int(input_list) - 1)])

        # combining the url and searchlist to make the api call
        response = requests.get(f"{BGG_URL}/boardgame/{searchlist}?stats=1")

        # using xmltodict to convert the xml response from the api to a dictionary
        boardgame = xmltodict.parse(response.content)["boardgames"]["boardgame"]
        # conditional to typecast boardgame as a list
        # because single vs multiple entries come in as different types
        if isinstance(boardgame, dict):
            boardgame = [boardgame]

        # iterating through boardgames to set variables to be used for printing
        for game in boardgame:
            game_id2 = (game.get("@objectid"))
            yr_pub = (game.get("yearpublished"))
            description = (game.get("description")).replace("<br/>", "").replace("&mdash", "")
            comprating = (game["statistics"]["ratings"].get("averageweight"))[:3]
            usrrating = (game["statistics"]["ratings"].get("average"))[:3]
            print(f"\nName: {game_list[game_id2]}({yr_pub}):\nComplexity Rating: {comprating}/5\
                \nUser Rating: {usrrating}/10 \nDescription:\n{description}\n\n")

def main():
    """called at runtime"""

    print("Welcome to the gamefinder (Powered by BoardGameGeek API)")

    # loop to allow user to
    while True:
        while True:
            try:
                searchgame()
                break
            except: # pylint: disable=bare-except
                print("Your Search did not return a response, Please try again!")

        if len(game_list) > 0:
            while True:
                try:
                    search_specific_game()
                    break
                except: # pylint: disable=bare-except
                    print("Please select values within the list!")

        check = input("Would you like to search again? Type 'y' to continue" \
            " or any other key to exit: ")
        if check.lower() == "y":
            continue

        print("Exiting...Hava a nice day!")
        break
if __name__ == "__main__":
    main()
