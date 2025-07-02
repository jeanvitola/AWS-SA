
## ESTRUCTURA GENERAL DEL SCRIPT 
### CREATE AN AMAZON S3 BUCKET

 
import boto3
import logging 
from botocore.exceptions import ClientError
import os 

# configuración  inicial 

"""
* Importar boto3 ( sdk de AWS para Python) y botocore.exceptions.ClientError (para manejar errores específicos de AWS).
* Crea un cliente s3 y detecta la región actival del perfil 


locationConstraint : En este caso solo es un formato apra empaquetar datos 
"""

import boto3
import logging
from botocore.exceptions import ClientError

def bucket_exists(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.head_bucket(Bucket=bucket_name) 
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
        return False

def create_bucket(bucket_name, region=None):
    if bucket_exists(bucket_name):
        print(f"⚠️ El bucket '{bucket_name}' ya existe.")
        return False

    try:
        if region is None or region == 'us-east-1':
            s3_client = boto3.client('s3', region_name=region)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"✅ Bucket '{bucket_name}' creado exitosamente.")
    except ClientError as e:
        logging.error(f"❌ Error al crear el bucket: {e}")
        return False
    return True


if __name__ == "__main__":
    bucket_name = 'test-sqs-lambda-lab-2'  # Cambia esto al nombre de tu bucket
    region = 'us-east-1'  # Cambia esto a la región deseada, o None para usar la región por defecto

    if create_bucket(bucket_name, region):
        print(f"Bucket '{bucket_name}' creado exitosamente en la región '{region}'.")
    else:
        print(f"Fallo al crear el bucket '{bucket_name}'.")