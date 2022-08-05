
import mysql.connector;
from mysql.connector import errorcode
from tabulate import tabulate

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
def tagTitleCookingTimeQuery(tagInput):
    query = "SELECT rm_tags.TAG_NAME, TITLE, COOKING_TIME FROM rm_recipe JOIN rm_recipe_tags on rm_recipe_tags.RECIPE_ID = rm_recipe.RECIPE_ID JOIN rm_tags on rm_recipe_tags.TAGS_ID = rm_tags.TAGS_ID WHERE rm_tags.TAG_NAME = '" + tagInput + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['TAG', 'RECIPE NAME', 'COOKING TIME'], tablefmt='psql'))

# INGREDIENT NAMES FOR A GIVEN RECIPE
def titleRecipeIngredientsQuery(recipeNameInput):
    assistTitleQuery(recipeNameInput)
    newString = "%" + recipeNameInput + "%"
    query = "SELECT NAME, recipe_ingredient.INGREDIENT_DESC FROM rm_ingredient JOIN recipe_ingredient on rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID JOIN rm_recipe on recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID WHERE rm_recipe.TITLE LIKE'" + newString + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['INGREDIENT NAME', "INGREDIENT DETAILS"], tablefmt='psql'))

def userRecipeQuery(userInput):
    query = "SELECT NAME, rm_recipe.TITLE FROM rm_useracc JOIN rm_recipe ON rm_useracc.USERACC_ID = rm_recipe.USERACC_ID WHERE rm_useracc.NAME = '" + userInput + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['USER', 'RECIPE NAME'], tablefmt='psql'))

def userCountRecipeQuery():
    query = """
            SELECT rm_useracc.NAME, COUNT(TITLE) FROM rm_recipe
            JOIN rm_useracc on rm_recipe.USERACC_ID = rm_useracc.USERACC_ID
            GROUP BY rm_useracc.NAME
            """
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['USER', 'NUMBER OF RECIPES'], tablefmt='psql'))

#getting the recipe title with all the ingredients concatenated
def createViewQuery():
    query = """
            CREATE VIEW the_view AS
            SELECT rm_useracc.NAME, rm_recipe.RECIPE_ID, rm_recipe.TITLE, rm_recipe.COOKING_TIME
            FROM rm_useracc, rm_recipe
            WHERE rm_useracc.USERACC_ID = rm_recipe.USERACC_ID
            ORDER BY rm_useracc.NAME
            """
    mycursor.execute(query)
    print("Success!")

# selecting everything from Recipe_View
def everythingFromViewQuery():
    query = """
            SELECT * FROM the_view
            """
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['USER', 'RECIPE_ID', 'RECIPE NAME', 'COOKING TIME'], tablefmt='psql'))


def nameTitleCookingTimeFromViewQuery(timeInput):
    query = "SELECT NAME, TITLE, COOKING_TIME FROM Recipe_View WHERE COOKING_TIME <= '" + timeInput + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['NAME', 'TITLE', 'COOKING TIME'], tablefmt='psql'))

def recipeTitlesQuery():
    query = """
            SELECT TITLE FROM rm_recipe
            """
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['RECIPE DATABASE'], tablefmt='psql'))

# gives a recipe description 
def recipeDescriptionQuery(titleInput):
    query = "SELECT DESCRIPTION from rm_recipe WHERE TITLE = '" + titleInput + "'"
    mycursor.execute(query)
    print(titleInput + " recipe below.")
    print("------------------------------------------------------------------------")
    for row in mycursor:
        print(row)

def assistTitleQuery(titleInput):
    newString = "%" + titleInput + "%"
    query = "SELECT TITLE FROM rm_recipe WHERE TITLE LIKE '" + newString + "'"
    mycursor.execute(query)
    for row in mycursor:
        tupleWithoutComma = "".join(row)
        print(tupleWithoutComma + " ingredients below.")
    
    
    

def introText():
    print("")
    print("                           RECIPE FINDER!")
    print("------------------------------------------------------------------------")
    recipeTitlesQuery()
    print("------------------------------------------------------------------------")
    print("1. Provide the recipe name and show the full description.")
    print("2. Provide a recipe tag to find it.")
    print("3. Type the recipe name to see the details.")
    print("4. Provide a username to see all the recipes associated with it.")
    print("5. Check all the usernames and how many recipes are associated with it.")
    print("6. Create a View with recipe owner, recipe ID, recipe Title, cooking time.")
    print("7. Show everything from the View created.")
    print("8. Show recipe details with less then provided cooking time.")
titleRecipeIngredientsQuery("wok")