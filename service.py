import boto3

def get_presigned_tuple(bucket, path):
    s3_client = boto3.client('s3')
    response = s3_client.generate_presigned_post(bucket, path, Fields=None, Conditions=None, ExpiresIn=3600)
    return response['url'], response['fields']
