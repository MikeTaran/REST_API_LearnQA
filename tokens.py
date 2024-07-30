import time
import requests

host = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(host)
response_json = response.json()
token = response_json["token"]
timeout = response_json["seconds"]
print(token, timeout)
param = {"token": token}
response = requests.get(host, params=param)
print(response.text)
response_json = response.json()
status = response_json["status"]
if status != "Job is NOT ready":
    print("not ready")
time.sleep(timeout)
response = requests.get(host, params=param)
print(response.text)
response_json = response.json()
status = response_json["status"]
if status != "Job is ready":
    print("not ready")
try:
    result = response_json["result"]
    print(result)
except KeyError:
    print("нет ключа result")
