import pandas as pd



def limpiar_valor(x):
    if pd.isna(x):
        return None
    x = str(x).strip().replace(',', '')
    if x == '':
        return None
    return float(x)

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df["fecha_liberacion_raw"] = pd.to_datetime(
        df["fecha_liberacion_raw"], errors="coerce", dayfirst=True)
    df["fecha_liberacion_raw"] = df["fecha_liberacion_raw"].dt.date


    columnas_a_limpiar = [
        'cantidad_planificada', 'cantidad_entregada',
        'code_101', 'code_102', 'code_261',
        'code_641', 'code_642', 'diff',
        'cons_cap'
    ]

    for col in columnas_a_limpiar:
        df[col] = df[col].apply(limpiar_valor)
    
    return df
