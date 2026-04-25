import requests
import logging


class APIClient:
    """
    A professional, reusable API client to fetch data from any REST endpoint.
    """
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def fetch_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        params = {"key": self.api_key} if self.api_key else {}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"❌ API request failed for {endpoint}: {e}")
            return None


def api_client(base_url, api_key=None):
    """Factory function for backwards compatibility."""
    return APIClient(base_url, api_key)