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

#file loading
def loadfile(file):
    import json
    f = open(file)
    out = json.load(f)
    return out

#RPG defs/ non-system type.
#Dice roller.
def dice(sides):
    import random
    roll = random.randint(1, sides)
    return roll

#2 choices
def choice2(c1, c2):
    in1 = input(f"{c1}, or {c2}? ")
    if in1 == c1:
        c0 = 1
    else:
        c0 = 2
    return c0

#3 choices
def choice3(c1, c2, c3):
    in1 = input(f"{c1}, {c2}, or {c3}? ")
    if in1 == c1:
        c0 = 1
    elif in1 == c2:
        c0 = 2
    else:
        c0 = 3
    return c0

#4 choices
def choice4(c1, c2, c3, c4):
    in1 = input(f"{c1}, {c2}, {c3}, or {c4}? ")
    if in1 == c1:
        c0 = 1
    elif in1 == c2:
        c0 = 2
    elif in1 == c3:
        c0 = 3
    else:
        c0 = 4
    return c0

#show character sheet
def scs(sheet):
    for key, value in sheet.items():
        print(key, ':', value)

#Character sheet edit/stat edit.
def sedit(name, points, stat1t, stat2t, stat3t, stat1, stat2, stat3):
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
    sheet = {'Name': name, stat1t: stat1, stat2t: stat2, stat3t: stat3}
    return sheet

def ccreate():
    print()