import requests
from pprint import pprint

username = "NixOS Package Collection"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)

