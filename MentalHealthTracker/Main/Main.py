import psycopg2

conn = psycopg2.connect(
                                  dbname = "mydatabase",
                                  user = "postgres",
                                  password = "12345678",
                                  host = "localhost"
                                  )

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE mytable2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    
    )

    """
    ) 

conn.commit()

cur.close()
conn.close()

print()
