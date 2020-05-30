import json
import urllib

def hello3(event, context):

    body = event["body"]
    print(body)

    body2 = urllib.parse.parse_qs(body)
    print(body2)

    # print(context)

    response = {
        "statusCode": 200,
        "body": "ok!"
    }

    return response
