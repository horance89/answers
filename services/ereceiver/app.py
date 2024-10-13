import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(filename='/var/log/ereceiver-service.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

@app.route('/api/v1/data', methods=['POST'])
def receive_data():
    data = request.json

    # Check for payload format
    if not isinstance(data, dict):
        print("Invalid payload format")  # Print to debug
        return jsonify({"error": "Invalid payload format"}), 400

    # Validate 'status'
    if 'status' not in data or data['status'] not in ['complete', 'incomplete', 'cancelled']:
        print("Invalid status")  # Print to debug
        return jsonify({"error": "Invalid status"}), 400

    # Validate 'type'
    if 'type' not in data or data['type'] not in [1, 2, 5, 11]:
        print("Invalid type")  # Print to debug
        return jsonify({"error": "Invalid type"}), 400

    # Validate 'hash'
    if 'hash' not in data or len(data['hash']) != 32:
        print("Invalid hash")  # Print to debug
        return jsonify({"error": "Invalid hash"}), 400

    # Log successful request
    logging.info(f"Data received: {data}")
    print("Request is valid and processed")  # Print to debug success

    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
