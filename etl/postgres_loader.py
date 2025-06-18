from sqlalchemy import create_engine, text
import pandas as pd
import logging

def load_to_postgres(df: pd.DataFrame, db_uri: str, table_name: str):
    engine = create_engine(db_uri)
    with engine.begin() as conn:
        logging.info(f"📤 Cargando datos en tabla {table_name}")
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        logging.info("🔧 Ejecutando permisos y propietario...")
        conn.execute(text(f"ALTER TABLE public.{table_name} OWNER TO postgres;"))
        conn.execute(text(f"""
            GRANT DELETE, INSERT, REFERENCES, SELECT, TRIGGER, TRUNCATE, UPDATE
            ON public.{table_name} TO n8n;
        """))

    logging.info("✅ Carga completada y permisos asignados")
