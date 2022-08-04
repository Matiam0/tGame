import lib.rtsystems as rts
import lib.rtstoryteller as rtst

def main():
    # get name stored for later use.s
    name = char_naming()
    
    # create character sheet
    sheet = char_creation(name)
    
    # give the ending screen time to be fully read. 9 seconds default?
    rtst.scs(sheet)
    rts.sleep(9)
    rts.clear()
    
    #Intro text scroll?
    intro()
    


# get name for character
def char_naming():
    name = input("What is your name? ")
    return name


#create a character
def char_creation(name):
    
    #Set base stats
    stat1 = 3
    stat1t = "STR"
    stat2 = 3
    stat2t = "AGI"
    stat3 = 3
    stat3t = "INT"
    #Roll for total points
    points = rtst.dice(6) + rtst.dice(6) + rtst.dice(6)
    #Call sedit to edit stats, and get character sheet out.
    sheet = rtst.sedit(name, points, stat1t, stat2t, stat3t, stat1, stat2, stat3)
    #pass stats to sheet, and return them
    
    return sheet

def intro():
    print()

main()