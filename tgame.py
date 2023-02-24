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
#Assigning Wait Values for ease of access.
WaitShort = 1
WaitMedium = 5
WaitMild = 10
WaitLong = 20
save = {'0': 'False'}

def main(save):
    #ToDo: Make main menu
    t.menu(save)
    #Clear screen to be sure, then use printVal for GameTitle and Version.
    t.clear()
    t.title()
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
        t.title()
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
            t.title()
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
            t.title()
            print(f"{races.get('1')}, {races.get('2')}, {races.get('3')}, {races.get('4')}, {races.get('5')}, or {races.get('6')}")
            race = input(f"Select a race from the above: ")
            if race != races.get('1') or races.get('2') or races.get('3') or races.get('4') or races.get('5') or races.get('6'):
                hold = 1
            else:
                hold = 0
        except ValueError:
            t.clear()
            t.title()
            print("You either misspelled the race, input something wrong, or you forgot to capitalize the first letter.")
            t.wait(WaitShort)
            print("Try again.")
            t.wait(WaitMedium)
        else:
            t.clear()
            t.title()
            race = race.title()
            break
            
    ##Todo: Generate initial stats, distribute starting points.
    
    ##ToDo: Make dictionary called sheet to hold stats age, name, and race.

    ##ToDo: XP/Level system.
    
    ##ToDo: Get Name!

    t.clear()
    ## Credits
    print(f"{name}, {gender}, {age}, {race}")
    GameCredits = t.fromJson(LibJson).get('credits')
    print(GameCredits.get('1'))
    t.wait(WaitShort)
    print(GameCredits.get('2'))
    t.wait(WaitMedium)
    #Finale screen clear.
    t.wait(WaitLong)
    t.clear()
        

main(LibJson)