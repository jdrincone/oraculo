# ETL Pipeline: S3 CSV to PostgreSQL

 **Pipeline ETL automatizado** que extrae archivos CSV desde Amazon S3, realiza transformaciones de datos y los carga en PostgreSQL.

## 🏗️ Arquitectura

```
oraculo/
├── main.py                 # Punto de entrada principal
├── etl/                    # Módulos ETL
│   ├── s3_reader.py       # Extracción desde S3
│   ├── transformer.py     # Transformaciones de datos
│   └── postgres_loader.py # Carga a PostgreSQL
├── requirements.txt       # Dependencias Python
├── pyproject.toml        # Configuración del proyecto
├── Dockerfile           # Imagen Docker
├── run_etl.sh          # Script de ejecución
└── README.md           # Este archivo
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.11+
- Docker (opcional)
- Acceso a AWS S3
- Base de datos PostgreSQL

### Instalación Local

```bash
# Clonar el repositorio
git clone <repository-url>
cd oraculo

# Instalar dependencias
pip install -r requirements.txt
```

### Instalación con Docker

```bash
# Construir imagen
docker build -t etl-s3-to-postgres .
```

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` con las siguientes variables:

```bash
# AWS S3
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
S3_BUCKET=your-bucket-name
S3_KEY=data/your-file.csv

# PostgreSQL
POSTGRES_URI=postgresql://user:password@host:port/database
TABLE_NAME=transformed_data
```

### Ejemplo de POSTGRES_URI

```
postgresql://username:password@localhost:5432/database_name
```

## 🎯 Uso

### Ejecución Local

```bash
# Configurar variables de entorno
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
export S3_BUCKET="your-bucket"
export S3_KEY="data/file.csv"
export POSTGRES_URI="postgresql://user:pass@host:5432/db"
export TABLE_NAME="my_table"

# Ejecutar ETL
python main.py
```

### Ejecución con Docker

```bash
# Usar el script de ejecución
./run_etl.sh

# O ejecutar manualmente
docker run --rm --env-file .env etl-s3-to-postgres
```




