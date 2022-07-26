# Importing Packages
import sqlite3
import pandas as pd

# Creating DB using SQLiteJDBC driver
db = sqlite3.connect('../DB/interesting_movies.db')

# DB Cursor
cursor = db.cursor()

# Creating Tables
# cursor.execute('''CREATE TABLE movies(id INTEGER PRIMARY KEY, Movie_Name TEXT, Lead_Actor TEXT, Lead_Actress TEXT, Director_Name TEXT, Year_Of_Release YEAR)''')
# Inserting Data into tables
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(1,"Vikram Vedha","Vijay Sethupathi","Shraddha Srinath","Pushkar",2017)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(2,"Thalapathi","Rajinikanth","Shobana","Mani Ratnam",1991)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(3,"Jai Bhim","Suriya","Lijomol Jose","TJ Gnanavel",2021)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(4,"Rocketry","R. Madhavan","Simran","R. Madhavan",2022)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(5,"Karnan","Dhanush","Rajisha Vijayan","Mari Selvaraj",2021)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(6,"soorarai pottru","Suriya","Aparna Balamurali","Sudha Kongara Prasad",2020)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(7,"O Kadhal Kanmani","Dulquer Salmaan","Nithya Menen","Mani Ratnam",2015)''')
# SELECT statement to query all rows from the Movies table
sqlite_select_query = """SELECT * from movies"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("\n\n")
print("Total Database")
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
print("\n\n")
# SELECT query with parameter like actor name to select movies based on the actor's name
sqlite_select_query = """SELECT * from movies where Lead_Actor = 'Suriya'"""
cursor.execute(sqlite_select_query)
records_select = cursor.fetchall()
print("Actor Name Customized")
print(pd.DataFrame(records_select,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
print("\n\n")
# SELECT query with parameter like director name to select movies based on the directors's name
sqlite_select_query = """SELECT * from movies where Director_Name = 'Mani Ratnam'"""
cursor.execute(sqlite_select_query)
records_select = cursor.fetchall()
print("Director Name Customized")
print(pd.DataFrame(records_select,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
# User Customization
print("Enter 0 exit")
print("Enter 1 to insert new movie details")
print("Enter 2 to view movie details with your custom query")
while True:
    inp = int(input("Enter your choice: "))
    if inp == 0:
        break
    elif inp == 1:
        movie_name = input("Enter the movie name: ")
        lead_actor = input("Enter the lead actor: ")
        lead_actress = input("Enter the lead actress: ")
        director_name = input("Enter the director name: ")
        year_of_release = int(input("Enter the year of release: "))
        cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(?,?,?,?,?,?)''',(len(records)+1,movie_name,lead_actor,lead_actress,director_name,year_of_release))
        db.commit()
        print("Movie details inserted successfully")
    elif inp == 2:
        print("Enter the query")
        query = input()
        cursor.execute(query)
        records = cursor.fetchall()
        print(pd.DataFrame(records_select,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
