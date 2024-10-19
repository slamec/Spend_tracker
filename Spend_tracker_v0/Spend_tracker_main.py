#imports 
#def add all the spends and categorize them
#visualise the spends vs. monthly budget

import pickle
import datetime
import currencies

spends = [1, 2, 600, 900, 300]
category = ['Housing', 'Car', 'Gasoline', 'Food']
date_time = datetime.datetime.now()
currency = currencies.Currency.get_currency_formats()


