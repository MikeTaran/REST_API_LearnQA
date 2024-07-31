import requests

host1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
host2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
# host = "https://playground.learnqa.ru/ajax/api/get_auth_cookie"
passwords = []
payload = {
    "login": "super_admin",
    "password": "secret_pass"
}
response1 = requests.post(host1, data=payload)

print(response1.status_code)
print(response1.text)
print(dict(response1.cookies))

cookie_val = response1.cookies.get("auth_cookie")
print(cookie_val)
cookies = {}
if cookie_val is not None:
    cookies = {"auth_cookie": cookie_val}
response2 = requests.post(host2, cookies=cookies)
print(response2.text)
