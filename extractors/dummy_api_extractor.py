import requests
import logging

# Configuramos el sistema de alertas (Logging) para que se vea profesional
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def extract_sales_data():
    """
    Extracts mock e-commerce cart data from a public free API.
    This simulates pulling orders from Shopify, WooCommerce, or Stripe.
    """
    url = "https://fakestoreapi.com/carts"
    logging.info(f"Connecting to Dummy API: {url}")
    
    try:
        # Hacemos la "llamada" a la API
        response = requests.get(url)
        # Esto hace que el código falle con gracia si la API está caída
        response.raise_for_status() 
        
        # Convertimos la respuesta a un formato JSON (diccionarios de Python)
        data = response.json()
        
        logging.info(f"Success! Extracted {len(data)} shopping carts.")
        return data
        
    except requests.exceptions.RequestException as e:
        logging.error(f"API connection failed: {e}")
        return None

# Este bloque solo se ejecuta si lanzamos este script directamente
if __name__ == "__main__":
    raw_data = extract_sales_data()
    if raw_data:
        print("\n--- SAMPLE OF THE FIRST EXTRACTED RECORD ---")
        print(raw_data[0])