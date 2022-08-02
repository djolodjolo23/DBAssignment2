
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
    query = """
            SELECT NAME from rm_ingredient 
            JOIN recipe_ingredient on rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID 
            JOIN rm_recipe on recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID 
            WHERE rm_recipe.TITLE = 'Carbonara'
            """
    mycursor.execute(query)
    for row in mycursor:
        print (row)

def query4():
    query = """
            SELECT NAME, rm_recipe.TITLE, rm_recipe.DESCRIPTION
            FROM rm_useracc
            JOIN rm_recipe ON rm_useracc.USERACC_ID = rm_recipe.USERACC_ID
            WHERE rm_useracc.NAME = 'Djordje'
            """
    mycursor.execute(query)
    for row in mycursor:
        print (row)

def query5():
    query = """
            SELECT rm_useracc.NAME, COUNT(TITLE) FROM rm_recipe
            JOIN rm_useracc on rm_recipe.USERACC_ID = rm_useracc.USERACC_ID
            GROUP BY rm_useracc.NAME
            """
    mycursor.execute(query)
    for row in mycursor:
        print (row)

#getting the recipe title with all the ingredients concatenated
def query6():
    query = """
            CREATE VIEW Recipe_View AS
            SELECT rm_useracc.NAME, rm_recipe.RECIPE_ID, rm_recipe.TITLE, rm_recipe.COOKING_TIME, rm_recipe.DESCRIPTION
            FROM rm_useracc, rm_recipe
            WHERE rm_useracc.USERACC_ID = rm_recipe.USERACC_ID
            ORDER BY rm_useracc.NAME
            """
    mycursor.execute(query)
    for row in mycursor:
        print (row)
# selecting everything from Recipe_View
def query7():
    query = """
            SELECT * FROM Recipe_View
            """
    mycursor.execute(query)
    for row in mycursor:
        print (row)

query7()