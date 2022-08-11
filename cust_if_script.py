#!/usr/bin/env python3

message = ' movie/book: '

num = int(input("Enter numb between 1 to 3 for 1.Harry Potter, 2. Hobbit & 3. Chronicles of Narnia : "))
        
if num > 3:
    message = message + 'Invalid entry, choose between 1,2 or 3'
    print(message)
elif num < 0:
    message =  message + 'Invalid entry, choose between 1,2 or 3'
    print(message)
elif num == 1:
    message = message + 'Magic wand chooses the kid.'
    print(message)
elif num == 2:
    message = message + 'Ring chooses the kid.'
    print(message)
elif num == 3:
    message = message + 'Closet chooses the kid.'
    print(message)
else:
    message = 'Invalid entry, choose between 1,2 or 3'
    
