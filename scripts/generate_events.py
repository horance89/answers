import json
import random
import hashlib

# Define possible values for status and type
statuses = ["complete", "incomplete", "cancelled"]
types = [1, 2, 5, 11]

# Function to generate a valid random MD5 hash
def generate_md5():
    random_string = str(random.random()).encode('utf-8')
    return hashlib.md5(random_string).hexdigest()

# Function to generate a valid eReceiver JSON Data Cloud Event
def generate_ereceiver_event():
    event = {
        "status": random.choice(statuses),
        "type": random.choice(types),
        "hash": generate_md5()
    }
    return event

# Generate 100 valid events and store them in a list
events = [generate_ereceiver_event() for _ in range(100)]

# Print the generated events as JSON
print(json.dumps(events, indent=4))
