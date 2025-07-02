#!/bin/bash

set -e  # El script fallará si hay un error

read -p "Ingresa el nombre del bucket de S3: " BUCKET_NAME

# Verifica que el directorio "temp" exista
if [ ! -d "./temp" ]; then
    echo "❌ El directorio 'temp' no existe. Por favor, ejecuta el script de generación de archivos primero."
    exit 1
fi

# Usa 'files' como prefijo por defecto si no se pasa como argumento
FILE_PREFIX=${2:-files}

# Subir archivos con cifrado SSE-KMS
aws s3 sync ./temp "s3://$BUCKET_NAME/$FILE_PREFIX" \
  --sse aws:kms
