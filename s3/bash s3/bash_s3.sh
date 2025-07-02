#!/bin/bash

# Pedir nombre del bucket al usuario
read -p "Ingresa el nombre del bucket (debe ser único a nivel global): " BUCKET_NAME

# Pedir región (opcionalmente puedes dejar una por defecto)
read -p "Ingresa la región (por defecto: us-east-1): " REGION
REGION=${REGION:-us-east-1}

# Validar si la región es us-east-1
if [ "$REGION" == "us-east-1" ]; then
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION"
else
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION"
fi

# Confirmación
if [ $? -eq 0 ]; then
  echo "✅ Bucket '$BUCKET_NAME' creado exitosamente en la región '$REGION'"
else
  echo "❌ Error al crear el bucket. Verifica el nombre y tus permisos."
fi
