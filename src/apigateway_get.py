import json

#
# API Gateway GETサンプル
#
def lambda_handler(event, context):

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
