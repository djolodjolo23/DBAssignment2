
from array import array
import mysql.connector;
from mysql.connector import errorcode
import PySimpleGUI as sg

# connection details
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    #database = "Dimitrov"
    )
#
mycursor = db.cursor()

DB_NAME = "assignment3"

mycursor.execute("USE {}".format(DB_NAME))
print("========================================================================")
print("Sucessfuly connected to {} database".format(DB_NAME))
print("-----------------------------------")

recipeDetailsArray = []

sqlQuery = "SELECT RECIPE_ID, COOKING_TIME, TITLE FROM rm_recipe"
mycursor.execute(sqlQuery)
print(mycursor)
for row in mycursor:
    recipeDetailsArray.append(row)

print(recipeDetailsArray)
#mycursor.execute("SELECT * FROM recipe_ingredient")
#for row in mycursor:
    #print(row)

headings = ['blaab ', 'bjsjs', 'shghg']





layout = [
        [sg.Table(values=recipeDetailsArray,
        headings=headings,
        max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=10,
                        key='-TABLE-',
                        row_height=35)]
]


sg.Window('something', layout).read()