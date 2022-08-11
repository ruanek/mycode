#!/usr/bin/env python3

# standard library imports
import shutil   
import os       

def main():
    # move into this working directory
    os.chdir('/home/student/mycode/') 
    # try moving the file raynor.obj into ceph_storage/ dir 
    shutil.move('raynor.obj', 'ceph_storage/')  

    # collect string input from the user
    xname = input('What is the new name for kerrigan.obj? ') 
    # moving kerrigan.obj into ceph_storage/ with new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  


main() # this calls our main function
