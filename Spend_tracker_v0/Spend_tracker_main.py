#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import sqlite3
import os
import datetime
import currencies

def insert_data(db_name: str, table_name: str, category: str, 
                amount: int, currency: str, date: str):
    '''Create a database and table, name of db and table name needed. 
        Then provide values for each variable.'''
         
    # Validate data types
    if not isinstance(db_name, str):
        raise TypeError('db_name must be a string')
    if not isinstance(table_name, str):
        raise TypeError('table_name must be a string')
    if not isinstance(category, str):
        raise TypeError('category must be a string')
    if not isinstance(amount, int):
        raise TypeError('amount must be an integer')
    if not isinstance(currency, str):
        raise TypeError('currency must be a string')
    if not isinstance(date, str):
        raise TypeError('date must be a string')

    # get current working directory 
    cwd = os.path.dirname(__file__)
    db_path = os.path.join(cwd, db_name + '.db')

    # connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # create a table, use DROP to delete a table
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                (id INTEGER PRIMARY KEY, category TEXT, amount INTEGER, currency TEXT, date TEXT)''')
    conn.commit()

    # insert data
    c.execute(f'''INSERT INTO {table_name} (category, amount, currency, date) VALUES (?, ?, ?, ?)''', 
              (category, amount, currency, date))
    conn.commit()

    # close connection
    conn.close()

# insert_data(db_name='spend', table_name='spends', category='Food', amount=1200, currency='CZK', date='19/10/2024')

def update_data(db_name: str, table_name: str, column_name_1: str, value_1, 
                column_name_2: str, value_2: str):
    '''Update a database and table, name of db and table name needed. 
        Then provide values for each variable.'''
         
    # Validate data types
    if not isinstance(db_name, str):
        raise TypeError('db_name must be a string')
    if not isinstance(table_name, str):
        raise TypeError('table_name must be a string')

    # get current working directory 
    cwd = os.path.dirname(__file__)
    db_path = os.path.join(cwd, db_name + '.db')

    # connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # update data
    c.execute(f'''UPDATE {table_name} SET {column_name_1} = ? WHERE {column_name_2} = ?''',
              (value_1, value_2)) 
    conn.commit()

    # close connection
    conn.close()

update_data(db_name='spend', table_name='spends', column_name_1='amount', value_1=9000, 
            column_name_2='category', value_2='Car')

# #update data
# c.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
# conn.commit()

# #delete data
# c.execute("DELETE FROM users WHERE name = 'Bob'")
# conn.commit()

# c.execute("SELECT * FROM spend")
# print(c.fetchall())



