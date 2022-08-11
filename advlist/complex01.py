#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    print(list1[1])
    #create new list
    list2 = ["juniper"]

    #extend 1 n 2
    list1.extend(list2)

    #print
    print(list1)

    #create list 3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #append 1 n 3
    list1.append(list3)

    print(list1)
    
    #create animal list
    animal = ["Fox","Fly","Cat","Rat","Hen"]
    
    

    print(list1[4][0] )
    #print 1st ip
    print(list1[4][0])

    #append animal to list 2
    list2.append(animal)
    print(list2[1],sep=" ")
main()

