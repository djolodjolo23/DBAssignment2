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