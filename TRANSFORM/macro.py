import json

def lambda_handler(event, context):
    print("Evento recibido:", json.dumps(event, indent=2))
    
    template = event["fragment"] 

    # Agregar la etiqueta "Environment: Production" a todos los recursos con Tags
    for resource_name, resource in template.get("Resources", {}).items():
        if "Properties" in resource and "Tags" in resource["Properties"]:
            resource["Properties"]["Tags"].append({"Key": "Environment", "Value": "Production"})

    return {
        "requestId": event["requestId"],  
        "status": "success",              
        "fragment": template              
    }
