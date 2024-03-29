from math import floor
import traceback
from datetime import datetime

from models.library import Library
from utils import getMenuInput, getQueriedInput
from crawler.expansions import loadExpansions
from crawler.url_gen import buildURLs
from crawler.crawl import getPrices

CRAWL_LOGFILE = "./crawllog.txt"

def run() -> None:
    lib = Library()
    lib.loadLibrary()
    loadExpansions()
    libraryLoop(lib)
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
        print("Which action would you like to perform?")
        selectedOption = getMenuInput(menuOptions, options)
        if(selectedOption == 1):
            viewLibraryMenu(lib)
        elif(selectedOption == 2):
            addCardMenu(lib)
        elif(selectedOption == 3):
            accessCardMenu(lib)
        elif(selectedOption == 4):
            lookUpPriceMenu()
        elif(selectedOption == 5):
            updatePrices(lib)
        elif(selectedOption == 0):
            return

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
        "7 - Rarity",
        "0 - Cancel"
    ]
    menuOptions = [*range(len(options))]

    sortByName = lambda card : card.name
    sortByPrice = lambda card : card.price
    sortByExpansion = lambda card : card.expansion
    sortByRarity = lambda card : card.rarity

    print("Which field do you want to sort by?")
    selectedOption = getMenuInput(menuOptions, options)
    # depending on the selected option, we'll sort the library then print a subsection of the library
    if(selectedOption == 0):
        return
    elif(selectedOption == 1):
        lib.sortLibrary(False, sortByName)
    elif(selectedOption == 2):
        lib.sortLibrary(True, sortByName)
    elif(selectedOption == 3):
        lib.sortLibrary(False, sortByPrice)
    elif(selectedOption == 4):
        lib.sortLibrary(True, sortByPrice)
    elif(selectedOption == 5):
        lib.sortLibrary(False, sortByExpansion)
    elif(selectedOption == 6):
        lib.sortLibrary(True, sortByExpansion)
    elif(selectedOption == 7):
        lib.sortLibrary(False, sortByRarity)
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
        selectedOption = getMenuInput(menuOptions, options)
        if(selectedOption == 1):
            if (page == 0):
                print("Can't go back.")
            else:
                page -= 1
        elif(selectedOption == 2):
            if (page == lastPage):
                print("Can't go forward.")
            else:
                page += 1
        elif(selectedOption == 3):
            break

def printPage(lib : Library, currentPage : int, lastPage : int, start : int, end : int) -> None:
    header = [
        " Amount ",
        " Price   ",
        " Expansion ",
        " Rarity       ",
        " Card Name "
    ]
    headerLengths = [len(x) for x in header]
    print("{0}|{1}|{2}|{3}|{4}".format(*header))
    lib.printLibrary(start, end, headerLengths)
    print()
    print((currentPage+1), "/", (lastPage + 1))


def addCardMenu(lib : Library) -> None:
    queries = {
        'name' : "Please input the card's name: ",
        'version' : "If this card has any alternate versions in this set, please input that version's number. Print 0 if it has none: ",
        'rarity' : "Please input the rarity: ",
        'expansion' : "Please input the expansion: ",
        'condition' : "Please input the condition (M/NM/EX/GD/LP/PL/P): ",
        'language' : "Please input the language: ",
        'edition' : "Is the card 1st ed? (y/n): ",
        'amount' : "Please input the number of copies you have: "
    }
    validRarities = []
    validExpansion = []
    validConditions = ["M", "NM", "EX", "GD", "LP", "PL", "P"]
    validLanguages = [ "English", "French", "German", "Spanish", "Italian", "Portuguese" ]
    validEditions = ['y', 'n']

    result = getQueriedInput(queries)
    # perform checks on the input
    try:
        name = result["name"]

        check = "version"
        version = result["version"]
        if int(version) < 0:
            raise ValueError

        check = "rarity"
        rarity = result["rarity"]
        # TODO: check if rarity exists

        check = "expansion"
        expansion = result["expansion"]
        # TODO: check if expansion is in expansion map

        check = "condition"
        condition = result["condition"].capitalize()
        if(condition not in validConditions):
            raise ValueError

        check = "language"
        language = result["language"].capitalize()
        if language not in validLanguages:
            raise ValueError

        check = "edition"
        if(result['edition'] not in validEditions):
            raise ValueError
        firstEd = True if result["edition"] == 'y' else False

        check = "amount"
        amount = int(result["amount"])

        price = 0.0 # TODO: fetch from crawler later
    except ValueError:
        print("Error parsing {0}. Please input a valid {0}.\n".format(check))
    else:
        lib.addCard([name, version, rarity, expansion, condition, language, firstEd, amount, price])

def accessCardMenu(lib : Library) -> None:
    print("Not yet implemented")

def lookUpPriceMenu() -> None:
    print("Not yet implemented")

def updatePrices(lib : Library) -> None:
    # TODO: Find a way to update all cards with the same name and expansion at once
    # TODO: Also save prices besides the fromPrice
    # TODO: Add remaining expansions to the expansions file
    # TODO: Fix miscelaneous issues with the crawler
    # TODO: Rewrite crawler in scrapy because it is faster and allows for more control when crawling
    crawl_logfile = open(CRAWL_LOGFILE, 'a+')
    update_time = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
    crawl_logfile.write("\n------------------------------\n" + update_time + "\n------------------------------\n")

    print("Updating prices...")

    lib.sortLibrary(False, lambda card : card.name)
    checkedCardNames = []
    prevPrice = 0.0
    for card in lib.getCollection():
        # multiple cards with the same name
        if card.getName() in checkedCardNames:
            card.updatePrice(prevPrice)
            continue
        logmsg = "\n" + card.getName()
        print(logmsg)

        prices = getPrices(buildURLs(card, crawl_logfile), crawl_logfile)
        if prices == {}:
            crawl_logfile.write(logmsg + "\n")
            failure_str = "Error fetching {0}({1})'s price. No changes were made...".format(card.getName(), card.getExpansion())
            print(failure_str)
            crawl_logfile.write(failure_str + "\n")
            continue
        card.updatePrice(prices['fromPrice'])
        checkedCardNames.append(card.getName())
        prevPrice = prices['fromPrice']

        success_str = "Updated {0}({1})'s price successfully.".format(card.getName(), card.getExpansion())
        print(success_str)

    crawl_logfile.close()

if __name__ == '__main__':
    run()