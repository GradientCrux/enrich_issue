from typing import List, Optional
from pydantic import BaseModel
import functions_framework
import base64
import json

# Define the Pydantic models
class ImageDetectionIssue(BaseModel):
    # Define fields as needed, placeholder for now
    issue_type: str
    confidence: Optional[float]

class PubSubIssue(BaseModel):
    image_url: str
    detected_issues: Optional[List[ImageDetectionIssue]] = None
    latitude: Optional[float]
    longitude: Optional[float]

@functions_framework.cloud_event
def enrich_issue(cloud_event):
    """
    Cloud Function triggered from a Pub/Sub message.
    Args:
        cloud_event: The CloudEvent containing the Pub/Sub message.
    """
    data = cloud_event.data
    if 'message' not in data or 'data' not in data['message']:
        raise ValueError('Invalid Pub/Sub message format')
    
    # Decode the Pub/Sub message data
    payload = base64.b64decode(data['message']['data']).decode('utf-8')
    payload_json = json.loads(payload)
    
    # Parse with Pydantic
    issue = PubSubIssue(**payload_json)
    print(f"Parsed issue: {issue}")
    # Add enrichment logic here
    return 'OK' 