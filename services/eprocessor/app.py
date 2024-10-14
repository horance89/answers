import logging
import psycopg2
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(filename='/var/log/eprocessor-service.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

# Database connection function
def connect_db():
    return psycopg2.connect(
        host="postgres_db", 
        database="testdb", 
        user="testuser", 
        password="password"
    )

@app.route('/api/v1/event', methods=['POST'])
def process_event():
    data = request.json
    conn = connect_db()
    cur = conn.cursor()

    # Check if entry exists
    cur.execute("SELECT * FROM events WHERE hash = %s", (data['hash'],))
    result = cur.fetchone()

    if result:
        cur.execute("UPDATE events SET status = %s, type = %s WHERE hash = %s", 
                    (data['status'], data['type'], data['hash']))
    else:
        cur.execute("INSERT INTO events (hash, status, type) VALUES (%s, %s, %s)", 
                    (data['hash'], data['status'], data['type']))

    conn.commit()
    cur.close()
    conn.close()

    logging.info(f"Event processed: {data}")
    return jsonify({"message": "Event processed", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
