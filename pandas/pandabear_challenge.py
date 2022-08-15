#!/usr/bin/python3

import pandas

def main():
    df = pandas.read_json("5movies.json")

    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()
