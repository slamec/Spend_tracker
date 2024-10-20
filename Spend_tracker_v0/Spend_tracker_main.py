#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import sqlite3
import os
import datetime
import currencies

#get current working directory 
cwd = os.path.dirname(__file__)
db_path = os.path.join(cwd, 'example.db')

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS spend
             (id INTEGER PRIMARY KEY, category TEXT, amount INTEGER, currency TEXT, date TEXT)''')
conn.commit()

#insert data
c.execute("INSERT INTO spend (category, amount, currency, date) VALUES ('Car', '8000', 'CZK', '10/10/2024')")
conn.commit()

c.execute("SELECT * FROM spend")
print(c.fetchall())

# #update data
# c.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
# conn.commit()

# #delete data
# c.execute("DELETE FROM users WHERE name = 'Bob'")
# conn.commit()



