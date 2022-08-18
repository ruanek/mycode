#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

herodata= [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    return jsonify(herodata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

