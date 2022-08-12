#!/usr/bin/env python3

filename = input("What csv file would you like to use: ")
with open(f"{filename}", "r") as configfile:
    configlist = configfile.readlines()
    linecount = len(configlist)

print(configlist)
print(linecount)
