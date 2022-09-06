import os, platform

def clearConsole():
    currentOS = platform.system()
    if(currentOS == 'Windows'):
        os.system('cls')
    elif(currentOS == 'Linux'):
        os.system('clear')

def getMenuInput(menuOptions : list, menuTexts : list) -> int:
    errorMsg = "You must input a valid integer."

    for optionText in menuTexts:
        print(optionText)

    while(True):
        try:
            inputOption = int(input("Please input an option: "))
        except ValueError:
            print(errorMsg)
        else:
            if(inputOption in menuOptions):
                clearConsole()
                return inputOption
            print(errorMsg)

def getQueriedInput(queries : dict) -> dict:
    queryResult = dict()
    for varName in queries:
        queryInput = input(queries[varName])
        queryResult[varName] = queryInput
    print() # purely for aesthetics
    return queryResult

def binarySearch(container : list, start, end, name):
    if start == end:
        return start if (container[start].name == name) else -1
    

        #array with 1 item
        #if(start == end){
        #    return (arr.get(start).getCardInfo().getName().equals(name))? start : -1;
        #}
        #//array of a different size
        #else if (end > start){
        #    //get the index of the middle of the array
        #    int mid = start + (end-start)/2;
        #    int test = name.compareTo(arr.get(mid).getCardInfo().getName());
        #    if(test == 0)
        #        return mid;
        #    else if(test < 0){  //elem in left side of the array
        #        return binarySearch(arr, start, mid, name);
        #    }
        #    else if(test > 0){  //elem in right side of the array
        #        return binarySearch(arr, mid+1, end, name);
        #    }
        #}
#
        #//in case something goes wrong
        #return -1;