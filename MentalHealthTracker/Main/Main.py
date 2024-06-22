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
    conn.autocommit = True
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
    
def add_accomplishment(accomplishment) :
    cur.execute(f"INSERT INTO accomplishments_new (accomplishment,username) VALUES ('{accomplishment}', 'codyc')")

def remove_accomplishment(accomplishment) :
    cur.execute(f"DELETE FROM accomplishments_new WHERE accomplishment = '{accomplishment}' AND username = 'codyc'")
    
def add_coping_strategy(coping_strategy) :
    cur.execute(f"INSERT INTO coping_strategies_new (coping_strategy, username) VALUES ('{coping_strategy}', 'codyc')")

def remove_coping_strategy(coping_strategy) :
    cur.execute(f"DELETE FROM coping_strategies_new WHERE coping_strategy = '{coping_strategy}' AND username = 'codyc'")
    
def add_goal(goal) :
    cur.execute(f"INSERT INTO goals_new (goal, username) VALUES ('{goal}','codyc')")

def remove_goal(goal) :
    cur.execute(f"DELETE FROM goals_new WHERE goal = '{goal}' AND username = 'codyc'")

def add_gratitude(gratitude) :
    cur.execute(f"INSERT INTO gratitudes_new (gratitude,username) VALUES ('{gratitude}', 'codyc')")

def remove_gratitude(gratitude) :
    cur.execute(f"DELETE FROM gratitudes_new WHERE gratitude = '{gratitude}' AND username = 'codyc'")

def add_reflection(reflection) :
    cur.execute(f"INSERT INTO reflections_new (reflection,username) VALUES ('{reflection}', 'codyc')")

def remove_reflection(reflection) :
    cur.execute(f"DELETE FROM reflections_new WHERE reflection = '{reflection}' AND username = 'codyc'")

def add_self_care_activity(self_care_activity) :
    cur.execute(f"INSERT INTO self_care_activities_new (self_care_activity, username) VALUES ('{self_care_activity}','codyc')")

def remove_self_care_activity(self_care_activity) :
    cur.execute(f"DELETE FROM self_care_activities_new WHERE self_care_activity = '{self_care_activity}' AND username = 'codyc'")

# def add_stressor() :
#     cur.execute(f"INSERT INTO stressors (id, stressor) VALUES (1, 'Love')")

# def remove_stressor() :
#     cur.execute(f"DELETE FROM stressors WHERE stressor = 'Love'")

def get_avg(category) :
    days = [10,30,90]
    ten_day_average = 0
    thirty_day_average = 0
    ninety_day_average = 0
    
    for i in range(len(days)) :  
        if category == 0:  # Assuming category 0 represents mood
            cur.execute(f"SELECT mood FROM user_entries ORDER BY entry_date DESC LIMIT {days[i]}")
            rows = cur.fetchall()
            total = 0

            num_entries = len(rows)
            
            for entry in rows[:min(days[i], len(rows))]:
                total += entry[0]
        
        avg = total / min(days[i], len(rows))
        
        if i == 0 :
            ten_day_average = avg
        elif i == 1 :
            thirty_day_average = avg
        elif i == 2 : 
            ninety_day_average = avg

    return f"{ten_day_average}\n{thirty_day_average}\n{ninety_day_average}"


def feed_values() : 
    for i in range(27) :
        cur.execute("""
        INSERT INTO user_entries (mood, energy_level, sleep_duration, sleep_quality, physical_symptoms, social_interaction, physical_activity, username)
        VALUES (10, 10, '10 hours', 10, 10, '10 hours', '10 hours', 'codyc')
        """)
        
def test() : 
     print( "hello")
    

# conn.commit()

# cur.close()
# conn.close()

