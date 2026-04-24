import os
import logging
from google.cloud import bigquery
from config.settings import PROJECT_ID, DATASET_ID
from dotenv import load_dotenv

load_dotenv()

from extractors.dummy_api_extractor import extract_sales_data
from transformers.clean_sales_data import transform_cart_data
from loaders.bigquery_loader import load_to_bigquery

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_to_bigquery(df, table_name):
    """
    Takes a Pandas DataFrame and securely loads it into a BigQuery table.
    """
    project_id = "smb-data-hub-pro" 
    dataset_id = "sales_data" 
    
    # Construimos la ruta completa de la tabla en BigQuery
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    
    logging.info(f"Connecting to BigQuery to load data into {table_id}...")
    
    try:
        client = bigquery.Client(project=project_id)
        
        # Configuramos cómo queremos que se suban los datos
        job_config = bigquery.LoadJobConfig(
            # Si la tabla ya existe, añadimos los datos al final (Append)
            write_disposition="WRITE_TRUNCATE",
        )

        # Hacemos la subida mágica
        job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        
        job.result()  # Esperamos a que el trabajo termine
        
        # Comprobamos cuántas filas han llegado vivas
        table = client.get_table(table_id)
        logging.info(f"✅ Success! Table {table_name} now has {table.num_rows} rows.")
        
    except Exception as e:
        logging.error(f"❌ Failed to load data to BigQuery: {e}")