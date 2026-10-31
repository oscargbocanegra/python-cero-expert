import requests
from typing import Dict, Any


def get_location(ip: str) -> Dict[str, Any]:
    url: str = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data: Dict[str, Any] = response.json()

  # Set a breakpoint for debugging
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }
