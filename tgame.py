
import json
import colorama
import os

os.system('color')
# !Import above this line.

# !Section for default variables
defaultSettings = {
    'screenWidth': 100
}

class format():  # !Text Formatting options go in this class.

    def ansi(code="0;37;40m"):
        Out = "\033[" + code
        return Out


class character():  # !CharacterSheet functions go in this class.

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
    print()


main()
