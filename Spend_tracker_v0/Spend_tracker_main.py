#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import sqlite3
import os
import datetime
import currencies

cwd = os.path.dirname(__file__)
db_path = os.path.join(cwd, 'example.db')

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

available_budget = []
spend = []
category = ['Housing', 'Car', 'Gasoline', 'Food']
date_time_now = datetime.datetime.now()
date_time_user = []
currency = currencies.Currency.get_currency_formats()
currency_user = []

print(cwd)
     
