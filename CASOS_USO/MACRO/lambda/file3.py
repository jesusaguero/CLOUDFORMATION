import json

def handler(event, context):
    fragment = event['fragment']
    
    for resource in fragment.get("Resources", {}):
        if "Description" in fragment["Resources"][resource]["Properties"]:
            fragment["Resources"][resource]["Properties"]["Description"] = fragment["Resources"][resource]["Properties"]["Description"].replace("{{ENV}}", "Producción")
    
    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
