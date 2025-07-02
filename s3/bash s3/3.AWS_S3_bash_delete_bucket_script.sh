#!/bin/bash

set -euo pipefail  # Mejora la seguridad: -u falla si una variable no está definida, -o pipefail captura errores en pipes

# Leer el nombre del bucket
read -p "Enter the name of the bucket to delete: " BUCKET_NAME

# Validar que el nombre no esté vacío
if [ -z "$BUCKET_NAME" ]; then
    echo "❌ No bucket name provided. Usage: $0 bucket-name"
    exit 1
fi

# Verificar si el bucket existe y si se tiene acceso
if ! aws s3api head-bucket --bucket "$BUCKET_NAME" 2>/dev/null; then
    echo "⚠️  The bucket '$BUCKET_NAME' does not exist or you don't have permission to access it."
    exit 1
fi

# Verificar si el bucket está vacío antes de eliminarlo
if ! aws s3 ls "s3://$BUCKET_NAME" | grep -q .; then
    echo "🗑️ Deleting bucket '$BUCKET_NAME'..."
    if aws s3api delete-bucket --bucket "$BUCKET_NAME"; then
        echo "✅ Bucket '$BUCKET_NAME' deleted successfully."
    else
        echo "❌ Failed to delete the bucket. Please check your permissions or try again."
        exit 1
    fi
else
    echo "❌ The bucket '$BUCKET_NAME' is not empty. Please empty it before deleting."
    exit 1
fi
