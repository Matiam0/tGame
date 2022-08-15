import src.rtlib as rt
import json

def main():
    #credits/opening text from file.
    textlib = rt.loadfile('src/textlib.json')
    for open in textlib.get('ocredit'):
        print(open, sep="", end="")
    rt.sleep(5)
    
    #Character creation.
    sheet = rt.ccreate()
    

main()