import requests


class TestApiCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        cookie = response.cookies.get("HomeWork")
        print()
        print(cookie)
        assert cookie == "hw_value", "not correct"
