from datetime import datetime
import pytest
import requests
from lib.base_case import BaseCase
from lib.assertion import Assertion


class TestUserInfo(BaseCase):
    def test_user_info_no_auth(self):
        id = 102659
        url = f"https://playground.learnqa.ru/api/user/{id}"
        response = requests.get(url)
        Assertion.assert_response_code_status(response, 200)
        print(response.status_code)
        print(response.text)
        Assertion.assert_json_has_key(response, "username")
        Assertion.assert_json_has_not_key(response, "firstName")
        Assertion.assert_json_has_not_key(response, "lastName")
        Assertion.assert_json_has_not_key(response, "email")

    def test_user_info_auth_as_same_user(self):
        login = "vintokot@example.com"
        password = "1234"

        data = {
            "email": login,
            "password": password
        }
        url1 = "https://playground.learnqa.ru/api/user/login"

        response1 = requests.post(url1, data=data)
        Assertion.assert_response_code_status(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_login = self.get_json_value(response1, "user_id")

        url2 = f"https://playground.learnqa.ru/api/user/{user_id_from_login}"
        response2 = requests.get(url2,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        print(response2.text)
        Assertion.assert_response_code_status(response2, 200)
        expected_keys = ["username", "firstName", "lastName", "email"]
        Assertion.assert_json_has_keys(response2,expected_keys)

    def test_user_info_auth_another_user(self):
        login = "vintokot@example.com"
        password = "1234"

        data = {
            "email": login,
            "password": password
        }
        url1 = "https://playground.learnqa.ru/api/user/login"

        response1 = requests.post(url1, data=data)
        Assertion.assert_response_code_status(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = 2

        url2 = f"https://playground.learnqa.ru/api/user/{user_id}"
        response2 = requests.get(url2,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        print(response2.text)
        Assertion.assert_response_code_status(response2, 200)
        Assertion.assert_json_has_key(response2, "username")
        not_expected_keys = ["firstName", "lastName", "email"]
        Assertion.assert_json_has_not_keys(response2,not_expected_keys)


