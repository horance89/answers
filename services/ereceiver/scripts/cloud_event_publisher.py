# cloud_event_publisher.py
import json
import uuid
from datetime import datetime
import requests


def publish_cloud_event(event_data, source, subject):
    cloud_event = {
        "specversion": "1.0",
        "type": "com.evertest.event",
        "source": source,
        "subject": subject,
        "id": str(uuid.uuid4()),
        "time": datetime.utcnow().isoformat() + "Z",
        "datacontenttype": "application/json",
        "data": event_data
    }
    try:
        print("Sending Cloud Event to eProcessor:", cloud_event)
        response = requests.post("http://eprocessor:8081/api/v1/event", json=cloud_event)
        print("Response from eProcessor:", response.status_code)
    except Exception as e:
        print("Error sending to eProcessor:", e)
        
        
    # Print to console for debugging purposes
    print("Publishing Cloud Event:")
    print(json.dumps(cloud_event, indent=4))
