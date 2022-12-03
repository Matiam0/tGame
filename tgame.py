from src import tlib as t
# Easy to edit Game; Version, Title. While Adding in Hooks for Json Text Libraries.
GameVersion = "0.1"
GameTitle = {"line1":f"tGame [Dev] {GameVersion}","line2":"_______________________","line3":""}
IntroJson = "lib\intro.json"
CreditsJson = "lib\Credits.json"

def main(GameTitle, IntroJson, CreditsJson):
    t.clear()
    t.title(GameTitle)
#Credits/opening text from file.
# This is an example of t.fromJsonKey() using a key to get the value.
    GameOpening = t.fromJsonKey(IntroJson, 'opening')
    print(GameOpening)

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
        t.title(GameTitle)
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
        t.title(GameTitle)
        age = int(input("How old are you? : "))
        if age != 0:
            if age >= 0:
                hold = 0
        else:
            hold = 1
    else:
        t.clear()
        t.title(GameTitle)
##ToDo: Race selection.
    
##Todo: Generate initial stats, distribute starting points.
    
##ToDo: Make dictionary called sheet to hold stats age, name, and race.

##ToDo: XP/Level system.

    t.clear()
        
        

main(GameTitle, IntroJson, CreditsJson)