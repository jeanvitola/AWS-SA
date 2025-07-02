import boto3 




# Inicializar cliente
s3 = boto3.client('s3')

def habilitar_versionado(bucket_name):
    """Activa el versionado en un bucket S3."""
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"🔁 Versionado habilitado en '{bucket_name}'.")

def verificar_o_habilitar_versionado(bucket_name):
    """Verifica el estado del versionado y lo habilita si no está configurado."""
    response = s3.get_bucket_versioning(Bucket=bucket_name)
    status = response.get('Status')

    if status == 'Enabled':
        print(f"✅ El bucket '{bucket_name}' ya tiene el versionado ACTIVADO.")
    elif status == 'Suspended':
        print(f"⚠️ El bucket '{bucket_name}' tiene el versionado SUSPENDIDO.")
    else:
        print(f"❌ El bucket '{bucket_name}' no tiene el versionado configurado.")
        habilitar_versionado(bucket_name)

# === USO ===
bucket_name = 'jeancarlosvitolatestjunio'
verificar_o_habilitar_versionado(bucket_name)
