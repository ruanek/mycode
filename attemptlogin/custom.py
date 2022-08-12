#!/usr/bin/python3

loginfail = 0 
successful = 0 

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 
            print("Failed login from " + line.split(" ")[-1])
        elif "-] Authorization failed" in line:  
            successful += 1
            
print("The number of failed log in attempts is", loginfail)

print("The number of successful log ins is", successful)
