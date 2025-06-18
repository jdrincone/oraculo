from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(df: pd.DataFrame, db_uri: str, table_name: str):
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
