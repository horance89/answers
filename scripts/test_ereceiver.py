#test_ereceiver.py
import sys
import requests
import json

url = "http://localhost:8080/api/v1/data"

valid_payload = {
    "status": "complete",
    "type": 1,
    "hash": "661f8009fa8e56a9d0e94a0a644397d7"
}

invalid_payload = {
    "status": "invalid",
    "type": 99,
    "hash": "invalid_hash"
}

def send_post_request(payload):
    response = requests.post(url, json=payload)
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.json()}")

if __name__ == "__main__":
    print("Sending valid request:")
    send_post_request(valid_payload)

    print("\nSending invalid request:")
    send_post_request(invalid_payload)
