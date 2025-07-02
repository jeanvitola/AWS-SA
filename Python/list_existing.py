import boto3
from botocore.exceptions import ClientError




s3 =boto3.client('s3')
response =  s3.list_buckets()

for i in response['Buckets']:
    print(f"Bucket Name: {i['Name']}")
    print(f"Creation Date: {i['CreationDate']}")
    print("-----")  # Separator for clarity