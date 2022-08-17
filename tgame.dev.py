import src.rtlib as rt
import json

def main():
    #credits/opening text from file.
    textlib = rt.loadfile("src/textlib.json")
    sleeptime = 3
    print(textlib.get('ocredit'))
    rt.sleep(sleeptime)
    print(textlib.get('ocredit-1'))
    rt.sleep(sleeptime)
    print(textlib.get('ocredit-2'))
    rt.sleep(sleeptime)
    print(textlib.get('ocredit-3'))
    rt.sleep(sleeptime)
    print(textlib.get('ocredit-4'))
    rt.sleep(sleeptime)
    
    #Character creation.
    rt.clear()
    sheet = rt.ccreate()
    rt.clear()
    rt.scs(sheet)
    rt.sleep(5)
    

main()