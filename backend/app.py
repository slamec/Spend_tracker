from flask import Flask, request, jsonify
from flask_cors import CORS
from database import insert_data, update_data, delete_data, fetch_all_spends

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_spend():
    try:
        data = request.json
        app.logger.info(f"Received data for add: {data}")
        # Convert amount to integer
        data['amount'] = int(data['amount'])
        insert_data(data['db_name'], data['table_name'], data['category'], data['amount'], data['currency'], data['date'])
        return jsonify({"message": "Data inserted successfully"}), 201
    except Exception as e:
        app.logger.error(f"Error adding spend: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/update', methods=['PUT'])
def update_spend():
    try:
        data = request.json
        app.logger.info(f"Received data for update: {data}")
        update_data(data['db_name'], data['table_name'], data['column_name_1'], data['value_1'], data['column_name_2'], data['value_2'])
        return jsonify({"message": "Data updated successfully"}), 200
    except Exception as e:
        app.logger.error(f"Error updating spend: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete_spend():
    try:
        data = request.json
        app.logger.info(f"Received data for delete: {data}")
        delete_data(data['db_name'], data['table_name'], data['column_name_1'], data['value_1'], data['column_name_2'], data['value_2'])
        return jsonify({"message": "Data deleted successfully"}), 200
    except Exception as e:
        app.logger.error(f"Error deleting spend: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/spends', methods=['GET'])
def get_spends():
    try:
        db_name = request.args.get('db_name', 'spend')
        table_name = request.args.get('table_name', 'spends')
        app.logger.info(f"Fetching spends for db: {db_name}, table: {table_name}")
        spends = fetch_all_spends(db_name, table_name)
        return jsonify(spends), 200
    except Exception as e:
        app.logger.error(f"Error fetching spends: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)