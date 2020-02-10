import json
import time


def hello(event, context):
    body = {
        "message": "Hello Worl. Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

