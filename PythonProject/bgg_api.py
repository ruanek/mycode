#!/usr/bin/env python3

import requests
import xmltodict

response = requests.get("https://boardgamegeek.com/xmlapi/search?search=horrified")

print(response.status_code)
dict_data = xmltodict.parse(response.content)
print(dict_data)

for x in dict_data:
    print(x[0[0]])




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