import psycopg2

conn = psycopg2.connect(
                                  dbname = "mydatabase",
                                  user = "postgres",
                                  password = "12345678",
                                  host = "localhost"
                                  )

cur = conn.cursor()


# cur.execute("INSERT INTO users_table (id, name) VALUES (001, 'Cody Christensen')") 

cur.execute("""
        CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY,
        goal TEXT   
        )
            """) 

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
