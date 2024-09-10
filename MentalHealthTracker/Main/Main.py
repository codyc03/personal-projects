""" 
File:      Main.py 
Author:    Cody Christensen 
Date:      9/10/24 
Copyright: Cody Christensen - This work may not be copied for use in Academic Coursework. 
  
I, Cody Christensen, certify that I wrote this code  
from scratch and did not copy it in part or whole from another source. 
All references used in the completion of the assignments are cited  
in my README file. 

File Contents 
    This file contains the code for the database 
    access portion of the project. It is used as a
    file to hold functions to fetch important data
    for my other GUI file, MainPageGUI.
"""

import datetime
import psycopg2
from psycopg2.sql import NULL
from dotenv import load_dotenv
import os
import sys
from tkinter import messagebox

def failed_connection() :
     """
       Handles case of a failed connection to database.
     """
     
     messagebox.showerror("Error", "Failed to connect to database.")
     sys.exit()

def get_latest_entry_date() :
    """
    Retrieves the date representing the most recent entry in user entries.
    """
    execute_statement("SELECT entry_date FROM user_entries WHERE username = 'codyc' ORDER BY entry_date DESC LIMIT 1")
    rows = cur.fetchall()

    result_strings = []
    
    for row in rows:
        result_strings.append(row[0])

    return result_strings

def get_reminders(attribute,table) : 
    """
    Helper method used to fetch different reminders from the database.
    """
    execute_statement(f"SELECT {attribute} FROM {table} WHERE username = 'codyc'")
    rows = cur.fetchall()

    result_strings = []
    
    for row in rows:
        result_strings.append(row[0])

    return result_strings

def get_entries(attribute,table) : 
    """
    Helper method to get specificed entries from specified table.
    """
    execute_statement(f"SELECT {attribute} FROM {table} WHERE username = 'codyc' ORDER BY entry_date DESC" )
    rows = cur.fetchall()

    result_strings = []
    
    for row in rows:
        result_strings.append(row[0])

    return result_strings

def add_user() :
    """
    Test method used to add a user to the user entries table.
    """
    execute_statement(f"INSERT INTO users_table (name) VALUES ('Test User')")

def remove_user() :
    """
    Test method used to remove a user from the user entries table.
    """
    execute_statement(f"DELETE FROM users_table WHERE name = 'Test User'")

def add_entry(mood,energy_level,sleep_duration,sleep_quality, physical_symptoms, social_interaction,physical_activity) :
    """
    Add an entry into the user entries table.
    """
    execute_statement(f"INSERT INTO user_entries (mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity, username) VALUES ({mood}, {energy_level}, '{sleep_duration} hours', {sleep_quality}, {physical_symptoms}, '{social_interaction} hours', '{physical_activity} hours', 'codyc')")
    
def add_accomplishment(accomplishment) :
    """
    Add an accomplishment to the accopmlishments table.
    """
    execute_statement(f"INSERT INTO accomplishments_new (accomplishment,username) VALUES ('{accomplishment}', 'codyc')")

def remove_accomplishment(accomplishment) :
    """
    Remove an accomplishment from the accopmlishments table.
    """
    execute_statement(f"DELETE FROM accomplishments_new WHERE accomplishment = '{accomplishment}' AND username = 'codyc'")
    
def add_coping_strategy(coping_strategy) :
    """
    Add a coping strategy to the coping strategies table.
    """
    execute_statement(f"INSERT INTO coping_strategies_new (coping_strategy, username) VALUES ('{coping_strategy}', 'codyc')")

def remove_coping_strategy(coping_strategy) :
    """
    Remove a coping strategy from the coping strategies table.
    """
    execute_statement(f"DELETE FROM coping_strategies_new WHERE coping_strategy = '{coping_strategy}' AND username = 'codyc'")
    
def add_goal(goal) :
    """
    Add a goal to the goals table.
    """
    execute_statement(f"INSERT INTO goals_new (goal, username) VALUES ('{goal}','codyc')")

def remove_goal(goal) :
    """
    Remove a goal from the goals table.
    """
    execute_statement(f"DELETE FROM goals_new WHERE goal = '{goal}' AND username = 'codyc'")

def add_gratitude(gratitude) :
    """
    Add a gratitude to the gratitudes table.
    """
    execute_statement(f"INSERT INTO gratitudes_new (gratitude,username) VALUES ('{gratitude}', 'codyc')")

def remove_gratitude(gratitude) :
    """
    Remove a gratitude from the gratitudes table.
    """
    execute_statement(f"DELETE FROM gratitudes_new WHERE gratitude = '{gratitude}' AND username = 'codyc'")

def add_reflection(reflection) :
    """
    Add a reflection to the reflections table.
    """
    execute_statement(f"INSERT INTO reflections_new (reflection,username) VALUES ('{reflection}', 'codyc')")

def remove_reflection(reflection) :
    """
    Remove a reflection from the reflections table.
    """
    execute_statement(f"DELETE FROM reflections_new WHERE reflection = '{reflection}' AND username = 'codyc'")

def add_self_care_activity(self_care_activity) :
    """
    Add a self care activity to the self care activities table.
    """
    execute_statement(f"INSERT INTO self_care_activities_new (self_care_activity, username) VALUES ('{self_care_activity}','codyc')")

def remove_self_care_activity(self_care_activity) :
    """
    Remove a self care activity from the self care activities table.
    """
    execute_statement(f"DELETE FROM self_care_activities_new WHERE self_care_activity = '{self_care_activity}' AND username = 'codyc'")

def get_avg(category) :
    """
    Returns an array with the 10 day, 30 day, and 90 day average of the specified category.
    """
    days = [10,30,90]
    ten_day_average = 0
    thirty_day_average = 0
    ninety_day_average = 0
    
    def fetch_helper (rows) :
        total = 0

        num_entries = len(rows)
            
        for entry in rows[:min(days[i], len(rows))]:
            if isinstance(entry[0], (int, float)):  # Check if entry[0] is an integer or float
                total += entry[0]
            elif isinstance(entry[0], datetime.timedelta):
                total += entry[0].total_seconds() / 3600
                
        return total
                
    for i in range(len(days)) :  
        total = 0
        
        if category == 0:  
            execute_statement(f"SELECT mood FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)
         
        if category == 1 :
            execute_statement(f"SELECT energy_level FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)

        if category == 2 :
            execute_statement(f"SELECT sleep_duration FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)
            
        if category == 3 :
            execute_statement(f"SELECT sleep_quality FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)
            
        if category == 4 :
            execute_statement(f"SELECT physical_symptoms FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)
            
        if category == 5 :
            execute_statement(f"SELECT social_interaction FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)

        if category == 6 :
            execute_statement(f"SELECT physical_activity FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = fetch_helper(rows)
        
        avg = total / min(days[i], len(rows))
        
        if i == 0 :
            ten_day_average = avg
        elif i == 1 :
            thirty_day_average = avg
        elif i == 2 : 
            ninety_day_average = avg

    return [ten_day_average,thirty_day_average,ninety_day_average]        

def get_cmp(category, ten_day_average, thirty_day_average, ninety_day_average) :    
    """
    Returns an array with the 10 day, 30 day, and 90 day comparison to average of the specified category.
    """
    
    days = [10,30,90]
    
    def comparison(most_recent, days, previous_avg) :
        comp = most_recent / previous_avg 
        today_value = most_recent 
        average_value = previous_avg  
        
        if isinstance(today_value, datetime.timedelta):
            today_value = today_value.total_seconds() / 3600
            
        # Calculate percent change
        percent_change = ((today_value - average_value) / average_value) * 100

        # Display the result
        return percent_change
    
    for i in range(len(days)) :  
        value = 0
        
        if category == 0: 
            execute_statement("SELECT mood FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 1:
            execute_statement("SELECT energy_level FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 2:
            execute_statement("SELECT sleep_duration FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 3:
            execute_statement("SELECT sleep_quality FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 4:
            execute_statement("SELECT physical_symptoms FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 5:
            execute_statement("SELECT social_interaction FROM user_entries ORDER BY entry_date DESC LIMIT 1")
        elif category == 6:
            execute_statement("SELECT physical_activity FROM user_entries ORDER BY entry_date DESC LIMIT 1")

        row = cur.fetchone()
        
        if row:
            value = row[0]  
        else:
            value = 0
     
        if i == 0 :
            ten_day_comparison = comparison(value,days[i],ten_day_average)
        elif i == 1 :
            thirty_day_comparison = comparison(value,days[i],thirty_day_average)
        elif i == 2 : 
            ninety_day_comparison = comparison(value,days[i],ninety_day_average)

    return [ten_day_comparison,thirty_day_comparison,ninety_day_comparison]

def feed_values():
    """
    Method used during testing to feed values into the user entries table, all with different timestamps.
    """
    for i in range(100):
        # Generate a date for each iteration, starting from today and decrementing by 'i' days
        entry_date = datetime.date.today() - datetime.timedelta(days=i)
    
        rand = i % 10
        
        # SQL query with embedded parameter using string formatting
        sql = f"""
            INSERT INTO user_entries (entry_date, mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity, username)
            VALUES ('{entry_date}', {rand}, {rand}, '{rand} hours', {rand}, {rand}, '{rand} hours', '{rand} hours', 'codyc')
        """
    
        # Execute the SQL query with dynamically generated date
        execute_statement(sql)
        
def execute_statement(statement) :
    """
    Method used to execute any generic SQL statement using the cursor.
    """
    try :
        cur.execute(statement)
    except Exception :
        if not error_callback == 0 :
            error_callback()
        
#Start with defining as null
conn = NULL
cur = NULL
error_callback = 0

# Load environmental variables from .env file
load_dotenv(r"C:\Users\codyc\source\repos\personal-projects\MentalHealthTracker\Main\Test.env")

# Access environmental variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("USER_NAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("HOST_NAME")

# Try to connect to database
try :
    conn = psycopg2.connect(
                                    dbname = db_name,
                                    user = db_user,
                                    password = db_password,
                                    host = db_host
                            )
    conn.autocommit = True
except Exception as e:
    failed_connection()

# Extra checking to make sure connection was succesful and assigned
if(conn == NULL) :
    failed_connection()
    
# Declare cursor
cur = conn.cursor()

