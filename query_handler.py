
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

# schema
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
    newString = "%" + tagInput + "%"
    query = "SELECT rm_tags.TAG_NAME, TITLE, COOKING_TIME FROM rm_recipe JOIN rm_recipe_tags on rm_recipe_tags.RECIPE_ID = rm_recipe.RECIPE_ID JOIN rm_tags on rm_recipe_tags.TAGS_ID = rm_tags.TAGS_ID WHERE rm_tags.TAG_NAME LIKE '" + newString + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['TAG', 'RECIPE NAME', 'COOKING TIME'], tablefmt='psql'))

# INGREDIENT NAMES FOR A GIVEN RECIPE
def titleRecipeIngredientsQuery(recipeNameInput):
    # assist query to print the entire recipe name from a wildcard LIKE
    assistTitleQuery(recipeNameInput)
    newString = "%" + recipeNameInput + "%"
    query = "SELECT NAME, recipe_ingredient.INGREDIENT_DESC FROM rm_ingredient JOIN recipe_ingredient on rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID JOIN rm_recipe on recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID WHERE rm_recipe.TITLE LIKE'" + newString + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['INGREDIENT NAME', "INGREDIENT DETAILS"], tablefmt='psql'))

# user and recipe title associated with the user
def userRecipeQuery(userInput):
    newString = "%" + userInput + "%"
    query = "SELECT NAME, rm_recipe.TITLE FROM rm_useracc JOIN rm_recipe ON rm_useracc.USERACC_ID = rm_recipe.USERACC_ID WHERE rm_useracc.NAME LIKE '" + newString + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['USER', 'RECIPE NAME'], tablefmt='psql'))

#show all users and the amount of recipes they are associated with
def userCountRecipeQuery():
    query = """
            SELECT rm_useracc.NAME, COUNT(TITLE) FROM rm_recipe
            JOIN rm_useracc on rm_recipe.USERACC_ID = rm_useracc.USERACC_ID
            GROUP BY rm_useracc.NAME
            """
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['USER', 'NUMBER OF RECIPES'], tablefmt='psql'))

#show ingredient names and count of recipes
def ingredientNameCountInRecipes():
    query = "SELECT rm_ingredient.NAME, COUNT(rm_recipe.RECIPE_ID) FROM rm_ingredient JOIN recipe_ingredient ON rm_ingredient.INGREDIENT_ID = recipe_ingredient.INGREDIENT_ID JOIN rm_recipe ON recipe_ingredient.RECIPE_ID = rm_recipe.RECIPE_ID GROUP BY rm_ingredient.NAME ORDER BY COUNT(rm_recipe.RECIPE_ID) DESC"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['INGREDIENT', 'NUMBER OF RECIPES IT APPEARS'], tablefmt='psql'))

# show tags and the recipes connected to it
def tagNameCountInRecipes():
    query = "SELECT rm_tags.TAG_NAME, COUNT(rm_recipe.RECIPE_ID) FROM rm_tags JOIN rm_recipe_tags on rm_tags.TAGS_ID = rm_recipe_tags.TAGS_ID JOIN rm_recipe on rm_recipe_tags.RECIPE_ID = rm_recipe.RECIPE_ID group by rm_tags.TAG_NAME"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['TAGS', 'NUMBER OF RECIPES ASSOCIATED WITH'], tablefmt='psql'))

# show average cooking time
def averageCookingTime():
    query = "SELECT ROUND(AVG(rm_recipe.COOKING_TIME)) AS 'COOKING TIME' FROM rm_recipe"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['AVERAGE COOKING TIME'], tablefmt='psql'))

#creating the View
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

# getting the name, title, cooking_time from a View where recipe time is less then the input
def nameTitleCookingTimeFromViewQuery(timeInput):
    query = "SELECT NAME, TITLE, COOKING_TIME FROM the_view WHERE COOKING_TIME <= '" + timeInput + "'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['NAME', 'TITLE', 'COOKING TIME'], tablefmt='psql'))

# only recipe titles, for homepage with all the recipes
def recipeTitlesQuery():
    query = """
            SELECT TITLE FROM rm_recipe
            ORDER BY TITLE
            """
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['RECIPE DATABASE'], tablefmt='psql'))

# gives a recipe description 
def recipeDescriptionQuery(titleInput):
    # assist query to print the entire recipe name from a wildcard LIKE
    assistTitleQuery2(titleInput)
    newString = "%" + titleInput + "%"
    query = "SELECT DESCRIPTION from rm_recipe WHERE TITLE LIKE '" + newString + "'"
    mycursor.execute(query)
    for row in mycursor:
        tupleWithoutComma = "".join(row)
        print(tupleWithoutComma)

#prints the recipe name with "ingredients below"
def assistTitleQuery(titleInput):
    newString = "%" + titleInput + "%"
    query = "SELECT TITLE FROM rm_recipe WHERE TITLE LIKE '" + newString + "'"
    mycursor.execute(query)
    for row in mycursor:
        tupleWithoutComma = "".join(row)
        print(tupleWithoutComma + " ingredients below.")

#prints the recipe name with "recipe below"
def assistTitleQuery2(titleInput):
    newString = "%" + titleInput + "%"
    query = "SELECT TITLE FROM rm_recipe WHERE TITLE LIKE '" + newString + "'"
    mycursor.execute(query)
    for row in mycursor:
        tupleWithoutComma = "".join(row)
        print(tupleWithoutComma + " recipe below.")
    
    
#intro text to be called each time the main menu is up
def introText():
    print("")
    print("                           RECIPE FINDER!                               ")
    print("------------------------------------------------------------------------")
    #prints the recipe names in the main menu
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
    print("9. Show ingredients and the amount of recipes they appear in.")
    print("10. Show tags and the amount of recipes they are associated with.")
    print("11. Show the average cooking time for all the recipes.")


mycursor.close()
db.close()