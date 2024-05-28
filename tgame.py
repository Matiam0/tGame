
import os

os.system('color')
# !Import above this line.

# !Section for default variables
screenWidth = 100


class fmt():  # !Text Formatting options go in this class.

    def ansi(code="0;37;40m"):
        Out = "\033[" + code
        return Out


class cs():  # !CharacterSheet functions go in this class.

    def create():  # Todo Character creation will go here.
        print()

    def edit():  # Todo Edit characters, aka use skill points and change stats.
        print()

    def save():  # Todo Make basic Save/Load for characters.
        print()

    def load():
        print()

# !Anything not falling into the above classes will go here as game functions.


class game():

    # Todo Roll a dice with x number of sides and return the number.
    def dice(number):
        print()

    def settings(setting, id):
        print()


def main():
    print(fmt.ansi("1;35;40m") + "|" + "Test".center(screenWidth,"-") + "|" + fmt.ansi())
    print("|" + fmt.ansi("3m") + "Yes".ljust(screenWidth) + fmt.ansi() + "|")
    print("|" + fmt.ansi("3m") + "No".ljust(screenWidth) + fmt.ansi() + "|")


main()
