import logging
import os
from etl.s3_reader import read_csv_from_s3
from etl.transformer import transform_dataframe
from etl.postgres_loader import load_to_postgres

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_etl():
    logging.info("🔁 Iniciando proceso ETL")

    df = read_csv_from_s3(
        bucket=os.getenv("S3_BUCKET"),
        key=os.getenv("S3_KEY"),
        aws_access_key=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    logging.info(f"✅ Archivo cargado desde S3 con {len(df)} filas")

    df = transform_dataframe(df)
    logging.info("🔧 Transformación completada")

    load_to_postgres(df, os.getenv("POSTGRES_URI"), os.getenv("TABLE_NAME"))
    logging.info("✅ Datos cargados exitosamente a PostgreSQL")


if __name__ == "__main__":
    try:
        run_etl()
        logging.info("🎉 Proceso ETL finalizado correctamente")
    except Exception as e:
        logging.error(f"💥 Error durante el proceso ETL: {e}", exc_info=True)
        raise
