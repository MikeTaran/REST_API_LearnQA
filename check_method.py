import requests

host_url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ["GET", "POST", "PUT", "DELETE"]

# 1. Делает http-запрос любого типа без параметра method
response_without_method = requests.get(host_url)
print(f"Request without method: {response_without_method.text}")

# 2. Делает http-запрос не из списка. Например, HEAD
response_head = requests.head(host_url, params={"method": "HEAD"})
print(f"HEAD request: {response_head.text}")

# 3. Делает запрос с правильным значением method
for method in methods:
    if method == "GET":
        response = requests.get(host_url, params={"method": method})
    elif method == "POST":
        response = requests.post(host_url, data={"method": method})
    elif method == "PUT":
        response = requests.put(host_url, data={"method": method})
    elif method == "DELETE":
        response = requests.delete(host_url, data={"method": method})

    print(f"{method} request with correct method parameter: {response.text}")

# 4. Проверяет все возможные сочетания реальных типов запроса и значений параметра method
for actual_method in methods:
    for method_param in methods:
        if actual_method == "GET":
            response = requests.get(host_url, params={"method": method_param})
        elif actual_method == "POST":
            response = requests.post(host_url, data={"method": method_param})
        elif actual_method == "PUT":
            response = requests.put(host_url, data={"method": method_param})
        elif actual_method == "DELETE":
            response = requests.delete(host_url, data={"method": method_param})

        print(f"Actual method: {actual_method}, Method param: {method_param}, Response: {response.text}")

