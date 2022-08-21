import src.tlib as t
import json

def main():
    #credits/opening text from file.
    textlib = t.loadfile("src/textlib.json")
    sleeptime = 3
    print(textlib.get('ocredit'))
    t.sleep(sleeptime)
    print(textlib.get('ocredit-1'))
    t.sleep(sleeptime)
    print(textlib.get('ocredit-2'))
    t.sleep(sleeptime)
    print(textlib.get('ocredit-3'))
    t.sleep(sleeptime)
    print(textlib.get('ocredit-4'))
    t.sleep(sleeptime)
    
    #Character creation.
    t.clear()
    sheet = t.ccreate()
    t.clear()
    t.scs(sheet)
    t.sleep(5)
    

main()