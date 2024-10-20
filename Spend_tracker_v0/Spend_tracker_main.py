#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import sqlite3
import os
import datetime
import currencies

def insert_data(db_name, table_name, category, amount, currency, date):
    '''Create a database and table, name of db and table name needed. 
        Then provide values for each variable.'''

    #get current working directory 
    cwd = os.path.dirname(__file__)
    db_path = os.path.join(cwd, db_name + '.db')

    #connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    #create a table, use DROP to delete a table
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                (id INTEGER PRIMARY KEY, category TEXT, amount INTEGER, currency TEXT, date TEXT)''')
    conn.commit()

    #insert data
    c.execute(f'''INSERT INTO {table_name} (category, amount, currency, date) VALUES (?, ?, ?, ?)''', 
              (category, amount, currency, date))
    conn.commit()

    #close connection
    conn.close()

insert_data(db_name='spend', table_name='spends', category='Car', amount=8000, currency='CZK', date='10/10/2024')

# c.execute("SELECT * FROM spend")
# print(c.fetchall())

# #update data
# c.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
# conn.commit()

# #delete data
# c.execute("DELETE FROM users WHERE name = 'Bob'")
# conn.commit()



