from enum import Enum
from os import get_terminal_size
from xml.etree.ElementTree import QName

class Condition(Enum):
    M = "Mint"
    NM = "Near Mint"
    EX = "Excelent"
    GD = "Good"
    LP = "Light Played"
    PL = "Played"
    P = "Poor"

class Language(Enum):
    ENGLISH = "English"
    FRENCH = "French"
    GERMAN = "German"
    SPANISH = "Spanish"
    ITALIAN = "Italian"
    PORTUGUESE = "Portuguese"

#class Rarity(Enum):
#   pass

class Card:

    name = None
    version = None
    rarity = None
    expansion = None
    condition = None
    language = None
    firstEd = None
    amount = None
    price = None

    def __init__(self, name:str, version:int, rarity:str, expansion:str, condition:str, language:str, firstEd:bool, amount:int, price:float) -> None:
        self.name = name
        self.version = version
        self.rarity = rarity
        self.expansion = expansion
        self.condition = condition
        self.language = language
        self.firstEd = firstEd
        self.amount = amount
        self.price = price
    
    def __repr__(self) -> str:
        return "Card({0},{1},{2},{3},{4},{5},{6},{7})".format(
            self.name,
            self.expansion,
            self.rarity,
            self.condition,
            self.language,
            self.firstEd,
            self.amount,
            self.price
        )

    def __str__(self) -> str:
        return "Name: {0}\nExpansion: {1}\nRarity: {2}\nCondition: {3}\nLanguage: {4}\nFirst Ed: {5}\nAmount: {6}\nPrice: {7}\n".format(
            self.name,
            self.expansion,
            self.rarity,
            self.condition,
            self.language,
            "Yes" if self.firstEd else "No",
            self.amount,
            self.price
        )

    def printSuccint(self, headerLengths) -> None:
        print("{0}|{1}|{2}|{3}|{4}".format(
            " " + str(self.amount).ljust(headerLengths[0]-1),
            " " + str(self.price).ljust(headerLengths[1]-1),
            " " + str(self.expansion).ljust(headerLengths[2]-1),
            " " + str(self.rarity).ljust(headerLengths[3]-1),
            " " + str(self.name).ljust(headerLengths[4-1])
        ))

    def getName(self) -> str:
        return self.name

    def getVersion(self) -> int:
        return self.version

    def getRarity(self) -> int:
        return self.rarity

    def getExpansion(self) -> str:
        return self.expansion

    def getCondition(self) -> Condition:
        return self.condition

    def getLanguage(self) -> Language:
        return self.language

    def isFirstEd(self) -> bool:
        return self.firstEd

    def getAmount(self) -> int:
        return self.amount

    def getPrice(self) -> float:
        return self.price

    def changeAmount(self, number:int) -> int:
        self.amount += number
