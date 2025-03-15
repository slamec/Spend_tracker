import sqlite3
import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/spends', methods=['POST'])
def insert_data():
    data = request.json
    category = data.get('category')
    amount = data.get('amount')
    currency = data.get('currency')
    date = data.get('date')

    db_path = get_db_path('spend')
    create_table_query = '''CREATE TABLE IF NOT EXISTS spends
                             (id INTEGER PRIMARY KEY, category TEXT, amount INTEGER, currency TEXT, date TEXT)'''
    insert_query = '''INSERT INTO spends (category, amount, currency, date) VALUES (?, ?, ?, ?)'''
    
    execute_query(db_path, create_table_query)
    execute_query(db_path, insert_query, (category, amount, currency, date))
    logging.info(f"Inserted data into spends: {category}, {amount}, {currency}, {date}")
    return jsonify({'message': 'Data inserted successfully'}), 201

@app.route('/spends', methods=['PUT'])
def update_data():
    data = request.json
    category = data.get('category')
    amount = data.get('amount')

    db_path = get_db_path('spend')
    update_query = '''UPDATE spends SET amount = ? WHERE category = ?'''
    
    execute_query(db_path, update_query, (amount, category))
    logging.info(f"Updated spends: Set amount to {amount} where category is {category}")
    return jsonify({'message': 'Data updated successfully'}), 200

@app.route('/spends', methods=['DELETE'])
def delete_data():
    data = request.json
    category = data.get('category')
    amount = data.get('amount')

    db_path = get_db_path('spend')
    delete_query = '''DELETE FROM spends WHERE category = ? AND amount = ?'''
    
    execute_query(db_path, delete_query, (category, amount))
    logging.info(f"Deleted from spends where category is {category} and amount is {amount}")
    return jsonify({'message': 'Data deleted successfully'}), 200

@app.route('/spends', methods=['GET'])
def get_spends():
    db_path = get_db_path('spend')
    query = '''SELECT * FROM spends'''
    
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        spends = [{'id': row[0], 'category': row[1], 'amount': row[2], 'currency': row[3], 'date': row[4]} for row in rows]
    
    return jsonify(spends), 200

if __name__ == '__main__':
    app.run(debug=True)