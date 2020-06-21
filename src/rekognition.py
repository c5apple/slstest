import boto3
import time

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

#
# Rekognitionサンプル(動画の節度)
#
def video_moderation(event, context):

    for record in event['Records']:

        input_key = record['s3']['object']['key']
        bucket = record['s3']['bucket']['name']
        print('bucket:', bucket)
        print('input_key:', input_key)

        rekognition = boto3.client('rekognition')
        response = rekognition.start_content_moderation(
            Video={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': input_key
                }
                # 実運用ではNotificationChannelをつけたほうが良さそう
                # NotificationChannel={
                #     'SNSTopicArn': 'string',
                #     'RoleArn': 'string'
                # }
            }
        )

        job_id = response['JobId']
        print('job_id:', job_id)

        pagination_token = ''
        finished = False

        while finished == False:

            response = rekognition.get_content_moderation(
                JobId=job_id,
                MaxResults=10,
                NextToken=pagination_token
            )

            for moderation_label in response['ModerationLabels']:

                print('-- ModerationLabels --')
                print('Confidence:', moderation_label['ModerationLabel']['Confidence'])
                print('Name:', moderation_label['ModerationLabel']['Name'])
                print('ParentName:', moderation_label['ModerationLabel']['ParentName'])
                print('Timestamp:', moderation_label['Timestamp'])

            if 'NextToken' in response:
                pagination_token = response['NextToken']

            if response['JobStatus'] != 'IN_PROGRESS':
                finished = True
            else:
                time.sleep(5)

        print('End')

    return {
        'statusCode': 200,
        'body': 'OK'
    }
