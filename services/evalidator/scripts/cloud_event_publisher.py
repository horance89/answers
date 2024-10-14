# cloud_event_publisher.py
import json
import uuid
from datetime import datetime

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

    # Print to console for debugging purposes
    print("Publishing Cloud Event:")
    print(json.dumps(cloud_event, indent=4))
