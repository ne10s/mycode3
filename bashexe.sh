#!/bin/bash
#Prompt user to enter user name
echo "Enter user name:"
#Read command reads one line from standard input
read NEWUSER
#Prompt user to enter group name
echo "Enter group name:"
#Read user input for group name
read GROUP
#add user as user input value
sudo useradd -p $PASS $NEWUSER
#create group as user input value for group
sudo groupadd $GROUP
#add new-user into newly created group
sudo usermod -aG $GROUP $name
