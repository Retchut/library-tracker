expansions = {}
EXPANSIONS_FILE_NAME = "expansions.txt"

def loadExpansions() -> None:
    try:
        expansionsFile = open(EXPANSIONS_FILE_NAME, "r")
    except FileNotFoundError:
        print("No expansions file found.")
        return False
    else:
        print("Building expansion dictionary.")
        lineNum = 1
        for line in expansionsFile:
            if line[0:2] != "//":
                expansion, url = line.split(",")
                url = url[:-1]
                expansions[expansion] = url
            lineNum += 1
    return True