#!/usr/bin/env python3

import shutil
import os

# allow the user to run the program from any location on the system
os.chdir('/home/student/mycode/')

#will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location
shutil.move('raynor.obj', 'ceph_storage/')

# prompt to rename file
xname = input('What is the new name for kerrigan.obj? ')

# rename file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


