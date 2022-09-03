from library import Library
from utils import getMenuInput
from math import floor


def run() -> None:
    lib = Library()
    lib.loadLibrary()
    libraryLoop(lib)
    # lib.printLibrary()
    lib.saveLibrary()

def libraryLoop(lib) -> None:
    options = [
        "1 - View your card collection.",
        "2 - Add cards to the library.",
        "3 - Modify a card in the library.",
        "4 - Look up a specific card's value.",
        "5 - Update the price of all cards in the library.",
        "0 - Exit and save the library."
    ]
    menuOptions = [*range(len(options))]

    while(True):
        print("\nWhich action would you like to perform?")
        selectedOption = getMenuInput(menuOptions, options)
        if(selectedOption == 1):
            viewLibraryMenu(lib)
        elif(selectedOption == 2):
            addCardMenu(lib)
        elif(selectedOption == 3):
            accessCardMenu(lib)
        elif(selectedOption == 4):
            lookUpPriceMenu() # isto vai sair daqui wtf is this name
        elif(selectedOption == 5):
            updatePrices(lib)
        elif(selectedOption == 0):
            close = True

def viewLibraryMenu(lib : Library) -> None:
    if(lib.isEmpty()):
        print("The library is empty.")
        return

    options = [
        "1 - Name (Asc)",
        "2 - Name (Desc)",
        "3 - Price (Asc)",
        "4 - Price (Desc)",
        "5 - Expansion (Asc)",
        "6 - Expansion (Desc)",
        "7 - Rarity"
    ]
    menuOptions = [*range(1,len(options) + 1)]

    print("\nWhich field do you want to sort by?")
    selectedOption = getMenuInput(menuOptions, options)
    # depending on the selected option, we'll sort the library then print a subsection of the library
    # lib.sortLibrary()
    libraryScroller(lib)

    
def libraryScroller(lib : Library) -> None:
    options = [
        "1 - Scroll left",
        "2 - Scroll Right",
        "3 - Quit screen"
    ]
    menuOptions = [*range(1, len(options) + 1)]

    # calculate pages we can navigate, and number of items per page
    MAX_DISPLAY = 20
    libSize = len(lib.getCollection())
    filledPages = floor(libSize / MAX_DISPLAY)
    leftover = libSize % MAX_DISPLAY
    totalPages = filledPages + (1 if leftover else 0)

    page = 0
    lastPage = totalPages - 1
    
    while True:
        # calculate range of cards to load
        start = page * MAX_DISPLAY
        increment = 20 if not (leftover and page == lastPage) else leftover
        printPage(lib, page, lastPage, start, start + increment)

        #
        option = getMenuInput(menuOptions, options)
        if(option == 1):
            if (page == 0):
                print("Can't go back.")
            else:
                page -= 1
        elif(option == 2):
            if (page == lastPage):
                print("Can't go forward.")
            else:
                page += 1
        elif(option == 3):
            break

def printPage(lib : Library, currentPage : int, lastPage : int, start : int, end : int) -> None:
    header = [
        " Amount ",
        "  Price  ",
        " Expansion ",
        "    Rarity    ",
        " Card Name "
    ]
    print("{0}|{1}|{2}|{3}|{4}".format(*header))
    lib.printLibrary(start, end)
    print()
    print((currentPage+1), "/", (lastPage + 1))


def addCardMenu(lib : Library) -> None:
    pass

def accessCardMenu(lib : Library) -> None:
    pass

def lookUpPriceMenu() -> None:
    pass

def updatePrices(lib : Library) -> None:
    pass