# roll a dice with {a} number of sides
def dice(sides):
    import random
    roll = random.randint(1, sides)
    return roll

#define choice with two options
def choice2(c1, c2):
    in1 = input(f"{c1}, or {c2}? ")
    if in1 == c1:
        c0 = 0
    else:
        c0 = 1
    return c0

def choice3(c1, c2, c3):
    in1 = input(f"{c1}, {c2}, or {c3}")
    if in1 == c1:
        c0 = 0
    elif in1 == c2:
        c0 = 1
    else:
        c0 = 3
    return c0

def choice4(c1, c2, c3, c4):
    in1 = input(f"{c1}, {c2}, {c3}, or {c4}")
    if in1 == c1:
        c0 = 0
    elif in1 == c2:
        c0 = 1
    elif in1 == c3:
        c0 = 2
    else:
        c0 = 3
    return c0

def scs(sheet):
    for key, value in sheet.items():
        print(key, ':', value)

def sedit(points,stat):
    while points != 0:
        print(f"You have {points} left.")
        stat = points - int(input(f"How many points do you want to add to {stat}? "))
        if points < 0:
            print(f"{points} is an Invalide Point Value.")
            rts.sleep(4) #ignore, start.py imports rtsystems rendering this error moot.
            break
        else:
            stat = points
            return stat
    else:
        stat = points
        return stat