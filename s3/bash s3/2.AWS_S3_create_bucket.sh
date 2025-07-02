#!/bin/bash                              
set -e  # Sale si hay un error 

# Solicita el nombre del bucket al usuario
read -p "🔤 Ingresa el nombre del bucket: " BUCKET_NAME   

# Valida que se haya ingresado algo
if [ -z "$BUCKET_NAME" ]; then
  echo "❌ Debes ingresar un nombre de bucket."
  exit 1
fi

# Solicita la región (valor por defecto: us-east-1)
read -p "🌍 Ingresa la región [por defecto: us-east-1]: " REGION
REGION=${REGION:-us-east-1}

# Verifica si el bucket ya existe
if aws s3api head-bucket --bucket "$BUCKET_NAME" 2>/dev/null; then
  echo "⚠️  El bucket '$BUCKET_NAME' ya existe o no tienes permisos para verificarlo."
  exit 1
fi

# Crea el bucket (varía según la región)
if [ "$REGION" == "us-east-1" ]; then
  aws s3api create-bucket --bucket "$BUCKET_NAME"
else
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION"
fi

echo "✅ Bucket '$BUCKET_NAME' creado exitosamente en la región '$REGION'."
