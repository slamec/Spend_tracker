import sqlite3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_path(db_name: str) -> str:
    '''Get the full path of the database file.'''
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, db_name + '.db')

def execute_query(db_path: str, query: str, params: tuple = ()):
    '''Execute a query on the database.'''
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute(query, params)
            conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"Exception in _query: {e}")

def insert_data(db_name: str, table_name: str, category: str, amount: int, currency: str, date: str):
    '''Insert data into the database.'''
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

    db_path = get_db_path(db_name)
    create_table_query = f'''CREATE TABLE IF NOT EXISTS {table_name}
                             (id INTEGER PRIMARY KEY, category TEXT, amount INTEGER, currency TEXT, date TEXT)'''
    insert_query = f'''INSERT INTO {table_name} (category, amount, currency, date) VALUES (?, ?, ?, ?)'''
    
    execute_query(db_path, create_table_query)
    execute_query(db_path, insert_query, (category, amount, currency, date))
    logging.info(f"Inserted data into {table_name}: {category}, {amount}, {currency}, {date}")

def update_data(db_name: str, table_name: str, column_name_1: str, value_1, column_name_2: str, value_2):
    '''Update data in the database.'''
    # Validate data types
    if not isinstance(db_name, str):
        raise TypeError('db_name must be a string')
    if not isinstance(table_name, str):
        raise TypeError('table_name must be a string')

    db_path = get_db_path(db_name)
    update_query = f'''UPDATE {table_name} SET {column_name_1} = ? WHERE {column_name_2} = ?'''
    
    execute_query(db_path, update_query, (value_1, value_2))
    logging.info(f"Updated {table_name}: Set {column_name_1} to {value_1} where {column_name_2} is {value_2}")

def delete_data(db_name: str, table_name: str, column_name_1: str, value_1, column_name_2: str, value_2):
    '''Delete data from the database.'''
    # Validate data types
    if not isinstance(db_name, str):
        raise TypeError('db_name must be a string')
    if not isinstance(table_name, str):
        raise TypeError('table_name must be a string')

    db_path = get_db_path(db_name)
    delete_query = f'''DELETE FROM {table_name} WHERE {column_name_1} = ? AND {column_name_2} = ?'''
    
    execute_query(db_path, delete_query, (value_1, value_2))
    logging.info(f"Deleted from {table_name} where {column_name_1} is {value_1} and {column_name_2} is {value_2}")

# Example usage
insert_data(db_name='spend', table_name='spends', category='Lover', amount=4400, currency='CZK', date='19/10/2024')
update_data(db_name='spend', table_name='spends', column_name_1='amount', value_1=9000, column_name_2='category', value_2='Car')
delete_data(db_name='spend', table_name='spends', column_name_1='category', value_1='wife', column_name_2='amount', value_2=4400)

