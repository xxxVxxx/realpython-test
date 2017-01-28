import sqlite3

conn = sqlite3.conn("new.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE population
                city TEXT, state TEXT, population int
            """)

conn.close()
