import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def transform_cart_data(raw_data):
    """
    Takes raw nested JSON data from the API and flattens it into a 
    tabular Pandas DataFrame ready for BigQuery.
    """
    logging.info("Starting data transformation...")
    
    # json_normalize "aplana" el JSON. 
    # Le decimos que extraiga la lista 'products' y mantenga los datos generales ('id', 'userId', 'date')
    df = pd.json_normalize(
        raw_data, 
        record_path=['products'], 
        meta=['id', 'userId', 'date']
    )
    
    # Renombramos las columnas para cumplir con las buenas prácticas de bases de datos (snake_case)
    df = df.rename(columns={
        'productId': 'product_id',
        'id': 'cart_id',
        'userId': 'user_id'
    })
    
    # Convertimos el texto de la fecha a un formato de tiempo real (datetime)
    df['date'] = pd.to_datetime(df['date'])
    
    # Reordenamos las columnas para que quede más visual
    df = df[['cart_id', 'user_id', 'date', 'product_id', 'quantity']]
    
    logging.info(f"Transformation complete! Flattened into {len(df)} individual line items.")
    return df

# Bloque de prueba
if __name__ == "__main__":
    # Importamos el extractor que hiciste antes
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from extractors.dummy_api_extractor import extract_sales_data
    
    # 1. Extraemos
    raw_data = extract_sales_data()
    
    if raw_data:
        # 2. Transformamos
        clean_df = transform_cart_data(raw_data)
        
        print("\n--- CLEAN TABULAR DATA (DATAFRAME) ---")
        print(clean_df.head(10)) # Mostramos las primeras 10 filas