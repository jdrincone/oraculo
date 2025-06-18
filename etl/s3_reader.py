import boto3
import io
import pandas as pd
import logging

def read_csv_from_s3(bucket, key, aws_access_key, aws_secret_key):
    logging.info(f"📥 Descargando archivo de S3: {bucket}/{key}")
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(io.BytesIO(obj['Body'].read()))
