from src import tlib as t

GameTitle = "tGame [Dev]"
GameVersion = "0.1"
IntroJson = "lib\intro.json"

def main(GameTitle, GameVersion, IntroJson):
    t.clear()
    t.title(GameTitle, GameVersion)
    #Credits/opening text from file.
    GameOpening = t.fromJson(IntroJson, 'opening')
    print(GameOpening)
    t.sleep(2)
    
    #Character Creation
    #Gender.
    hold = 1
    while hold == 1:
        t.clear()
        t.title(GameTitle, GameVersion)
        gender = str(input("Are you male or female? : ")).lower()
        if gender == "male" or gender == "female":
            hold = 0
        else:
            hold = 1
    else:
        t.clear()
        t.title(GameTitle, GameVersion)
    
    #Age. Come back later to decide how to handle non-integer values.
    hold = 1
    while hold == 1:
        t.clear()
        t.title(GameTitle, GameVersion)
        age = int(input("How old are you? : "))
        if age != 0:
            if age >= 0:
                hold = 0
        else:
            hold = 1
    else:
        t.clear()
        t.title(GameTitle, GameVersion)
    #Get race?
    
    #Get stats
    
    #Print/Make sheet!

        
        

main(GameTitle, GameVersion, IntroJson)