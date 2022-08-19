#!/usr/bin/env python3
""" Python program allowing the user to search for games
request more information and export selected
game data to a csv file || Author: Kyle Ruane """

# importing requests for api calls
import requests
# importing xmltodict to convert xml to dictionary
import xmltodict
# importing pandas to append to dataframe and write to csv
import pandas as pd

# defining global variables to be used in multiple functions
game_list = {}
BGG_URL =  "https://boardgamegeek.com/xmlapi"

# function to call API with string search
def searchgame():
    """ Uses the BGG XML API to Search for games by name and by AKAs """
    # requesting user input
    usrinput = input("\nWhat game are you looking for? Enter your search, or type 'q' to quit: ")

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

# helper function for search_specific game and possibly send to csv
def input_handler(usrinput):
    """ Used to output searchlist in a string with values the api can understand """
    # defining variables to be used throughout the function
    keylist = list(game_list.keys())
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

    return searchlist

# function to search specific game details using id's
def search_specific_game():
    """ Uses the BGG XML API to Retrieve information about a particular game or games """
    # requesting user input
    usrinput = input("\nLooking for more info?\nEnter the # of the game separated by a comma" \
        " (i.e 1 or 1,2,3), or type 'q' to quit: ")
    # conditional to allow user to escape this function or continue
    if usrinput.lower() == "q":
        print("Skipping...")
    else:
        search_list = input_handler(usrinput)
        # combining the url and searchlist to make the api call
        response = requests.get(f"{BGG_URL}/boardgame/{search_list}?stats=1")

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
            comp_rating = (game["statistics"]["ratings"].get("averageweight"))[:3]
            user_rating = (game["statistics"]["ratings"].get("average"))[:3]
            print(f"\nName: {game_list[game_id2]}({yr_pub}):\nComplexity Rating: {comp_rating}/5\
                \nUser Rating: {user_rating}/10 \nDescription:\n{description}\n\n")

# function to search specific game details using id's
def send_to_csv():
    """ Uses the BGG XML API to Retrieve information about a particular game or games """
    # setting variables for each list that will be added to the data_to_csv dict
    ids = []
    name = []
    published = []
    minplayers = []
    maxplayers = []
    age = []
    desc = []
    complexity = []
    usrrtg = []

    data_to_csv = {
        "game_id" : ids,
        "name" : name,
        "yr_pub" : published,
        "minplayers" : minplayers,
        "maxplayers" : maxplayers,
        "age" : age,
        "description" : desc,
        "comp_rating" : complexity,
        "user_rating" : usrrtg
            }

    # requesting user input
    usrinput = input("\nWould you like to export game information to a csv file?\nEnter the #" \
        " of the game separated by a comma (i.e 1 or 1,2,3), or type 'q' to quit: ")
    # conditional to allow user to escape this function or continue
    if usrinput.lower() == "q":
        print("Skipping...")
    else:
        search_list = input_handler(usrinput)
        # combining the url and searchlist to make the api call
        response = requests.get(f"{BGG_URL}/boardgame/{search_list}?stats=1")

        # using xmltodict to convert the xml response from the api to a dictionary
        boardgame = xmltodict.parse(response.content)["boardgames"]["boardgame"]
        # conditional to typecast boardgame as a list
        # because single vs multiple entries come in as different types
        if isinstance(boardgame, dict):
            boardgame = [boardgame]
        # iterating through boardgames to append to each list within the data_to_csv dict
        for game in boardgame:
            ids.append(game.get("@objectid")),
            name.append(game_list[(game.get("@objectid"))]),
            published.append(game.get("yearpublished")),
            minplayers.append(game.get("minplayers")),
            maxplayers.append(game.get("maxplayers")),
            age.append(game.get("age")),
            desc.append((game.get("description")).replace("<br/>", "").replace("&mdash", "")),
            complexity.append((game["statistics"]["ratings"].get("averageweight"))[:3]),
            usrrtg.append((game["statistics"]["ratings"].get("average"))[:3])

        # allowing user to set the filename of the csv
        file_name = input("What do you want to call the file?: ")
        #using panda to append DataFrames and write to user named csv file
        data_frame = pd.DataFrame(data_to_csv)
        data_frame.to_csv(f"{file_name}.csv")

def main():
    """called at runtime"""

    print("Welcome to the gamefinder (Powered by the BoardGameGeek API)")

    # loop to allow user to navigate through the prompts
    while True:
        # loop through the search_game function
        while True:
            try:
                searchgame()
                break
            except: # pylint: disable=bare-except
                print("Your Search did not return a response, Please try again!")

        # conditional to check if game_list was populated since the user can
        # quit out of the first function they would have no options to choose from here
        if len(game_list) > 0:
            # loop through the search_specific_game function
            while True:
                try:
                    search_specific_game()
                    break
                except: # pylint: disable=bare-except
                    print("Please select values within the list!")

        # conditional to check if game_list was populated since the user can
        # quit out of the first function they would have no options to choose from here
        if len(game_list) > 0:
        # loop through the search_specific_game function
            while True:
                try:
                    send_to_csv()
                    break
                except: # pylint: disable=bare-except
                    print("Please select values within the list!")

        # prompting user if they would like to start a new search
        check = input("\nWould you like to search again? Type 'y' to continue" \
            " or any other key to exit: ")
        if check.lower() == "y":
            if len(game_list) > 0:
                # using to allow user to clear the game_list or add to it
                clear_list = input("\nWould you like to clear the game list? Type 'y' to" \
                    " clear or 'n' to keep and add to it: ")
                # conditional to clear or keep game_list
                if clear_list.lower() == "y":
                    game_list.clear()
            continue

        print("\nExiting...Hava a nice day!")
        break
if __name__ == "__main__":
    main()
