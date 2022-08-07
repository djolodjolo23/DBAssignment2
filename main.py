from query_handler import *

incrementNumber = 0


while True:
    incrementNumber += 1
    try:
        mycursor.execute("USE {}".format(DB_NAME))
        print("========================================================================")
        print("Sucessfuly connected to {} database".format(DB_NAME))
        print("========================================================================")
    except mysql.connector.Error as err:
        print("Database {} does not exist".format(DB_NAME))
        break
    while incrementNumber > 0:
        introText()
        mainEntry = int(input("Check the menu and provide a number:"))
        print("-> KEY " + str(mainEntry) + " PRESSED <-")
        print("Executing...")
        print("------------")
        if mainEntry == 1:
            subEntry = str(input("Provide a recipe name:"))
            recipeDescriptionQuery(subEntry)
            entry = str(input("Press any key to go back."))
        if mainEntry == 2:
            subEntry = str(input("Provide a tag:"))
            tagTitleCookingTimeQuery(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 3:
            subEntry = str(input("Provide the recipe name:"))
            titleRecipeIngredientsQuery(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 4:
            subEntry = str(input("Provide a username:"))
            userRecipeQuery(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 5:
            userCountRecipeQuery()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 6:
            createViewQuery()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 7:
            everythingFromViewQuery()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 8:
            subEntry = str(input("Provide the cooking time:"))
            nameTitleCookingTimeFromViewQuery(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 9:
            ingredientNameCountInRecipes()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 10:
            tagNameCountInRecipes()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 11:
            averageCookingTime()
            entry = str(input("Press any key to go back."))
