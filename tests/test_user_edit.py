from datetime import datetime
import pytest
import requests
from lib.base_case import BaseCase
from lib.assertion import Assertion


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        # register
        url = "https://playground.learnqa.ru/api/user/"
        register_data = self.prepare_registration_data()
        response1 = requests.post(url, data=register_data)
        print(response1.text)
        Assertion.assert_response_code_status(response1, 200)
        Assertion.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        first_name = register_data["firstName"]
        user_id = self.get_json_value(response1, "id")

        # edit no login
        url3 = f"https://playground.learnqa.ru/api/user/{user_id}"
        new_name = "Sabaka"
        response5 = requests.put(url3,
                                 data={"firstName": new_name}
                                 )
        print("edit no login", response5.text)
        Assertion.assert_response_code_status(response5, 400)

        # login
        data = {
            "email": email,
            "password": password
        }
        url2 = "https://playground.learnqa.ru/api/user/login"
        response2 = requests.post(url2, data=data)
        Assertion.assert_response_code_status(response2, 200)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # edit
        url3 = f"https://playground.learnqa.ru/api/user/{user_id}"
        new_name = "Sabaka"
        response3 = requests.put(url3,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        print(response3.text)
        Assertion.assert_response_code_status(response3,200)

        # get
        url3 = f"https://playground.learnqa.ru/api/user/{user_id}"
        new_name = "Sabaka"
        response4 = requests.get(url3,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 )
        print(response4.text)
        Assertion.assert_response_code_status(response3, 200)
        Assertion.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "User was not updated!"
        )
