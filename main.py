import requests
import json

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)
