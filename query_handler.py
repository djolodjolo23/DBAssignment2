
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
print("========================================================================")

# EVERYTHING FROM RECIPE
def query1():
    query = "SELECT * FROM rm_recipe"
    mycursor.execute(query)
    for row in mycursor:
        print(row)

# TAGS WITH RECIPE TITLE AND COOKING TIME
def query2(tagInput):
    query = "SELECT rm_tags.TAG_NAME, TITLE, COOKING_TIME FROM rm_recipe JOIN rm_recipe_tags on rm_recipe_tags.RECIPE_ID = rm_recipe.RECIPE_ID JOIN rm_tags on rm_recipe_tags.TAGS_ID = rm_tags.TAGS_ID WHERE rm_tags.TAG_NAME = '" + tagInput + "'"
    mycursor.execute(query)
    for row in mycursor:
        print(row)

# INGREDIENT NAMES FOR A GIVEN RECIPE
def query3(recipeNameInput):
    query = "SELECT NAME from rm_ingredient JOIN recipe_ingredient on rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID JOIN rm_recipe on recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID WHERE rm_recipe.TITLE = '" + recipeNameInput + "'"
    mycursor.execute(query)
    for row in mycursor:
        print(row)

def query4():
    query = """
            SELECT NAME, rm_recipe.TITLE, rm_recipe.DESCRIPTION
            FROM rm_useracc
            JOIN rm_recipe ON rm_useracc.USERACC_ID = rm_recipe.USERACC_ID
            WHERE rm_useracc.NAME = 'Djordje'
            """
    mycursor.execute(query)
    for row in mycursor:
        print(row)

def query5():
    query = """
            SELECT rm_useracc.NAME, COUNT(TITLE) FROM rm_recipe
            JOIN rm_useracc on rm_recipe.USERACC_ID = rm_useracc.USERACC_ID
            GROUP BY rm_useracc.NAME
            """
    mycursor.execute(query)
    for row in mycursor:
        print(row)

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
        print(row)


def query8(timeInput):
    query = "SELECT NAME, TITLE, COOKING_TIME FROM Recipe_View WHERE COOKING_TIME <= '" + timeInput + "'"
    mycursor.execute(query)
    for row in mycursor:
        print(row)

def query9():
    query = """
            SELECT TITLE FROM rm_recipe
            """
    mycursor.execute(query)
    for row in mycursor:
        tupleWithoutComma = ''.join(row)
        print("{:<15}".format(tupleWithoutComma))

def introText():
    print("")
    print("                           RECIPE FINDER!")
    print("------------------------------------------------------------------------")
    query9()
    print("------------------------------------------------------------------------")
    print("1. Provide a recipe tag to find it.")
    print("2. Type the recipe name to see the details.")
    print("3. Provide a username to see all the recipes associated with it.")
    print("4. Check all the usernames and how many recipes are associated with it.")
    print("5. Create a View with recipe owner, recipe ID, recipe Title, cooking time and description.")
    print("6. Show everything from the View created.")
    print("7. Show recipe details with less then provided cooking time.")