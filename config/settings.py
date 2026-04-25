import os
from dotenv import load_dotenv

# Cargamos el .env desde aquí para que todo el proyecto lo tenga disponible
load_dotenv()

# Google Cloud Config
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "smb-data-hub-pro")
DATASET_ID = os.getenv("BQ_DATASET_ID", "sales_data")

# API Config
API_BASE_URL = os.getenv("API_BASE_URL", "https://my.api.mockaroo.com")
MOCKAROO_API_KEY = os.getenv("MOCKAROO_API_KEY", "b20e7cd0")