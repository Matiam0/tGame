import lib.rtsystems as rts
import lib.rtstoryteller as rtst

def main():
    # get name stored for later use.s
    name = char_naming()
    
    # create character sheet
    sheet = char_creation(name)
    
    # give the ending screen time to be fully read. 5 seconds default?
    rtst.scs(sheet)
    rts.sleep(5)
    rts.clear()


# get name for character
def char_naming():
    name = input("What is your name? ")
    return name


#create a character
def char_creation(name):
    points = rtst.dice(12)
    
    #assign rolled points to character sheet loop till 0
    while points != 0:
        print(f"How would you like to assign your {points} points?")
        stat1start = 3
        stat2start = 3
        stat3start = 3
        #Distribute point's rolled between Str, Agi, and Int.
        print(f"Your starting stats are: ") 
        print(f"Strength : {stat1start}")
        print(f"Agility : {stat2start}")
        print(f"Intelligence : {stat3start}")
        print()
        rts.sleep(5)
        
        #may scrap this in favor of 6 side roll per stat.
        try:
            stat1 = stat1start + int(input("How many points into STR? "))
            points = points - stat1
            print(f"You have {points} points left.")
            if points < 0:
                print("Too few points!")
                points = points + stat1
                stat1 = stat1start
                print(f"{points} points remian")
                rts.sleep(2)
            elif points == 0:
                break
            
            stat2 = stat2start + int(input("How many points into AGI? "))
            points = points - stat2
            print(f"You have {points} points left.")
            if points < 0:
                print("Too few points!")
                points = points + stat2
                stat2 = stat2start
                print(f"{points} points remian")
                rts.sleep(2)
            elif points == 0:
                break
            
            stat3 = stat3start + int(input("How many points into INT? "))
            points = points - stat3
            print(f"You have {points} points left.")
            if points < 0:
                print("Too few points!")
                points = points + stat3
                stat3 = stat3start
                print(f"{points} points remian")
                rts.sleep(2)
            elif points == 0:
                break
            
        except SyntaxError:
            pass
        
        except ValueError:
            pass
    rts.clear()
        
    #pass stats to sheet, and return them
    sheet = {'Name': name, 'STR': stat1, 'AGI': stat2,'INT': stat3}
    return sheet


main()