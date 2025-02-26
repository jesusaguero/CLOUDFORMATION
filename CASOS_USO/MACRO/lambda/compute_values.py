import json

def handler(event, context):
    fragment = event['fragment']

    for resource in fragment.get("Resources", {}):
        if "Size" in fragment["Resources"][resource]["Properties"]:
            original_size = fragment["Resources"][resource]["Properties"]["Size"]
            fragment["Resources"][resource]["Properties"]["Size"] = original_size * 2  # Duplicamos el tamaño

    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
