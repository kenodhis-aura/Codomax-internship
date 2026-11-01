import json

def lambda_handler(event, context):
    print(f"Received event payload: {json.dumps(event)}")
    query_params = event.get('queryStringParameters') or {}
    visitor_name = query_params.get('name', 'Cloud Engineer')
    
    message = f"Hello {visitor_name}! Connection successful. Your serverless API backend is fully operational!"
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*" 
        },
        "body": json.dumps({
            "status": "success",
            "message": message,
            "module": "AWS Module 04: Serverless Architecture",
            "cloud_provider": "Amazon Web Services"
        })
    }
