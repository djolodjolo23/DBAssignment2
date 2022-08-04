from black import main
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
        introText()
    except mysql.connector.Error as err:
        print("Database {} does not exist".format(DB_NAME))
        break
    while incrementNumber > 0:
        mainEntry = int(input("Provide a number:"))
        print("-> KEY " + str(mainEntry) + " PRESSED <-")
        print("Executing...")
        print("------------")
        if mainEntry == 1:
            subEntry = str(input("Provide a tag:"))
            query2(subEntry)
        elif mainEntry == 2:
            subEntry = str(input("Provide the recipe name:"))
            query3(subEntry)
        elif mainEntry == 3:
            subEntry = str(input("Provide a username:"))
            query4(subEntry)
        elif mainEntry == 4:
            query5()
        elif mainEntry == 5:
            query6()
        elif mainEntry == 6:
            query7()
        elif mainEntry == 7:
            subEntry = int(input("Provide the cooking time:"))
            query8()
