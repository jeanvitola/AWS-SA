import boto3
from botocore.exceptions import ClientError



s3 = boto3.client('s3')

# 4. Listar todos los buckets y sus regiones
def listar_buckets():
    respuesta = s3.list_buckets()
    for bucket in respuesta['Buckets']:
        name = bucket['Name']
        try:
            location = s3.get_bucket_location(Bucket=name)['LocationConstraint']
            location = location or 'us-east-1'
        except ClientError as e:
            location = 'Error'
        print(f"🪣 {name} => Región: {location}")

listar_buckets()