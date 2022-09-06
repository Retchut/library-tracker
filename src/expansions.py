expansions = {}
EXPANSIONS_FILE_NAME = "expansions.txt"

def loadExpansions() -> bool:
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

    # static Map<String, String> expansions;

    # static{
    #     expansions = new HashMap<>();
    #     File expansionsFile = new File("expansions.txt");
    #     int line = 0;
    #     try{
    #         Scanner fileReader = new Scanner(expansionsFile);
    #         fileReader.useDelimiter("[,\\r\\n]");
    #         String expansionName, expansionURL;
    #         while(fileReader.hasNextLine()){
    #             expansionName = fileReader.next();
    #             if(expansionName.charAt(0) == '/'){
    #                 line++;
    #                 fileReader.nextLine();
    #                 continue;
    #             }
    #             expansionURL = fileReader.next();
    #             expansions.put(expansionName, expansionURL);
    #             line++;
    #             fileReader.nextLine();
    #         }
    #         fileReader.close();
    #     }
    #     catch (IOException e){
    #         throw new RuntimeException("Exception while initializing expansion map");
    #     }
    #     catch (NoSuchElementException e){
    #         System.out.println("Error reading expansion at line " + line);
    #         e.printStackTrace();
    #         throw new RuntimeException("Exception while initializing expansion map");
    #     }
    # }

    # public static String getExpansion(String key){
    #     if(expansions.containsKey(key))
    #         return expansions.get(key);
    #     return "";
    # }