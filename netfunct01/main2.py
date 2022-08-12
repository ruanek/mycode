#!/usr/bin/env python3

import crayons
import json

def commandpush(devicecmd): 
    for ip in devicecmd.keys(): 
        print(f'{crayons.green("Handshaking")}. .. ... connecting with {ip}') 

        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
    return None

def devicereboot(devicecmd):
    for ip in devicecmd.keys(): 
        print(f'{crayons.blue("Connecting ")} to {ip}')
        print(f'{crayons.red("REBOOTING ")}{ip} now')

def main():
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)

    print(f"Welcome to the {crayons.cyan('Network')} device command pusher") 

    print("\nData set found\n") 

    commandpush(devicecmd) 
    devicereboot(devicecmd)

main()
