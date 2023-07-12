from random import randint

class game():
    def rollDice(sides):
        roll = randint(1, sides) # type: ignore
        return roll
    
    def fromDic(dic):
        for i,v in dic: # type: ignore
            print(f"{i}:{v}")

    class charInit():
        ##Defaults
        statusDefault = {
            "fName":"Mafe",
            "lName":"Roe",
            "Level": 0,
            "Exp":0,
            "Stats":{
                "Physical":{
                    "Strength":3,
                    "Agility":3
                    },
                "Spirit":{
                    "Lore":3,
                    "Determination":3
                },
                "Mental":{
                    "Intelligence":3,
                    "Charisma":3
                }
            }
        }
        def create(statusDefault):
            print()
            

class tFormat():
    def fCode(code):
        return "\33[{code}m".format(code=code)

    def fClear():
        print(tFormat.fCode(0)) # type: ignore

    def cJustify(text, width=-1):
      lines = text.split('\n') # type: ignore
      width = max(map(len, lines)) if width == -1 else width
      return '\n'.join(line.center(width) for line in lines)

    def rJustify(text,width=-1):
        lines = text.split('\n') # type: ignore
        width = max(map(len,lines)) if width == -1 else width
        return '\n'.join(line.rjust(width) for line in lines)

    def fTitle(text,width=100,bg="40",st="31",cc="1"):
        print(tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc),end="") # type: ignore
        text = tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc) + text # type: ignore
        print(tFormat.cJustify(text,width))
        tFormat.cclear() # type: ignore