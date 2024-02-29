from flask import Flask, jsonify
import os
import pymysql

app = Flask(__name__)

def get_database_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        database=os.environ.get('DB_NAME', 'mydatabase')
    )

@app.route('/')
def get_all_rows():
    connection = None  # Initialize connection to None
    try:
        connection = get_database_connection()
        with connection.cursor() as cursor:
            query = "SELECT * FROM users;"
            cursor.execute(query)
            rows = cursor.fetchall()

        return jsonify({'data': rows})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
