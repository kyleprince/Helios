# Program: Helios SIO
# Description: Scalable Identifier Organization:
# Scaling program for sorting files based on extension or name inclusion specified by the user

# system imports
import os
import shutil
import random
import string
import datetime
import array


def identify():
    print("Scalable Identifier Organization")
    print("==================================")
    print("Choose identifier (ext/name): ")
    option = input()
    option2 = " "
    partial = " "

    if option == "ext":
        print("Extension: ")
        option2 = input()
        original = "*." + option2
        target = "./" + option2
        shutil.move(original,target)

    elif option == "name":
        print("Partial name: ")
        option2 = input()



# Main
identify()
