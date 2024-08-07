import datetime
from gc import callbacks
from random import Random, random
from tkinter import EXCEPTION
from typing import Self
from unittest import result
import psycopg2
from psycopg2.sql import NULL
from dotenv import load_dotenv
import os
import sys
from tkinter import messagebox

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

def failed_connection() :
    messagebox.showerror("Error", "Failed to connect to database.")
    sys.exit()

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

if(conn == NULL) :
    failed_connection()
    

cur = conn.cursor()

# def set_error_callback(callback) :
#     global error_callback
#     error_callback = callback


def get_latest_entry_date() :
    execute_statement("SELECT entry_date FROM user_entries WHERE username = 'codyc' ORDER BY entry_date DESC LIMIT 1")
    rows = cur.fetchall()

    result_strings = []
    
    for row in rows:
        result_strings.append(row[0])

    return result_strings



def get_reminders(attribute,table) : 
    execute_statement(f"SELECT {attribute} FROM {table} WHERE username = 'codyc'")
    rows = cur.fetchall()

    result_strings = []
    
    for row in rows:
        result_strings.append(row[0])

    return result_strings

def get_entries(attribute,table) : 
    execute_statement(f"SELECT {attribute} FROM {table} WHERE username = 'codyc' ORDER BY entry_date DESC" )
    rows = cur.fetchall()

    result_strings = []
    for row in rows:
        result_strings.append(row[0])

    return result_strings

def add_user() :
    execute_statement(f"INSERT INTO users_table (name) VALUES ('Test User')")

def remove_user() :
    execute_statement(f"DELETE FROM users_table WHERE name = 'Test User'")

def add_entry(mood,energy_level,sleep_duration,sleep_quality, physical_symptoms, social_interaction,physical_activity) :
    execute_statement(f"INSERT INTO user_entries (mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity, username) VALUES ({mood}, {energy_level}, '{sleep_duration} hours', {sleep_quality}, {physical_symptoms}, '{social_interaction} hours', '{physical_activity} hours', 'codyc')")
    conn.commit()
    
def add_accomplishment(accomplishment) :
    execute_statement(f"INSERT INTO accomplishments_new (accomplishment,username) VALUES ('{accomplishment}', 'codyc')")

def remove_accomplishment(accomplishment) :
    execute_statement(f"DELETE FROM accomplishments_new WHERE accomplishment = '{accomplishment}' AND username = 'codyc'")
    
def add_coping_strategy(coping_strategy) :
    execute_statement(f"INSERT INTO coping_strategies_new (coping_strategy, username) VALUES ('{coping_strategy}', 'codyc')")

def remove_coping_strategy(coping_strategy) :
    execute_statement(f"DELETE FROM coping_strategies_new WHERE coping_strategy = '{coping_strategy}' AND username = 'codyc'")
    
def add_goal(goal) :
    execute_statement(f"INSERT INTO goals_new (goal, username) VALUES ('{goal}','codyc')")

def remove_goal(goal) :
    execute_statement(f"DELETE FROM goals_new WHERE goal = '{goal}' AND username = 'codyc'")

def add_gratitude(gratitude) :
    execute_statement(f"INSERT INTO gratitudes_new (gratitude,username) VALUES ('{gratitude}', 'codyc')")

def remove_gratitude(gratitude) :
    execute_statement(f"DELETE FROM gratitudes_new WHERE gratitude = '{gratitude}' AND username = 'codyc'")

def add_reflection(reflection) :
    execute_statement(f"INSERT INTO reflections_new (reflection,username) VALUES ('{reflection}', 'codyc')")

def remove_reflection(reflection) :
    execute_statement(f"DELETE FROM reflections_new WHERE reflection = '{reflection}' AND username = 'codyc'")

def add_self_care_activity(self_care_activity) :
    execute_statement(f"INSERT INTO self_care_activities_new (self_care_activity, username) VALUES ('{self_care_activity}','codyc')")

def remove_self_care_activity(self_care_activity) :
    execute_statement(f"DELETE FROM self_care_activities_new WHERE self_care_activity = '{self_care_activity}' AND username = 'codyc'")

# def add_stressor() :
#     execute_statement(f"INSERT INTO stressors (id, stressor) VALUES (1, 'Love')")

# def remove_stressor() :
#     execute_statement(f"DELETE FROM stressors WHERE stressor = 'Love'")

def get_avg(category) :
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
        
        if category == 0:  # Assuming category 0 represents mood
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

    # return f"{ten_day_average}\n{thirty_day_average}\n{ninety_day_average}"
    return [ten_day_average,thirty_day_average,ninety_day_average]        

def get_cmp(category, ten_day_average, thirty_day_average, ninety_day_average) :    
    days = [10,30,90]
    
    def comparison(most_recent, days, previous_avg) :
        comp = most_recent / previous_avg 
        # Assuming you have today's value and average value calculated
        today_value = most_recent # Replace with your actual value for today's entry
        average_value = previous_avg  # Replace with your actual average value over the past ninety days
        
        if isinstance(today_value, datetime.timedelta):
            today_value = today_value.total_seconds() / 3600
            
        # Calculate percent change
        percent_change = ((today_value - average_value) / average_value) * 100

        # Display the result
        return percent_change
    
    for i in range(len(days)) :  
        value = 0
        
        if category == 0:  # Assuming category 0 represents mood
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
            value = row[0]  # Assuming each query returns exactly one value
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

# Close the database connection
    conn.close()
        
def test() : 
     print( "hello")
    

def execute_statement(statement) :
    try :
        cur.execute(statement)
    except Exception :
        if not error_callback == 0 :
            error_callback()
        




# conn.commit()

# cur.close()
# conn.close()

