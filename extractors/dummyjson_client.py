import requests
import logging


class DummyJSONClient:
    """Client for DummyJSON API (no API key needed)."""

    BASE_URL = "https://dummyjson.com"

    def fetch_users(self, limit=0):
        url = f"{self.BASE_URL}/users?limit={limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get("users", [])
        except Exception as e:
            logging.error(f"❌ DummyJSON request failed: {e}")
            return None