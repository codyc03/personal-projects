import psycopg2
from psycopg2.sql import NULL

conn = NULL

try :
    conn = psycopg2.connect(
                                  dbname = "mydatabase",
                                  user = "postgres",
                                  password = "12345678",
                                  host = "localhost"
                           )
except Exception as e:
    raise NotImplementedError(e)

if(conn == NULL) :
    raise NotImplementedError()

cur = conn.cursor()
name = "Test User"

def add_user() :
    # TODO: Automate this with GUI
    cur.execute(f"INSERT INTO users_table (name) VALUES ('{name}')")

def remove_user():
    cur.execute(f"DELETE FROM users_table WHERE name = '{name}'")



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
