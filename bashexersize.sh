#!/bin/bash

#check if user is root
if [ $(id -u) -eq 0 ]; then
#ask for username
	read -p "Enter username : " username
#check if user already exists
	egrep "^$username" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		echo "$username exists!"
		exit 1
	else
#creates the new user with password and creates their home directory if they dont have one
		useradd -m  "$username"
#creates and adds user to the group
		usermod -a -G testgroup $username
		[ $? -eq 0 ] && echo "User has been added to system!" || echo "Failed to add a user!"
		echo 
        
	fi
else
#response if user is not root
	echo "Only root may add a user to the system."
	exit 2
fi

