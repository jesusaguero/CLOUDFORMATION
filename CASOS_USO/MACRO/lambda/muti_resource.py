import json

def handler(event, context):
    fragment = event['fragment']
    new_resources = {}

    for i, env in enumerate(["Dev", "Prod"]):
        new_resources[f"MyBucket{env}"] = {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": f"mybucket-{env.lower()}"
            }
        }

    fragment["Resources"].update(new_resources)
    
    return {"requestId": event["requestId"], "status": "success", "fragment": fragment}
