# test_evalidator.py
import requests

url = "http://localhost:8082/api/v1/validate"

# Valid event
valid_event = {
    "status": "complete",
    "type": 5,
    "hash": "valid-hash"
}

# Invalid event
invalid_event = {
    "status": "complete",
    "type": 15,  # Exceeds threshold of 10
    "hash": "invalid-hash"
}

def send_post(data):
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

print("Testing valid event:")
send_post(valid_event)

print("\nTesting invalid event:")
send_post(invalid_event)
