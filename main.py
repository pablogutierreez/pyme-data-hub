import os
import logging
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


def run_multi_niche_pipeline():
    logging.info("🚀 STARTING GLOBAL PORTFOLIO INGESTION")

    api_key = os.getenv("MOCKAROO_API_KEY")
    base_url = os.getenv("API_BASE_URL")
    project_id = os.getenv("GCP_PROJECT_ID")

    if not api_key:
        logging.error("❌ MOCKAROO_API_KEY not found in .env")
        return

    from extractors.api_client import api_client
    client = api_client(base_url, api_key)

    verticals = [
        {"name": "E-commerce", "endpoint": "ecommerce.json", "table": "fact_ecommerce_sales"},
        {"name": "Gym & SaaS", "endpoint": "gym_saas.json", "table": "fact_gym_memberships"},
        {"name": "Healthcare", "endpoint": "healthcare.json", "table": "fact_clinic_appointments"},
        {"name": "Logistics", "endpoint": "logistics.json", "table": "fact_logistics_trips"},
        {"name": "Real Estate", "endpoint": "real_estate.json", "table": "fact_real_estate_listings"},
    ]

    logging.info(f"Using Google Cloud Project: {project_id}")

    for industry in verticals:
        try:
            logging.info(f"📦 Extracting {industry['name']} data...")
            data = client.fetch_data(industry["endpoint"])

            if data:
                df = pd.DataFrame(data)

                date_cols = [col for col in df.columns if "Date" in col or "Time" in col]
                for col in date_cols:
                    df[col] = pd.to_datetime(df[col], errors="coerce")

                logging.info(f"✅ {industry['name']}: {len(df)} rows extracted")

                from loaders.bigquery_loader import load_to_bigquery
                load_to_bigquery(df, industry["table"])
            else:
                logging.warning(f"⚠️ No data returned for {industry['name']}")

        except Exception as e:
            logging.error(f"❌ Error processing {industry['name']}: {e}")

    logging.info("🏁 ALL VERTICALS PROCESSED SUCCESSFULLY")


if __name__ == "__main__":
    run_multi_niche_pipeline()