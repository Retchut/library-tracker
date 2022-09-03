from library import Library
from utils import getMenuInput

mainMenuOptions = [
    "1 - View your card collection.",
    "2 - Add cards to the library.",
    "3 - Modify a card in the library.",
    "4 - Remove cards from the library.",
    "5 - Look up a specific card's value.",
	"6 - Update the price of all cards in the library.\n", # newline here for aesthetics(tm)
    "0 - Exit and save the library."
]


def run() -> None:
    lib = Library()
    lib.loadLibrary()
    libraryLoop(lib)
    # lib.printLibrary()
    lib.saveLibrary()

def libraryLoop(lib) -> None:
    close = False
    while(not close):
        # wanted the list generated by the range to have 0 as the last number here
        selectedOption = getMenuInput(mainMenuOptions)
        if(selectedOption == 1):
            viewLibrary(lib)
        elif(selectedOption == 2):
            addCard(lib)
        elif(selectedOption == 3):
            accessCard(lib)
        elif(selectedOption == 4):
            removeCard(lib)
        elif(selectedOption == 5):
            lookUpPrice()
        elif(selectedOption == 6):
            updatePrices(lib)
        elif(selectedOption == 0):
            close = True

def viewLibrary(lib : Library) -> None:
    pass

def addCard(lib : Library) -> None:
    pass

def accessCard(lib : Library) -> None:
    pass

def removeCard(lib : Library) -> None:
    pass

def lookUpPrice() -> None:
    pass

def updatePrices(lib : Library) -> None:
    pass