import logging
from google.cloud import bigquery
from config.settings import PROJECT_ID, DATASET_ID

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def load_to_bigquery(df, table_name):
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"
    logging.info(f"Connecting to BigQuery to load data into {table_id}...")

    try:
        client = bigquery.Client(project=PROJECT_ID)
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
        )
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()

        table = client.get_table(table_id)
        logging.info(f"✅ Success! Table {table_name} now has {table.num_rows} rows.")
    except Exception as e:
        logging.error(f"❌ Failed to load data to BigQuery: {e}")
