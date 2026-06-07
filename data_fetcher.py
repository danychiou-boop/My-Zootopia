import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params={"name": animal_name}
    )

    return response.json()
