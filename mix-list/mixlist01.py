#!/usr/bin/env python3

# list with 3 tiems
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display only ip addresses
print("IP only:" + iplist[3], iplist[4] )

#display 1st item in list
print("The first item in the list (IP); " + my_list[0] )

#display 2nd item
print("The second item in the list (port): " + str(my_list[1]) )

#display 3rd item
print("The last item in the list (state): " + my_list[2] )

