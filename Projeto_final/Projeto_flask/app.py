import flask
from flask import jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)  # Add this line to enable CORS
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'mysql_api_container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mysqldocker'

mysql = MySQL(app)

# Route to insert data into the database
@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        # Get data from the request
        data = request.json
        
        # Check if 'message' key exists in the request data
        if 'message' not in data:
            return jsonify({'error': 'Message key is missing in the request data'}), 400
        
        message = data['message']
        
        # Insert data into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO messages (message) VALUES (%s)', (message,))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'Data inserted into MySQL database successfully.', 'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
