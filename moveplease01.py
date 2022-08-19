#!/usr/bin/env python3

"""Author:Neten"""

#importing files
import shutil
import os


#force to start in home user dir
os.chdir('/home/student/mycode3/')

#moving file
shutil.move('raynor.obj', 'ceph_storage/')

#prompt usr for new name
xname = input('What is the n name for kerrigan.obj? ')

#rename file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)




