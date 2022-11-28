import requests
from config import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Barbers",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

name_business = [business["name"]
                 for business in businesses if business["rating"] > 5]
