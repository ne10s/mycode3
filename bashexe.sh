#!/bin/bash

echo "Enter user name:"
read NEWUSER
echo "Enter group name:"
read GROUP

sudo useradd -p $PASS $NEWUSER

sudo groupadd $GROUP

sudo usermod -aG $GROUP $name
