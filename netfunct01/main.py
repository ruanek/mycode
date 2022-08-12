#!/usr/bin/env python3

import crayons

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
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.cyan('Network')} device command pusher") 

    print("\nData set found\n") 

    commandpush(devicecmd) 
    devicereboot(devicecmd)

main()
