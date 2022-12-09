from lib import tlib as t
# Easy to edit Game; Version, Title. While Adding in Hooks for Json Text Libraries.
LibJson = "lib\lib.json"
name="pc"
gender="male"
age="19"


def main(LibJson):
    #ToDo: Make main menu

    #Assigning Wait Values for ease of access.
    WaitShort = 1
    WaitMedium = 5
    WaitMild = 10
    WaitLong = 20
    #Clear screen to be sure, then use printVal for GameTitle and Version.
    t.clear()
    t.title()
    #Credits/opening text from file.
    GameOpening = t.fromJsonKey(LibJson, 'intro')
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
                if age >= 0:
                    hold = 0
            else:
                hold = 1
        except ValueError:
            print("Try a number!")
            t.wait(WaitShort)
        else:
            t.clear()
            t.printVal()

    ##ToDo: Race selection.
    races = t.fromJsonKey(LibJson, 'races')
    hold = 1
    while hold == 1:
        try:
            t.clear()
            t.title()
            print(f"{races.get('1')}, {races.get('2')}, {races.get('3')}, {races.get('4')}, or {races.get('5')}")
            race = input(f"Select a race from the above. ")
            if race != races.get('1') or races.get('2') or races.get('3') or race.get('4') or race.get('5'):
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
            
    ##Todo: Generate initial stats, distribute starting points.
    
    ##ToDo: Make dictionary called sheet to hold stats age, name, and race.

    ##ToDo: XP/Level system.

    t.clear()
    ## Credits
    t.printVal()
    print(name, gender, age, race)
    GameCredits = t.fromJsonKey(LibJson, 'credits')
    print(GameCredits.get('1'))
    t.wait(WaitShort)
    print(GameCredits.get('2'))
    t.wait(WaitMedium)
    #Finale screen clear.
    t.wait(WaitLong)
    t.clear()
        

main(LibJson)