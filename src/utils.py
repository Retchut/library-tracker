def getMenuInput(menuTexts : list) -> int:
    for optionText in menuTexts:
        print(optionText)
    
    menuOptions = [*range(len(menuTexts))]
    while(True):
        try:
            inputOption = int(input("Please input an option: "))
        except ValueError:
            print("You must input a valid integer.")
        else:
            if(inputOption in menuOptions):
                return inputOption
            print("That option does not exist.")