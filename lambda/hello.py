import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    body = {
        "message": "Hello, CDK! Your function executed successfully!",
        "input": event,
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': json.dumps(body)
        
    }
