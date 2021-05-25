import requests
import os
import json

from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Grab environment variables
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST")
RAPIDAPI_URL = f'https://{RAPIDAPI_HOST}'

# Endpoints 
AUTOCOMPLETE_ENDPOINT = "/auto-complete"

headers = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": RAPIDAPI_HOST
}

query = {
    "q": "tesla",
    "region": "US"
}

response = requests.get(
    url = RAPIDAPI_URL + AUTOCOMPLETE_ENDPOINT,
    headers=headers,
    params=query
)

print(response.text)