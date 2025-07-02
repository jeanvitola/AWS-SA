import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
import os 


# 1 CONFIGURACIÓN INICIAL 

s3 = boto3.client('s3')
region = boto3.session.Session().region_name or 'us-east-1'  # Establecer una región por defecto si no se encuentra una

"""  
 1. boto3
# La salida generalmente <botocore.client.S3 object at 0x000001758D661070>, que indica que se ha creado el cliente correctamente y es un objeto de tipo S3.
# botocore.cliente.s3 es el objeto creado
# 0x000001758D661070 es la direccion de memorio donde el objeto estará almacenado

2. region
boto3.session.Session() crea una nueva sesion de boto3. La cual peude tener aossiones de configuracion, como la region, las credenciales, etc.
En tal caso que region name  = None se devolvera el 'us-east-1' como region por defecto.

"""



# 2 CREAR EL BUCKET Y  CONFIGURAR LA REGION DE LA MISMA

import boto3
from botocore.exceptions import ClientError

# Obtener región actual o asignar 'us-east-1'
region = boto3.session.Session().region_name or 'us-east-1'
s3 = boto3.client('s3', region_name=region)


def bucket_exists(bucket_name):
    """Verifica si el bucket existe (en tu cuenta o globalmente)."""
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
        else:
            print(f"⚠️ Error inesperado al verificar el bucket: {e}")
            raise

def create_bucket(bucket_name):
    """Crea el bucket si no existe."""
    if bucket_exists(bucket_name):
        print(f"❌ El bucket '{bucket_name}' ya existe (puede ser tuyo o de otra cuenta).")
        return

    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"✅ Bucket '{bucket_name}' creado exitosamente en la región '{region}'.")
    except ClientError as e:
        print(f"❌ Error al crear el bucket: {e}")

# === USO ===
bucket_name = 'mi-nombre-unico-de-bucket-jean'  # Cambia esto
create_bucket(bucket_name)

"""
Este script utiliza un enfoque modular para gestionar la creación de buckets en S3.
La función bucket_exists verifica si el bucket ya existe, evitando duplicaciones o errores.
La función create_bucket decide si debe proceder con la creación según la región activa.
Este diseño mejora la legibilidad, reutilización y control de errores en operaciones con AWS S3.

"""