import boto3

dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table('sample')

#
# DynamoDBサンプル
#
def lambda_handler(event, context):

    insert(event)

    value = search(event)

    delete(event)

    response = {
        "statusCode": 200,
        "body": value
    }

    return response

# データ登録
def insert(event):

    table.put_item(
        Item = {
            'id': event['id'],
            'sample_value': event['sample_value']
        }
    )
    print("PutItem succeeded:")

    return

# データ取得
def search(event):
    query_data = table.get_item(
        Key={
            'id': event['id']
            }
        )
    print("GetItem succeeded:")

    # 取り出す時は
    sample_value = query_data['Item']['sample_value']

    return sample_value

# データ削除
def delete(event):

    table.delete_item(
        Key={
            'id': event['id']
        }
    )

    print("DeleteItem succeeded:")

    return
