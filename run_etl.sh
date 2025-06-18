#!/bin/bash

# === VARIABLES ===
IMAGE_NAME="etl-s3-to-postgres"
ENV_FILE=".env"

# === VERIFICACIONES PREVIAS ===
if [ ! -f "$ENV_FILE" ]; then
  echo "❌ Archivo $ENV_FILE no encontrado. Por favor crea uno con tus credenciales."
  exit 1
fi

# === CONSTRUCCIÓN DE LA IMAGEN ===
echo "🚧 Construyendo imagen Docker: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

# === EJECUCIÓN DEL CONTENEDOR ===
echo "🚀 Ejecutando ETL desde contenedor..."
docker run --rm --env-file "$ENV_FILE" "$IMAGE_NAME"

# === CÓDIGO DE SALIDA ===
EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ Proceso ETL finalizado correctamente"
else
  echo "💥 Proceso ETL falló con código de salida: $EXIT_CODE"
fi

exit $EXIT_CODE
