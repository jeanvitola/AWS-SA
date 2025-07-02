

import boto3 
from botocore.exceptions import ClientError
# Configuración inicial
#  VERIFICAR SI EL BUCKET EXISTE

"""
 * Verifica si un bucket con el nombre bucket_name ya existe en AWS
 
 -> COMO LO HACE ?

* Usa el método head_bucket del cliente s3
*Este método intenta obtener los metadatos del bucket especificado.
* Si el bucket existe y tú tienes permisos, no lanza error y devuelve True 
* Si el bucket no existe, lanza un ClientError con código 404 y devuelve False
* Si ocurre otro error, también devuelve False
* para cualquier otro error devuelve False

"""

# 1 BUCKET_EXISTS
def bucket_exists(bucket_name):
    s3 = boto3.client('s3') #  SI EL BUCKET EXISTE SE EJECUTA EL HEAD_BUCKET Y PASA A DAR LOS METADOS,
    """Sei el bucket existe lo que  hace es que se ejecuta una función head_data, el cuál apsa
    la metadata y deuelve el True, si no existe o hay un error, devuelve False."""
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
        return False
    
# 2 CREATE A BUCKET

"""
¿  QUE HACE PRIMERO ?
* Antes de crear un bucket llama a bucket_exists(bucket_name) para verificar si el bucket ya existe.
* si existe, muestra un mensaje de advertencia y no intenta crearlo, termina ahí con RETURN FALSE

-> Acá se ahce un IF tradicional en python, lo que va dentro del IF se EVALUA como True o False
->


"""  
## 1 El bucket_exists es uan función que definiste antes, que hace algo así :

def bucket_exists(bucket_name):
    # Si el bucket existe, retorna True
    # Si no existe o hay error, retorna False

"""
¿ POR QUÉ NO SE COMPARA EXPLICITAMENTE CON TRUE O FALSE?

"""

if bucket_exists(bucket_name): 

if bucket_exists(bucket_name) == True

if bucket_exists(bucket_name) is True:

"Lo mismo sucede con los valores falsos. Python considera False, o, none, [], {}"




# 2 CREATE A BUCKET

def create_bucket(bucket_name, region = None) :
    if bucket_exists(bucket_name):
        print(f"⚠️ El bucket '{bucket_name}' ya existe.")
        return False


"""
Luego de esta validación lo que ahce es intentar crear el bucket  si no existe,
si no se especifica la region  es 'us-east-1, crea el bucket sin apsar por el
createBucketconfiguration, porque en us-east-1 no es necesario especificar la región al crear un bucket.
"""
    try:
        if region is None or region == 'us-east-1':
            s3_client = boto3.client('s3', region_name=region)
            s3_client.create_bucket(Bucket=bucket_name)
    
"Si es otra región ya comienza a construir un diccionario"
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
