
#!Read Me

#This library requires the following files
##A "lib\lib.json" with the version and gamestate key:variable pairs.
##If you want the above to not be required you can comment out the def title, ... lines.





# Use for System type commands that can be used in the lib later.
# define easy to use clear screen that works on multiple os
def clear():
    import os
    if(os.name =='posix'):
        os.system('clear')
    else:
        os.system('cls')

# define sleep as an easy to call function
def wait(n):
    from time import sleep
    sleep(n)

# RPG def below here

##Game functions
def title(Setting=0):
    LibJson = "lib\lib.json"
    Dic = fromJson(LibJson).get('Title')
    for v in Dic.values():
        print(v)

#Main menu function
def menu(save):
    check = True
    while check == True:
            clear()
            print("_____________")
            print("| New Game")
            if save == True:
                print("| Load")
            print("| Settings")
            print("| Quit")
            print("\__________")
            option = input('Select: ')

##Json management functions
### Create Dictionary from Json.
def fromJson(File):
    import json
    OpenFile = open(File, "r")
    JsonFile = json.load(OpenFile)
    return JsonFile