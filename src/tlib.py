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
def pfjson(file, key):
    import json
    with open(file) as json_file:
        data = json.load(json_file)
        out = data.keys()
        return out

# title
def title(version):
    print(f"TGame [Dev] {version}")
    print("_______________________")
    print(" ")
    print(" ")