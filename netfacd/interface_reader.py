#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        print('IP: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
    except:          
            print('Could not collect adapter information')

ip_interface = input("What adapter IP are you looking for?: ")
for i in netifaces.interfaces():
    if i == ip_interface:
        print('IP: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
    else:          
        print('Could not collect adapter information')

mac_interface = input("What adapter MAC are you looking for?: ")
for i in netifaces.interfaces():
    if i == mac_interface:
        print('MAC: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
    else:          
        print('Could not collect adapter information')