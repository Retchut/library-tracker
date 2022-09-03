from dbm.ndbm import library
import traceback
from card import Card
LIBRARY_FILE_NAME = "library.txt"

class Library:
    collection = list()

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def getCollection(self) -> list:
        return self.collection
    
    def loadLibrary(self) -> None:
        try:
            libraryFile = open(LIBRARY_FILE_NAME, "r")
        except FileNotFoundError:
            print("No library file found. Launching with an empty library.")
        else:
            print("A library.txt was detected and will be loaded.");
            success = True;
            line = 1
            for entry in libraryFile:
                # split entries by token, and remove line terminator from the entry
                cardData = entry.split("|")
                cardData[-1] = (cardData[-1])[:-1]
                try:
                    self.collection.append(Card(
                        name=cardData[0],
                        version=int(cardData[1]),
                        rarity=cardData[2],
                        expansion=cardData[3],
                        condition=cardData[4],
                        language=cardData[5],
                        firstEd=bool(cardData[6]),
                        amount=int(cardData[7]),
                        price=float(cardData[8])
                    ))
                except ValueError:
                    print("Error loading line number", line, "of the library file.")
                    print(traceback.format_exc())
                    exit(1)
                line+=1
        libraryFile.close()

    def saveLibrary(self) -> None:
        with open(LIBRARY_FILE_NAME, "w+") as libraryFile:
            for card in self.collection:
                entryString = (card.getName() + "|"
                        + str(card.getVersion()) + "|"
                        + card.getRarity() + "|"
                        + card.getExpansion() + "|"
                        + card.getCondition() + "|"
                        + card.getLanguage() + "|"
                        + str(card.isFirstEd()) + "|"
                        + str(card.getAmount()) + "|"
                        + str(card.getPrice())
                        + "\n")
                libraryFile.write(entryString)
            libraryFile.close()

    def addCard(self) -> int:
        pass

    def removeCard(self) -> int:
        pass

    def printLibrary(self) -> None:
        for card in self.collection:
            print(card)

    def printSubCollection(self) -> None:
        pass
    
    def accessCard(self) -> int:
        pass

    def sortLibrary(self, choice : int):
        pass