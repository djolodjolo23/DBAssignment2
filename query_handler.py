
import mysql.connector;
from mysql.connector import errorcode
import numpy as np
from tkinter import *
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

def query1():
    mycursor.execute("SELECT * FROM rm_recipe")
    i = 0
    for recipe in mycursor:
        for j in range(len(recipe)):
            e = Entry(root, width=50, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, recipe[j])
        i+=1


root = Tk()

root.title=('Recipe finder!')
root.geometry("800x800")

mycursor.execute("SELECT * FROM rm_recipe")
i = 0
for recipe in mycursor:
    for j in range(len(recipe)):
        e = Entry(root, width=50, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, recipe[j])
    i+=1

root.mainloop()


