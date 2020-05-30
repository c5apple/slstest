import json


def hello2(event, context):

    row1='"aaaa","bbbb","cccc"'
    row2='aaaa,bbbb,cccc'
    csv=""
    csv=csv+row1+str('\n')
    csv=csv+row2+str('\n')

    response = {
        "statusCode": 200,
        "body": csv,
        "headers": {"content-type": "text/csv"}
    }

    return response
