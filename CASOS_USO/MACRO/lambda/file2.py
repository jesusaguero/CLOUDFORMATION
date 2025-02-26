import json
import uuid

def handler(event, context):
    fragment = event['fragment']

    for resource in fragment.get("Resources", {}):
        fragment["Resources"][resource]["Properties"]["Name"] = f"AutoName-{uuid.uuid4().hex[:6]}"
    
    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
