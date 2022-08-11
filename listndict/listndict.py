#!/usr/bin/env python3


    #list 1,2,3 creation
list1 = ["dumplings", "chicken_rice", "curry"]
list2 = ["pizza", "burger"]
list3 = ["BBQ"]

    #append lists
list1.append(list2)
list1.append(list3)

    #print list1
print(list1)
print("My fav food", list1[0])


heroes = {
        "SpiderMan": {"color": "red_blue", "comic": "marvel", "power": "web"},
        "BatMan": {"color": "black", "comic": "DC", "power": "none"},
        "IronMan": {"color": "red_gold", "comic": "marvel", "power": "none"}}

print(heroes.keys())
print(heroes.values())
