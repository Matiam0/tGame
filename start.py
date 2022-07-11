import sys
import syslib
import storylib

def main():
    # get name stored for later use.
    name = char_naming()
    
    # create character sheet
    sheet = char_creation(name)
    
    # give the ending screen time to be fully read. 5 seconds default?
    syslib.sleep(5)
    syslib.clear()


# get name for character
def char_naming():
    name = print("What is your name? ")
    return name


#create a character
def char_creation(name):
    points = storylib.dice(12)
    
    #assign rolled points to character sheet
    while points != 0:
        print()


main()