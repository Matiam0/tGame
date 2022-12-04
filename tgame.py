from src import tlib as t
# Easy to edit Game; Version, Title. While Adding in Hooks for Json Text Libraries.
GameVersion = "0.1.12"
GameTitle = {"line1":f"tGame [Dev] {GameVersion}","line2":"_______________________","line3":""}
IntroJson = "lib\intro.json"
CreditsJson = "lib\credits.json"

def main(GameTitle, IntroJson, CreditsJson):
#Assigning Wait Values for ease of access.
    WaitShort = 1
    WaitMedium = 5
    WaitMild = 10
    WaitLong = 20
#Clear screen to be sure, then use printVal for GameTitle and Version.
    t.clear()
    t.printVal(GameTitle)
#Credits/opening text from file.
# This is an example of t.fromJsonKey() using a key to get the value.
    GameOpening1 = t.fromJsonKey(IntroJson, '1')
    GameOpening2 = t.fromJsonKey(IntroJson, '2')
    GameOpening3 = t.fromJsonKey(IntroJson, '3')
    GameOpening4 = t.fromJsonKey(IntroJson, '4')
    GameOpening5 = t.fromJsonKey(IntroJson, '5')
    GameOpening6 = t.fromJsonKey(IntroJson, '6')
    GameOpening7 = t.fromJsonKey(IntroJson, '7')
    print(GameOpening1)
    t.wait(WaitShort)
    print(GameOpening2)
    t.wait(WaitShort)
    print(GameOpening3)
    t.wait(WaitShort)
    print(GameOpening4)
    t.wait(WaitShort)
    print(GameOpening5)
    t.wait(WaitShort)
    print(GameOpening6)
    t.wait(WaitShort)
    print(GameOpening7)
    t.wait(WaitMild)

# This is an example of t.fromJson(), t.printDic(), t.printKey(), & t.printVal().
#    TestJson = t.fromJson(IntroJson)
#    t.printDic(TestJson)
#    t.printKey(TestJson)
#    t.printVal(TestJson)
#    t.sleep(4)
    
#ToDo:Character Creation
##Gender
    hold = 1
    while hold == 1:
        t.clear()
        t.printVal(GameTitle)
        gender = str(input("Are you male or female? : ")).lower()
        if gender == "male" or gender == "female":
            hold = 0
        else:
            hold = 1
    else:
        t.clear()
    
##Age
##!Come back later to decide how to handle non-integer values.
##?Hold loops while useful can be messy, maybe look at a try loop.
    hold = 1
    while hold == 1:
        t.clear()
        t.printVal(GameTitle)
        age = int(input("How old are you? : "))
        if age != 0:
            if age >= 0:
                hold = 0
        else:
            hold = 1
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
    GameCredits1 = t.fromJsonKey(CreditsJson, "1")
    print(GameCredits1)
    t.wait(WaitMedium)
#Finale screen clear.
    t.wait(WaitLong)
    t.clear()
        

main(GameTitle, IntroJson, CreditsJson)