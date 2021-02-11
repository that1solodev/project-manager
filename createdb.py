import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""CREATE TABLE project(
                ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
                Client_name TEXT,
                Project_desc TEXT,
                Total_Amount REAL,
                Start_Date TEXT,
                End_Date TEXT
)""")

c.execute("""CREATE TABLE transactions(
                ProjectID INTEGER NOT NULL,
                TransactionID TEXT NOT NULL,
                Amount REAL,
                Transaction_Date TEXT

)""")
conn.commit()
conn.close()
