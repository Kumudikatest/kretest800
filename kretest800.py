import boto3
eventBridge = boto3.client("events")

def handler(event, context):
    try:
        data = eventBridge.put_events(
            Entries=[
                {
                    'EventBusName': "default",
                    'Source': "k",
                    'DetailType': "k",
                    'Detail': "{}"
                }
            ]
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
