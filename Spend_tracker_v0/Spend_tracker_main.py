#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import sqlite3
import os
import datetime
import currencies

#get current directory 
cwd = os.path.dirname(__file__)
db_path = os.path.join(cwd, 'example.db')

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

#insert data
c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
conn.commit()

c.execute("SELECT * FROM users")
print(c.fetchall())

#update data
c.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
conn.commit()

#delete data
c.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()



available_budget = []
spend = []
category = ['Housing', 'Car', 'Gasoline', 'Food']
date_time_now = datetime.datetime.now()
date_time_user = []
currency = currencies.Currency.get_currency_formats()
currency_user = []

print(cwd)
     
