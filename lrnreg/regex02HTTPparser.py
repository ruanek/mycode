#!/usr/bin/env python3

import re
import requests

def main():
    print("Where should we search?")
    url = input("> ")  

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    
    while(True):
        searchFor = input("> ")

        resp = requests.get(url)  
        searchMe = resp.text      

        if re.search(searchFor, searchMe):
            print("Found a match!")
        else:
            print("No match!")

        cont = input(f"\nWould you like to search {url} again? Enter to continue, or enter 'q' to quit: ")
        if (cont.lower() == 'q'):
            break
if __name__ == "__main__":
    main()

