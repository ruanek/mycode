#!/usr/bin/env python3

configfile = open("vlanconfig.cfg", "r")

print(configfile.read())
configfile.seek(0, 0)
configlist = configfile.readlines()
print(configlist)

for x in configlist:
    print(x, end="")

configfile.close()
