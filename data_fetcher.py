import requests

API_KEY = "hOLnoaZ49FQ5wU7CokH5WXzqabKRVxD9NKIsik9U"
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
