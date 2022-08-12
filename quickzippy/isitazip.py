#!/usr/bin/python3

import zipfile

def main():
    iszip = input("What is the file you would like to examine (full or relative path)? ")

    if zipfile.is_zipfile(iszip):   
        print("Yep! That is a 'zip' file.")
    else:
        print("Nay. That is not a 'zip' file.")

if __name__ == "__main__":
    main()
