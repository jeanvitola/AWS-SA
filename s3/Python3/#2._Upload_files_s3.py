import boto3 
from botocore.exceptions import ClientError
import os 

import boto3
import os

# Reemplaza con tu ruta local (usa r'' para evitar errores con las barras invertidas)
local_files = r'C:\Users\USUARIO\OneDrive\Escritorio\AWS Architect\Glue\aws-glue-101\products.csv'
bucket_name = 'awsgluelabjean'

# Inicializar el recurso de S3
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(bucket_name)

# Subir todos los archivos de la carpeta
for root, dirs, files in os.walk(local_files):
    for file in files:
        local_path = os.path.join(root, file)
        s3_key = os.path.relpath(local_path, local_files).replace('\\', '/')

        print(f"Subiendo {local_path} como {s3_key}...")
        bucket.upload_file(local_path, s3_key)

print("✅ Todos los archivos han sido cargados con éxito.")

"""
#1. For root, dirs, files in os.walk(local_files):

* os.walk() recorre todas las subcarpetas y archivos de la ruta local_files.
Te devuelve :
- root: la ruta actual que se está recorriendo.
- dirs: una lista de subdirectorios en la ruta actual.
- files: una lista de archivos en la ruta actual.
#2. local_path = os.path.join(root, file)
Construye la ruta completa en tu sistema para ese archivo
ejemplo :

root = 'C:/mi/carpeta'
file = 'imagen.jpg'
local_path → 'C:/mi/carpeta/imagen.jpg'




 """

# Tener en cuanta que cuando subimos archivos y tienen la misma KEY se reemplazan sin un mensaje previo de advertencia.
# Para este caso se peude manejar versionamiento o crear una clave unica para cada archivo empleando un timestamp o un UUID.