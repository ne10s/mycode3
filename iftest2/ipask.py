#!/usr/bin/env python3

#prompt user for IP add
ipchk = input("Apply an IP address: ")

#if IP is gateway
if ipchk == "192.168.70.1":
    print("looks like IP add of Gateway was set: " + ipchk + "Not recommended.")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk) 
    #if data not provided
else: 
    print("You didn't provide input.")
