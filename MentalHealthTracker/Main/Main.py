import psycopg2
from psycopg2.sql import NULL
from dotenv import load_dotenv
import os

# Load environmental variables from .env file
load_dotenv()

# Access environmental variables
DB_NAME = os.getenv("DB_NAME")
db_user = os.getenv("USER_NAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("HOST_NAME")

conn = NULL

try :
    conn = psycopg2.connect(
                                  dbname = DB_NAME,
                                  user = db_user,
                                  password = db_password,
                                  host = db_host
                           )
except Exception as e:
    raise NotImplementedError(e)

if(conn == NULL) :
    raise NotImplementedError()

cur = conn.cursor()
name = "Test User"

def add_user() :
    cur.execute(f"INSERT INTO users_table (name) VALUES ('{name}')")

def remove_user() :
    cur.execute(f"DELETE FROM users_table WHERE name = '{name}'")

def add_entry() :
    cur.execute(f"INSERT INTO user_entries (id, mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity) VALUES (1, 2, 3, '4 hours', 5, 6, '7 hours', '8 hours')")
        
def add_accomplishment() :
    cur.execute(f"INSERT INTO accomplishments (id, accomplishment) VALUES (1, 'Started loving myself')")

def remove_accomplishment() :
    cur.execute(f"DELETE FROM accomplishments WHERE accomplishment = 'Started loving myself'")
    
def add_coping_strategy() :
    cur.execute(f"INSERT INTO coping_strategies (id, coping_strategy) VALUES (1, 'Movies')")

def remove_coping_strategy() :
    cur.execute(f"DELETE FROM coping_strategies WHERE coping_strategy = 'Movies'")
    

# cur.execute() 

# cur.execute("""
#         CREATE TABLE IF NOT EXISTS goals (
#         id INTEGER PRIMARY KEY,
#         goal TEXT   
#         )
#             """) 

# activities TEXT,
# stressors TEXT,
# coping_strategies TEXT,
# self_care_activities TEXT,
# social_interaction TEXT,
# accomplishments TEXT,
# gratitude TEXT,
# reflections TEXT,
# goals TEXT,
# cur.execute("INSERT INTO users_table (id, name) VALUES (001, 'Cody Christensen')") 

conn.commit()

cur.close()
conn.close()

# print()
