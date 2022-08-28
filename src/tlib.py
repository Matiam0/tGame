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

# print fromfile using key to get only the value to print.
def fromfilevalue(file,key):
    out = loadfile(file)
    print(out.get(key))

# print fromfile with key and value.
def fromfilekeyvalue(file, key):
    out = loadfile(file)
    for key, value in out.items():
        print(key, ':', value)

#file loading
def loadfile(file):
    import json
    f = open(file)
    out = json.load(f)
    return out

# rpg defs/ non-system type.
# dice roller.
def dice(sides):
    import random
    roll = random.randint(1, sides)
    return roll

# 2 choices
def choice2(c1, c2):
    in1 = input(f"{c1}, or {c2}? ")
    if in1 == c1:
        c0 = c1
    else:
        c0 = c2
    return c0

# 3 choices
def choice3(c1, c2, c3):
    in1 = input(f"{c1}, {c2}, or {c3}? ")
    if in1 == c1:
        c0 = c1
    elif in1 == c2:
        c0 = c2
    else:
        c0 = c3
    return c0

# 4 choices
def choice4(c1, c2, c3, c4):
    in1 = input(f"{c1}, {c2}, {c3}, or {c4}? ")
    if in1 == c1:
        c0 = c1
    elif in1 == c2:
        c0 = c2
    elif in1 == c3:
        c0 = c3
    else:
        c0 = c4
    return c0

# show character sheet
def scs(sheet):
    for key, value in sheet.items():
        print(key, ':', value)

# character sheet edit/stat edit.
def sedit(sheet):
    name = sheet.get('Name')
    stat1t = sheet.item(stat1t)
    stat1 = sheet.item(stat1)
    stat2t = sheet.item(stat2t)
    stat2 = sheet.item(stat2)
    stat3t = sheet.item(stat3t)
    stat3 = sheet.item(stat3)
    points = sheet.get('Points')
    level = sheet.item(level)
    exp = sheet.get('Exp')
    gender = sheet.get('Gender')
    while points > 0:
        clear()
        print(f"Hello you have {points} points  remaining.")
        print(f"Where would you like to spend  them?")
        pick = input(f"{stat1t}, {stat2t}, or {stat3t}? ")
        if pick == stat1t:
            spent = int(input(f"How many points into {stat1t}? "))
            points = points - spent
            stat1 = stat1 + spent
            spent = 0
        elif pick == stat2t:
            spent = int(input(f"How many points into {stat2t}? "))
            points = points - spent
            stat2 = stat2 + spent
            spent = 0
        elif pick == stat3t:
            spent = int(input(f"How many points into {stat3t}? "))
            points = points - spent
            stat3 = stat3 + spent
            spent = 0
        else:
            pass
    sheet = {'Name': name, "Gender": gender, "Level": level, 'EXP' : exp, 'Points': points, stat1t: stat1, stat2t: stat2, stat3t: stat3}
    return sheet

def ccreate():
    # flare, useless code... may add a def for automating this and make it easier to comment out during testing.
    clear()
    print("Initializing Character creation.")
    sleep(3)
    clear()
    print("Initializing Character creation..")
    sleep(3)
    clear()
    print("Initializing Character creation...")
    sleep(3)
    clear()
    # initial / basic stats and starting level.
    stat1t = "STR"
    stat1 = 3
    stat2t = "INT"
    stat2 = 3
    stat3t = "DEX"
    stat3 = 3
    level = 1
    exp = 0
    points = 0
    #  currently random gender, may make it a choice?
    roll = dice(2)
    if roll == 1:
        gender = "Male" 
    else:
        gender = "Female"
    print(f"You were born a {gender}.")
    name = input("What is your name? ")
    sheet = {'Name': name, "Gender": gender, "Level": level, 'EXP' : exp, 'Points': points, stat1t: stat1, stat2t: stat2, stat3t: stat3}
    return sheet

def unpackssheet():
    print()

def packsheet():
    print()