#!/bin/bash                              # Indica qie es un script de bash
set -e  # Sale si hay un error 

# 1 Solicita el nombre del bucket al usuario
read -p "🔤 Ingresa el nombre del bucket: " BUCKET_NAME   

# read es un comando de  Bash que permite la entrada del usuario por teclado, cuando se utilizac on la opción -p, puede mostrar un mensaje personlizado antes de la entrada del dato  "BUCKET_NAME" en este caso representa la variable en la cual se almacena ese input, es algo como BUCKET_NAME = Entrada 


# 2 Valida que se haya ingresado algo
if [ -z "$BUCKET_NAME" ]; then
  echo "❌ Debes ingresar un nombre de bucket."
  exit 1
fi

# El if : comienza una estructura condicional, mientras que [ -z "$BUCKET_NAME" ] valida que no esté vacia, especialmente con -z, el Exit = 1 es un comando que termina la ejecución del script y devuelve un código de salida al sistema operativo o al proceso que lo llamó


# 3. Solicita la región (valor por defecto: us-east-1)
read -p "🌍 Ingresa la región [por defecto: us-east-1]: " REGION
REGION=${REGION:-us-east-1}

# Hace exactamente lo mismo, mediante una read -p permite el input, luego alamcena ese input dentro de la variable REGION, si region está vacia este asgina por defecto a -us-east-1 como está almacenado, esto actua solo si el valor no está definido o vacio, no sobreescribe un valor que el usuario haya ingresado. Esta es una asignación condicional conocida como expansión por defecto BASH.




# 4 Verifica si el bucket ya existe
if aws s3api head-bucket --bucket "$BUCKET_NAME" 2>/dev/null; then
  echo "⚠️  El bucket '$BUCKET_NAME' ya existe o no tienes permisos para verificarlo."
  exit 1
fi

# aws s3api head-bucket --bucket "$BUCKET_NAME"
# Este comando intenta acceder a la cabecera (metadata) del bucket.
# Si el bucket existe (y tienes permiso para verlo), el comando retorna 0 (éxito).
# Si el bucket no existe o no tienes permiso, retorna un código de error (≠ 0).
# 🔕 2>/dev/null
# Esto oculta el mensaje de error que normalmente aparecería en la terminal.
# Redirige la salida de error estándar (stderr) al vacío (/dev/null).



# 5. Crea el bucket (varía según la región)
if [ "$REGION" == "us-east-1" ]; then
  aws s3api create-bucket --bucket "$BUCKET_NAME"
else
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION"
fi

echo "✅ Bucket '$BUCKET_NAME' creado exitosamente en la región '$REGION'."

# Por último lo que hace es ejecutar el código de linea que crea el bucket desde el CLI, con el nombre, y la región proporcionada.
# acá  hay que tener en cuenta que el bucket se crea según los parámetros pord efecto pero logicamente se puede emplear mas variables.