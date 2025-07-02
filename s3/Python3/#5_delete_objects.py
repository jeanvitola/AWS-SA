import boto3 


def vaciar_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.all().delete()
    print(f"🧹 Bucket '{bucket_name}' vaciado.")


vaciar_bucket('jeancarlosvitolatestjunio')