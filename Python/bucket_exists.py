import boto3
from botocore.exceptions import ClientError




def bucket_exists(bucket_name):
    """Check if an S3 bucket exists."""
    s3 = boto3.client('s3')
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
        return False  # For any other error, return False



if __name__ == "__main__":
    bucket_name = 'test-sqs-lambda-lab-1'  # Change this to your bucket name

    if bucket_exists(bucket_name):
        print(f"✅ The bucket '{bucket_name}' exists.")
    else:
        print(f"❌ The bucket '{bucket_name}' does not exist.")