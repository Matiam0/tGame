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
def title():
    LibJson = "lib\lib.json"
    GameVersion = fromJsonKey(LibJson,'version')
    GameState = fromJsonKey(LibJson,'gamestate')
    if GameState == "dev":
        Dic = {"line1":f"tGame [Dev] {GameVersion}","line2":"_______________________","line3":""}
    elif GameState == "troll":
        Dic = {"line1":f"tGame [Troll] {GameVersion}","line2":"_______________________","line3":""}
    else:
        Dic = {"line1":f"tGame {GameVersion}","line2":"_______________________","line3":""}
    for v in Dic.values():
        print(v)

##Json management functions

### print from json by keyword argument.
def fromJsonKey(File, Key):
    import json
    with open(File,"r") as JsonFile:
        JsonFile = json.load(JsonFile)
        Out = JsonFile.get(Key)
        return Out

### Create Dictionary from Json.
def fromJson(File):
    import json
    OpenFile = open(File, "r")
    JsonFile = json.load(OpenFile)
    return JsonFile



## Dictionary functions

### Print |"{key} : {value}"| from dictionary.
def printDic(Dic):
    for k, v in Dic.items():
        print(f"{k} : {v}")

### Print values from dictionary.
def printVal(Dic):
    for v in Dic.values():
        print(v)

### Print keys from dictionary.
def printKey(Dic):
    for k in Dic.keys():
        print(k)

# This is an example of t.fromJson(), t.printDic(), t.printKey(), & t.printVal().
#    TestJson = t.fromJson(IntroJson)
#    t.printDic(TestJson)
#    t.printKey(TestJson.get('1')) # for if you have nested dictionary items ex {"yep":{"1":"What I want to print!"}}
#    t.printVal(TestJson)
#    t.sleep(4)