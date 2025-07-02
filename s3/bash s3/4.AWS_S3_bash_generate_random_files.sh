#!/bin/bash
set -e  # El script fallará si hay un error
OUTPUT_DIR="./temp" # Directorio temporal para los archivos generados
mkdir -p $OUTPUT_DIR # Crea el directorio si no existe
rm -rf $OUTPUT_DIR/* # Limpia el directorio temporal
NUM_FILES=$((RANDOM % 6 + 5)) # Genera un número aleatorio entre 5 y 10
for i in $(seq 1 $NUM_FILES); do 
    FILE_NAME="$OUTPUT_DIR/file_$i.txt"
    head -c 100 </dev/urandom > $FILE_NAME
    echo "Created $FILE_NAME"
done

# Al final crea una carpeta temporar  llamada "temp" y genera entre 5 y 10 archivos de texto aleatorios de 100 bytes cada uno.