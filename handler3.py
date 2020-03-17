import json


def hello3(event, context):

    print(event["body"])
    # print(context)

    response = {
        "statusCode": 200,
        "body": "ok!"
    }

    return response
