#!/usr/bin/env python3

import requests
import xmltodict

usrinput = input("What game are you looking for?: ")
response = requests.get(f"https://boardgamegeek.com/xmlapi/search?search={usrinput}")

print(response.status_code)
dict_data = xmltodict.parse(response.content)
game_dict = (dict_data["boardgames"]["boardgame"])

for x in game_dict:
    print(x.get("@objectid"))
    if type(x.get("name")) == str:
        print(x.get("name"))
    else:
        print((x.get("name")).get("#text"))

usrinput2 = input("Would you like to know more about any?: ")
response = requests.get(f"https://boardgamegeek.com/xmlapi/boardgame/{usrinput2}")

print(response.status_code)
dict_data2 = xmltodict.parse(response.content)
more_info = (dict_data2["boardgames"]["boardgame"])
print(more_info.keys())
# for x in more_info:
#     if type(x.get("name")) == str:
#         print(x.get("name"))
#     else:
#         print((x.get("name")).get("#text"))
#     print(x.get("description"))

# {'boardgames': 
# {'@termsofuse': 'https://boardgamegeek.com/xmlapi/termsofuse', 'boardgame': 
#     [{'@objectid': '282524', 
#       'name': {
#             '@primary': 'true', 
#             '#text': 'Horrified'
#             }, 
#         'yearpublished': '2019'
#         }, 

#     {'@objectid': '343562', 
#     'name': {
#         '@primary': 'true', 
#         '#text': 'Horrified: American Monsters'
#         }, 
#     'yearpublished': '2021'
#     }]}}