#!/usr/bin/env python3

import os      
import zipfile 

def zipdir(dirpath, zipfileobj):
    for root, dirs, files in os.walk(dirpath):
        for file in files:  
            print(os.path.join(root,file))   
            zipfileobj.write(os.path.join(root, file)) 
    return None 


def main():
    dirpath = input("What directory are we archiving today? ")

    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? ")
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            zipdir(dirpath, zipfileobj) 
    else:
        print("Run the script again when you have a valid directory to zip.")

main()
