import json

def handler(event, context):
    fragment = event['fragment']
    
    for param in fragment.get("Parameters", {}):
        if param == "InstanceType" and fragment["Parameters"][param]["Default"] not in ["t2.micro", "t3.medium"]:
            raise Exception(f"El tipo de instancia {fragment['Parameters'][param]['Default']} no es válido.")

    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
