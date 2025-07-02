import boto3
from botocore.exceptions import ClientError
import os

# Configuración inicial
s3 = boto3.client('s3')
region = boto3.session.Session().region_name or 'us-east-1'

# 1. Crear bucket con bloqueo público
def crear_bucket_con_bloqueo(bucket_name):
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )

        # Bloquear acceso público
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print(f"✅ Bucket '{bucket_name}' creado con acceso público bloqueado.")
    except ClientError as e:
        print(f"❌ Error: {e}")

# 2. Subir archivos desde una carpeta
def subir_directorio(local_dir, bucket_name):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)

    for root, _, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.relpath(local_path, local_dir)
            bucket.upload_file(local_path, s3_path)
            print(f"📤 Subido: {local_path} -> s3://{bucket_name}/{s3_path}")

# 3. Habilitar versionado
def habilitar_versionado(bucket_name):
    s3_version = boto3.client('s3')
    s3_version.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"🔁 Versionado habilitado en '{bucket_name}'.")

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

# 5. Eliminar todos los objetos del bucket
def vaciar_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.all().delete()
    print(f"🧹 Bucket '{bucket_name}' vaciado.")

# =======================
# Ejecutar flujo completo
# =======================
if __name__ == "__main__":
    bucket = input("Nombre del bucket: ")
    crear_bucket_con_bloqueo(bucket)

    local = input("Ruta local de archivos a subir: ")
    subir_directorio(local, bucket)

    habilitar_versionado(bucket)
    listar_buckets()

    confirm = input(f"¿Deseas vaciar el bucket '{bucket}'? (y/N): ").lower()
    if confirm == 'y':
        vaciar_bucket(bucket)
