import logging
from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='/var/log/evalidator-service.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

# In-memory event tracking
events = {}

@app.route('/api/v1/validate', methods=['POST'])
def validate_event():
    data = request.json
    hash_value = data['hash']
    current_time = datetime.utcnow()
    events[hash_value] = events.get(hash_value, []) + [(data, current_time)]

    # Clean up events outside the validation window
    for key, items in list(events.items()):
        events[key] = [(d, t) for d, t in items if current_time - t < timedelta(milliseconds=5000)]
        if not events[key]:
            del events[key]

    # Check for conditions and publish error event if needed
    total_type = sum(d['type'] for d, _ in events[hash_value])
    if total_type >= 10:
        logging.info(f"Publishing error event for hash {hash_value}")
        publish_cloud_event(events[hash_value], source="evalidator", subject="ERROR")

    logging.info(f"Event validated: {data}")
    return jsonify({"message": "Event validated", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
