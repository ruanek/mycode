#!/usr/bin/env python3

import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_hero= {
           "name": "Wolverine",
           "realName": "James Howlett",
           "since": 1974,
           "powers": ["adamantium skeleton","claws","regeneration"]
          }

new_hero= json.dumps(new_hero)

resp= requests.post(URL, json=new_hero)

pprint(resp.json())

