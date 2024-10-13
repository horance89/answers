# eProcessor app.py
from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection details (loaded from .env)
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_NAME = os.getenv('POSTGRES_DB', 'testdb')
DB_USER = os.getenv('POSTGRES_USER', 'testuser')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'password')

def connect_db():
    conn = psycopg2.connect(
        host=DB_HOST, 
        database=DB_NAME, 
        user=DB_USER, 
        password=DB_PASS
    )
    return conn

@app.route('/api/v1/event', methods=['POST'])
def process_event():
    data = request.json
    conn = connect_db()
    cur = conn.cursor()
    
    # Check for the hash in the database (simulate logic)
    cur.execute("SELECT * FROM events WHERE hash = %s", (data['hash'],))
    result = cur.fetchone()
    
    if result:
        # Update entry
        cur.execute("UPDATE events SET status = %s, type = %s WHERE hash = %s", 
                    (data['status'], data['type'], data['hash']))
    else:
        # Insert new entry
        cur.execute("INSERT INTO events (hash, status, type) VALUES (%s, %s, %s)", 
                    (data['hash'], data['status'], data['type']))
    
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Event processed", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
