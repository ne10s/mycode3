#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
#succesful attempt
loginsuccess = 0


# open the file for reading
with open("/home/student/mycode3/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif "-] Authorization failed" in line:
            loginsuccess += 1 
print("The number of failed log in attempts is", loginfail)
print("Successful attempt", loginsuccess)
print("Fin")
