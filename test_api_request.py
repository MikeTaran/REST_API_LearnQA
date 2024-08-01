import pytest
import requests


class TestApiRequest:

    # @pytest.skip
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        cookie = response.cookies.get("HomeWork")
        print()
        print(cookie)
        assert cookie == "hw_value", "not correct"

    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        header = response.headers.get("Content-Type")
        print()
        print(header)
        assert header == "application/json"
