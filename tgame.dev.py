from src import tlib as t


def main():
    version = "0.1"
    #credits/opening text from file.
    t.pff('lib/intro.json', 1) #expand on this function later**
    t.sleep(2)
    
    #character creation
    #Get gender
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
    
    #Get age?
    hold = 1
    while hold == 1:
        t.clear()
        t.title(version)
        age = input("How old are you?")
        if age != 0:
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