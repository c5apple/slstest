import boto3

#
# Rekognitionサンプル(画像の節度)
#
def image_moderation(event, context):

    for record in event['Records']:

        input_key = record['s3']['object']['key']
        bucket = record['s3']['bucket']['name']
        print('bucket:', bucket)
        print('input_key:', input_key)

        rekognition = boto3.client('rekognition')
        response = rekognition.detect_moderation_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': input_key
                }
            }
        )

        for moderation_label in response['ModerationLabels']:
 
            print('-- ModerationLabels --')
            print('Confidence:', moderation_label['Confidence'])
            print('Name:', moderation_label['Name'])
            print('ParentName:', moderation_label['ParentName'])

    return {
        'statusCode': 200,
        'body': 'OK'
    }
