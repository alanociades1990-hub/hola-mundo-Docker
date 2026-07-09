from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'example'),
            database=os.getenv('MYSQL_DATABASE', 'testdb')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hola Mundo desde MySQL!' AS message;")
        message = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return message
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
