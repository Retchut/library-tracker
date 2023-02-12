from typing import TextIO

from crawler.expansions import expansions
from models.card import Card

def buildURLs(card : Card, logfile : TextIO) -> list:
    possibleURLs  = []
    url = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/"
    urlExpansion = getUrlExpansion(card.getExpansion(), logfile)
    if urlExpansion == "":
        return []
    else:
        url += urlExpansion
    return getCompleteURLs(url, card.getName(), card.getVersion(), card.getRarity())

def getUrlExpansion(expansionKey : str, logfile : TextIO) -> str:
    try:
        expansionURL = expansions[expansionKey]
    except KeyError:
        keyerror_str = expansionKey + ": There's no such expansion"
        print(expansionKey + ": There's no such expansion")
        logfile.write(keyerror_str + "\n")
        return ""
    else:
        return expansionURL + '/'

def getCompleteURLs(url : str, name : str, version : int, rarity : str):
    possibleURLs = []
    possibleNames = getPossibleNames(name)
    if version > 0 :
        # first name in the list is most likely
        for name in possibleNames:
            #Add the 4 possible different urls that cardmarket may use for the item, in order of most common to least common
            version_strings = [
                name + " (V" + str(version) + " " + rarity + ")",
                name + " (V-" + str(version) + " " + rarity + ")",
                name + " (V" + str(version) + ")",
                name + " (V-" + str(version) + ")"
            ]
            for version_str in version_strings:
                possibleURLs.append(url + urlify(version_str))
    else:
        for name in possibleNames:
            possibleURLs.append(url + urlify(name))
    fixedURLs = fixApostropheURLs(possibleURLs)
    return fixedURLs

# if the name of a card contains a dash, it can be either ignored or maitained, seemingly at random
# this function takes into account both possibilities
def getPossibleNames(name : str):
    possibleNames = [ name ]
    possibleNames.append(name.replace('-', ''))
    return possibleNames

def urlify(string : str):
    #Characters cardmarket seems to ignore, when creating the url of cards
    ignoreChars = [ '"', '?', '!', ',', '@', '/', '&', '=', ':', '(', ')', '.']
    replaceWithDash = [ '-', ' ' ]

    urlString = ""
    for c in string:
        if c in ignoreChars:
            continue
        elif(c in replaceWithDash):
            # write '-' only if the previous character written was not a '-'
            if(urlString[-1] != '-'):
                urlString += '-'
        else:
            # preserve char
            urlString += c

    return urlString

# in the case that the card name contains an apostrophe, cardmarket either ignores it, or
# replaces it with a dash, seemingly at random
# this function accounts for all those versions
def fixApostropheURLs(generatedURLs):
    fixedURLs = []
    for url in generatedURLs:
        if '\'' in url:
            ignoreApostrophe = url.replace('\'', '')
            replaceWithDash = url.replace('\'', '-')
            fixedURLs.extend([ignoreApostrophe, replaceWithDash])
        else:
            fixedURLs.append(url)
    return fixedURLs

# in the case that the card name contains a dash, cardmarket either ignores it, or
# replaces it with a dash, seemingly at random
# this function accounts for all those versions
def fixDashURLs(generatedURLs):
    fixedURLs = []
    for url in generatedURLs:
        if '-' in url:
            ignoreApostrophe = url.replace('\'', '')
            replaceWithDash = url.replace('\'', '-')
            fixedURLs.extend([ignoreApostrophe, replaceWithDash])
        else:
            fixedURLs.append(url)
    return fixedURLs