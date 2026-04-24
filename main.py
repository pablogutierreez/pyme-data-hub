import logging
from extractors.dummy_api_extractor import extract_sales_data
from transformers.clean_sales_data import transform_cart_data
from loaders.bigquery_loader import load_to_bigquery

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_pipeline():
    logging.info("🚀 STARTING PIPELINE: SMB Data Hub")
    
    # 1. EXTRACT
    raw_data = extract_sales_data()
    if not raw_data:
        logging.error("Pipeline stopped: Extraction failed.")
        return

    # 2. TRANSFORM
    clean_df = transform_cart_data(raw_data)
    if clean_df.empty:
        logging.error("Pipeline stopped: Transformation resulted in empty data.")
        return

    # 3. LOAD
    # Le decimos que guarde los datos en una tabla llamada 'raw_carts_api'
    load_to_bigquery(clean_df, "raw_carts_api")
    
    logging.info("🏁 PIPELINE FINISHED SUCCESSFULLY")

if __name__ == "__main__":
    run_pipeline()