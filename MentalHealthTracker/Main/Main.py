import psycopg2
from psycopg2.sql import NULL
from dotenv import load_dotenv
import os

conn = NULL
cur = NULL


# Load environmental variables from .env file
load_dotenv()

# Access environmental variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("USER_NAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("HOST_NAME")


try :
    conn = psycopg2.connect(
                                    dbname = db_name,
                                    user = db_user,
                                    password = db_password,
                                    host = db_host
                            )
except Exception as e:
    raise NotImplementedError(e)

if(conn == NULL) :
    raise NotImplementedError()

cur = conn.cursor()

def get_reminders(attribute,table) : 
    cur.execute(f"SELECT {attribute} FROM {table} WHERE username = 'codyc'")
    rows = cur.fetchall()

    result_strings = []
    for row in rows:
        result_strings.append(row[0])

    return result_strings


def add_user() :
    cur.execute(f"INSERT INTO users_table (name) VALUES ('Test User')")

def remove_user() :
    cur.execute(f"DELETE FROM users_table WHERE name = 'Test User'")

def add_entry(mood,energy_level,sleep_duration,sleep_quality, physical_symptoms, social_interaction,physical_activity) :
    cur.execute(f"INSERT INTO user_entries (mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity, username) VALUES ({mood}, {energy_level}, '{sleep_duration} hours', {sleep_quality}, {physical_symptoms}, '{social_interaction} hours', '{physical_activity} hours', 'codyc')")
    conn.commit()
    
def add_accomplishment() :
    cur.execute(f"INSERT INTO accomplishments (id, accomplishment) VALUES (1, 'Started loving myself')")

def remove_accomplishment() :
    cur.execute(f"DELETE FROM accomplishments WHERE accomplishment = 'Started loving myself'")
    
def add_coping_strategy() :
    cur.execute(f"INSERT INTO coping_strategies (id, coping_strategy) VALUES (1, 'Movies')")

def remove_coping_strategy() :
    cur.execute(f"DELETE FROM coping_strategies WHERE coping_strategy = 'Movies'")
    
def add_goal() :
    cur.execute(f"INSERT INTO goals (id, goal) VALUES (1, 'learn to code')")

def remove_goal() :
    cur.execute(f"DELETE FROM goals WHERE goal = 'learn to code'")

def add_gratitude() :
    cur.execute(f"INSERT INTO gratitudes (id, gratitude) VALUES (1, 'Relationships')")

def remove_gratitude() :
    cur.execute(f"DELETE FROM gratitudes WHERE gratitude = 'Relationships'")

def add_reflection() :
    cur.execute(f"INSERT INTO reflections (id, reflection) VALUES (1, 'Love')")

def remove_reflection() :
    cur.execute(f"DELETE FROM reflections WHERE reflection = 'Love'")

def add_self_care_activity() :
    cur.execute(f"INSERT INTO self_care_activities (id, self_care_activity) VALUES (1, 'Love')")

def remove_self_care_activity() :
    cur.execute(f"DELETE FROM self_care_activities WHERE self_care_activity = 'Love'")

def add_stressor() :
    cur.execute(f"INSERT INTO stressors (id, stressor) VALUES (1, 'Love')")

def remove_stressor() :
    cur.execute(f"DELETE FROM stressors WHERE stressor = 'Love'")

def test() : 
    print( "hello")

# conn.commit()

# cur.close()
# conn.close()

