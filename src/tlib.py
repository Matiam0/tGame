# Use for System type commands that can be used in the lib later.
# define easy to use clear screen that works on multiple os
def clear():
    import os
    if(os.name =='posix'):
        os.system('clear')
    else:
        os.system('cls')

# define sleep as an easy to call function
def sleep(n):
    from time import sleep
    sleep(n)

# RPG def below here
## print from json
def fromJson(File, Key):
    import json
    with open(File,"r") as JsonFile:
        JsonFile = json.load(JsonFile)
        Out = JsonFile.get(Key)
        return Out

# title
def title(GameTitle, GameVersion):
    print(f"{GameTitle} {GameVersion}")
    print("_______________________")
    print(" ")
    print(" ")