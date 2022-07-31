
import mysql.connector;
from mysql.connector import errorcode

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

# EVERYTHING FROM RECIPE
def query1():
    query = "SELECT * FROM rm_recipe"
    mycursor.execute(query)
    for row in mycursor:
        print (row)

# TAGS WITH RECIPE TITLE AND COOKING TIME
def query2():
    query = "SELECT rm_tags.TAG_NAME, TITLE, COOKING_TIME FROM rm_recipe JOIN rm_recipe_tags on rm_recipe_tags.RECIPE_ID = rm_recipe.RECIPE_ID JOIN rm_tags on rm_recipe_tags.TAGS_ID = rm_tags.TAGS_ID WHERE rm_tags.TAG_NAME = 'Pasta'"
    mycursor.execute(query)
    for row in mycursor:
        print (row)

# INGREDIENT NAMES FOR A GIVEN RECIPE
def query3():
    query = "SELECT NAME from rm_ingredient JOIN recipe_ingredient on rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID JOIN rm_recipe on recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID WHERE rm_recipe.RECIPE_NAME = 'Carbonara'"
    mycursor.execute(query)
    for row in mycursor:
        print (row)

