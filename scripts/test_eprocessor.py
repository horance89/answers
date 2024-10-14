# test_eprocessor.py
import requests

# Define the URL for the eProcessor service
url = "http://localhost:8081/api/v1/event"

# Test data for an existing hash (modify as needed for your database content)
data_existing = {
    "status": "complete",
    "type": 1,
    "hash": "existing-hash"
}

# Test data for a new hash (simulate an insert)
data_new = {
    "status": "incomplete",
    "type": 5,
    "hash": "new-hash"
}

# Function to send a POST request
def send_post(data):
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

# Run the tests
print("Testing existing record update:")
send_post(data_existing)

print("\nTesting new record insertion:")
send_post(data_new)
