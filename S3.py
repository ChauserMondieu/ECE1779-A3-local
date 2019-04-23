import boto3
bucket_name="ece1779avatarss"


def upload_photo(user_name, photo_stream):
    client = boto3.client('s3')
    response = client.put_object(ACL='public-read', Body=photo_stream,
                                 Bucket=bucket_name, Key='People/' + str(user_name) + '.jpg',
                                 ContentType='image/jpeg')
    return response


def copy_photo(user_name):
    client = boto3.client('s3')
    response = client.copy_object(ACL='public-read', Bucket=bucket_name,
                                  CopySource={'Bucket': bucket_name, 'Key': 'Public/default_avatar.jpg'},
                                  Key='People/' + str(user_name) + '.jpg',
                                  ContentType='image/jpeg')
    return response


