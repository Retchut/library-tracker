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
                return inputOption
            print(errorMsg)