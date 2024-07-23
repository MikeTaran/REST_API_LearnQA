import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
history_redirect = response.history
last_url = response.url

print(len(history_redirect))
print(last_url)
