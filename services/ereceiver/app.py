# eReceiver/app.py
import logging
import uuid
import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/var/log/ereceiver-service.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

def is_valid_payload(data):
    # Validate status
    if data.get('status') not in ['complete', 'incomplete', 'cancelled']:
        return False, "Invalid status"
    # Validate type
    if data.get('type') not in [1, 2, 5, 11]:
        return False, "Invalid type"
    # Validate hash length (not format here)
    if not data.get('hash') or len(data['hash']) != 32:
        return False, "Invalid hash"
    return True, "Valid payload"

def create_cloud_event(data):
    return {
        "specversion": "1.0",
        "type": "com.evertest.event",
        "source": "ereceiver",
        "subject": "DATA",
        "id": str(uuid.uuid4()),
        "time": datetime.utcnow().isoformat() + "Z",
        "datacontenttype": "application/json",
        "data": data
    }

@app.route('/api/v1/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    is_valid, message = is_valid_payload(data)
    if not is_valid:
        logging.error(f"Invalid data: {message}")
        return jsonify({"error": message}), 400

    # Log the valid request
    logging.info(f"Data received: {data}")
    
    # Create Cloud Event
    cloud_event = create_cloud_event(data)
    
    # Here, add logic to publish the cloud event
    logging.info(f"Published Cloud Event: {json.dumps(cloud_event)}")
    
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
