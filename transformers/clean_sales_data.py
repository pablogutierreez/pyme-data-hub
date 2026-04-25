import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def transform_cart_data(raw_data):
    """
    Takes raw nested JSON data from the API and flattens it into a 
    tabular Pandas DataFrame ready for BigQuery.
    """
    logging.info("Starting data transformation...")
    
    df = pd.json_normalize(
        raw_data, 
        record_path=['products'], 
        meta=['id', 'userId', 'date']
    )
    
    df = df.rename(columns={
        'productId': 'product_id',
        'id': 'cart_id',
        'userId': 'user_id'
    })
    
    df['date'] = pd.to_datetime(df['date'])
    
    df = df[['cart_id', 'user_id', 'date', 'product_id', 'quantity']]
    
    logging.info(f"Transformation complete! Flattened into {len(df)} individual line items.")
    return df


if __name__ == "__main__":
    from extractors.api_client import APIClient
    from config.settings import API_BASE_URL, MOCKAROO_API_KEY

    client = APIClient(API_BASE_URL, MOCKAROO_API_KEY)
    raw_data = client.fetch_data("healthcare.json")
    
    if raw_data:
        clean_df = transform_cart_data(raw_data)
        print("\n--- CLEAN TABULAR DATA (DATAFRAME) ---")
        print(clean_df.head(10))