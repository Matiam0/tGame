from src import tlib as t
import json

def main():
    version = "0.1"
    #Credits/opening text from file.
    t.pfjson("lib\intro.json", 'opening') #Still needs fixed. Probably need a refresher
    t.sleep(2)
    
    #Character Creation
    #Gender.
    hold = 1
    while hold == 1:
        t.clear()
        t.title(version)
        gender = str(input("Are you male or female? : ")).lower()
        if gender == "male" or gender == "female":
            hold = 0
        else:
            hold = 1
    else:
        t.clear()
        t.title(version)
    
    #Age. Come back later to decide how to handle non-integer values.
    hold = 1
    while hold == 1:
        t.clear()
        t.title(version)
        age = int(input("How old are you? : "))
        if age != 0:
            if age >= 0:
                hold = 0
        else:
            hold = 1
    else:
        t.clear()
        t.title(version)
    #Get race?
    
    #Get stats
    
    #Print/Make sheet!

        
        

main()