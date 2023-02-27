from lib import tlib as t
#Pre-Game Setup/Variable sets.
#set LibJson location.
LibJson = "lib\lib.json"
#set character defaults.
name="Trollolol Johnson"
gender="male"
age="19"
#pull the game values from LibJson.
gameName =  t.fromJson(LibJson).get('gameName')
gameState = t.fromJson(LibJson).get('gameState')
gameVersion = t.fromJson(LibJson).get('version')
menuMain = t.fromJson(LibJson).get('menuMain')
title = t.fromJson(LibJson).get('title')
gameCredits = t.fromJson(LibJson).get('credits')
#Assigning Wait Values for ease of access.
WaitShort = 1
WaitMedium = 5
WaitMild = 10
WaitLong = 20
save = {'0': 'False'}

def main():
    #ToDo: Make functional main menu
    check = True
    while check == True:
        t.clear()
        t.jsonValue(menuMain)
        option = input("/Select option: ")
        if option == "New Game" or "new game" or "New game" or "new Game" or "New" or "new" or "N" or "n":
            print()
            check = False
        elif option == "Load" or "load" or "L" or "l":
            print()
            check = False
        elif option == "Settings" or "settings" or "setting" or "Setting" or "S" or "s":
            print("There currently are no settings available in the game. This is a placeholder for when I find things I want users to have settings for.")
            t.wait(WaitMild)
            check = True
        elif option == "Quit" or "quit" or "Q" or "q":
            print("Exiting...")
            t.wait(4)
            exit()
            check = False
        else:
            print("Try entering a number 1-4.")
    #Clear screen to be sure, then use printVal for GameTitle and Version.
    t.clear()
    t.jsonValue(title)
    #Credits/opening text from file.
    GameOpening = t.fromJson(LibJson).get('intro')
    print(GameOpening.get('1'))
    t.wait(WaitShort)
    print(GameOpening.get('2'))
    t.wait(WaitShort)
    print(GameOpening.get('3'))
    t.wait(WaitShort)
    print(GameOpening.get('4'))
    t.wait(WaitShort)
    print(GameOpening.get('5'))
    t.wait(WaitShort)
    print(GameOpening.get('6'))
    t.wait(WaitShort)
    print(GameOpening.get('7'))
    t.wait(WaitMild)

    
    #ToDo:Character Creation
    ##Gender
    hold = 1
    while hold == 1:
        t.clear()
        t.jsonValue(title)
        gender = str(input("Are you male or female? : ")).lower()
        if gender == "male" or gender == "female" or gender == "m" or gender == "f":
            if gender == "m" or gender == "male":
                gender = "Male"
            else:
                gender = "Female"
            hold = 0
        else:
            print("")
            print("Please enter m, f, male, or female.")
            t.wait(WaitShort)
            hold = 1
    else:
        t.clear()
        
    
    ##Age
    hold = 1
    while hold == 1:
        try:
            t.clear()
            t.jsonValue(title)
            age = int(input("How old are you? : "))
            if age != 0:
                if age >= 9 or age <= 60:
                    hold = 0
            else:
                print("Try a number between 9 and 60!")
                t.wait(WaitShort)
                hold = 1
        except ValueError:
            print("Try a number between 9 and 60!")
            t.wait(WaitShort)
        else:
            t.clear()

    ##Race selection.
    races = t.fromJson(LibJson).get('races')
    hold = 1
    while hold == 1:
        try:
            t.clear()
            t.jsonValue(title)
            print(f"{races.get('1')}, {races.get('2')}, {races.get('3')}, {races.get('4')}, {races.get('5')}, or {races.get('6')}")
            race = input(f"Select a race from the above: ")
            if race != races.get('1') or races.get('2') or races.get('3') or races.get('4') or races.get('5') or races.get('6'):
                hold = 1
            else:
                hold = 0
        except ValueError:
            t.clear()
            t.jsonValue(title)
            print("You either misspelled the race, input something wrong, or you forgot to capitalize the first letter.")
            t.wait(WaitShort)
            print("Try again.")
            t.wait(WaitMedium)
        else:
            t.clear()
            t.jsonValue(title)
            race = race.title()
            break
            
    ##Todo: Generate initial stats, distribute starting points.
    
    ##ToDo: Make dictionary called sheet to hold stats age, name, and race.

    ##ToDo: XP/Level system.
    
    ##ToDo: Get Name!

    t.clear()
    ## Credits
    print(f"{name}, {gender}, {age}, {race}")
    t.wait(WaitMedium)
    t.clear()
    print(gameCredits.get('1'))
    t.wait(WaitShort)
    print(gameCredits.get('2'))
    t.wait(WaitMedium)
    #Finale screen clear.
    t.wait(WaitLong)
    t.clear()
        

main()