from query_handler import *

print("THE RECIPE FINDER!")
print("------------------")

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
            query10(subEntry)
            entry = str(input("Press any key to go back."))
        if mainEntry == 2:
            subEntry = str(input("Provide a tag:"))
            query2(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 3:
            subEntry = str(input("Provide the recipe name:"))
            query3(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 4:
            subEntry = str(input("Provide a username:"))
            query4(subEntry)
            entry = str(input("Press any key to go back."))
        elif mainEntry == 5:
            query5()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 6:
            query6()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 7:
            query7()
            entry = str(input("Press any key to go back."))
        elif mainEntry == 8:
            subEntry = str(input("Provide the cooking time:"))
            query8(subEntry)
            entry = str(input("Press any key to go back."))
