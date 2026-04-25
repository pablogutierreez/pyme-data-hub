import pandas as pd
import logging


def flatten_user_coordinates(raw_data):
    """
    Flattens nested DummyJSON user data:
    user -> address -> coordinates -> lat/lng
    into a flat DataFrame for BigQuery.
    """
    logging.info("Flattening DummyJSON user coordinates...")

    rows = []
    for user in raw_data:
        address = user.get("address", {})
        coordinates = address.get("coordinates", {})

        rows.append({
            "user_id": user.get("id"),
            "first_name": user.get("firstName"),
            "last_name": user.get("lastName"),
            "email": user.get("email"),
            "city": address.get("city"),
            "state": address.get("state"),
            "country": address.get("country", "United States"),
            "latitude": coordinates.get("lat"),
            "longitude": coordinates.get("lng"),
        })

    df = pd.DataFrame(rows)
    logging.info(f"Flattened {len(df)} user records with coordinates.")
    return df