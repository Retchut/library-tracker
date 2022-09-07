from card import Card
from expansions import expansions

def buildURLs(card : Card) -> list:
    possibleURLs  = []
    url = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/"
    urlExpansion = getUrlExpansion(card.getExpansion())
    if urlExpansion == "":
        return []
    else:
        url += urlExpansion
    return getCompleteURLs(url, card.getName(), card.getVersion(), card.getRarity())

def getUrlExpansion(expansionKey : str) -> str:
    try:
        expansionURL = expansions[expansionKey]
    except KeyError:
        print(expansionKey + ": There's no such expansion")
        return ""
    else:
        return expansionURL + '/'

def getCompleteURLs(url : str, name : str, version : int, rarity : str):
    possibleURLs = []
    if version > 0 :
        #Add the 4 possible different urls that cardmarket may use for the item, in order of most common to least common
        possibleURLs.append(url + urlify(name + " (V" + str(version) + " " + rarity + ")"))
        possibleURLs.append(url + urlify(name + " (V-" + str(version) + " " + rarity + ")"))
        possibleURLs.append(url + urlify(name + " (V" + str(version) + ")"))
        possibleURLs.append(url + urlify(name + " (V-" + str(version) + ")"))
    else:
        possibleURLs.append(url + urlify(name))
    return possibleURLs

def urlify(string : str):
    #Characters cardmarket seems to ignore, when creating the url of cards
    ignoreChars = [ '"', '?', '!', ',', '@', '/', '&', '=', ':', '(', ')', '.']

    # TODO: check this
    for i in range(len(string)):
        current = string[i]
        if current not in ignoreChars:
            continue
        elif (current == '-' or current == ' '):
            #replace space with '-', or write '-', if one hasn't been already written
            if(string[:-1] != '-'):
                string += '-'
        else:
            #add normal char to url
            string += current
    return string