import json

def handler(event, context):
    fragment = event['fragment']
    
    if "ShortInstance" in fragment:
        fragment["Resources"]["MyInstance"] = {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "InstanceType": "t2.micro",
                "ImageId": "ami-12345678"
            }
        }
    
    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
