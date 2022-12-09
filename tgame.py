from lib import tlib as t
# Easy to edit Game; Version, Title. While Adding in Hooks for Json Text Libraries.
LibJson = "lib\lib.json"
GameVersion = t.fromJsonKey(LibJson,'version')
GameState = t.fromJsonKey(LibJson,'gamestate')
if GameState == "dev":
    GameTitle = {"line1":f"tGame [Dev] {GameVersion}","line2":"_______________________","line3":""}
elif GameState == "troll":
    GameTitle = {"line1":f"tGame [Troll] {GameVersion}","line2":"_______________________","line3":""}
else:
    GameTitle = {"line1":f"tGame {GameVersion}","line2":"_______________________","line3":""}
name="pc"
gender="male"
age="19"


def main(GameTitle, LibJson):
#Assigning Wait Values for ease of access.
    WaitShort = 1
    WaitMedium = 5
    WaitMild = 10
    WaitLong = 20
#Clear screen to be sure, then use printVal for GameTitle and Version.
    t.clear()
    t.printVal(GameTitle)
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
        t.printVal(GameTitle)
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
            t.printVal(GameTitle)
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
            t.printVal(GameTitle)

##ToDo: Race selection.
    
##Todo: Generate initial stats, distribute starting points.
    
##ToDo: Make dictionary called sheet to hold stats age, name, and race.

##ToDo: XP/Level system.

    t.clear()
## Credits
    t.printVal(GameTitle)
    print(name, gender, age)
    GameCredits = t.fromJsonKey(LibJson, 'credits')
    print(GameCredits.get('1'))
    t.wait(WaitShort)
    print(GameCredits.get('2'))
    t.wait(WaitMedium)
#Finale screen clear.
    t.wait(WaitLong)
    t.clear()
        

main(GameTitle, LibJson)