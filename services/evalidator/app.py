# eValidator app.py
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

VALIDATION_WINDOW_MS = int(os.getenv('VALIDATION_WINDOW_MS', 5000))  # Default to 5000 if not set

event_store = {}  # Store events temporarily by hash

@app.route('/api/v1/validate', methods=['POST'])
def validate_event():
    data = request.json
    hash_value = data['hash']
    event_type = data['type']
    
    if hash_value in event_store:
        prev_event = event_store[hash_value]
        type_sum = prev_event['type'] + event_type
        if type_sum >= 10:
            return jsonify({"error": "Type sum >= 10", "events": [prev_event, data]}), 200
        else:
            return jsonify({"message": "No error, type sum < 10"}), 200
    else:
        # Store the event
        event_store[hash_value] = data

    return jsonify({"message": "Event validated", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
