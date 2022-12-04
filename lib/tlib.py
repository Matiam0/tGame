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