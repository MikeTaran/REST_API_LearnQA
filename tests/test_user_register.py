from datetime import datetime
import pytest
from lib.base_case import BaseCase
from lib.assertion import Assertion
from lib.my_requests import MyRequests


class TestUserRegistration(BaseCase):
    conds = [
        "no_username",
        "no_firstName",
        "no_lastName",
        "no_email",
        "no_password"
    ]

    def test_create_user_success(self):
        data = self.prepare_registration_data()
        uri = "/user/"
        response = MyRequests.post(uri, data=data)
        print(response.text)
        Assertion.assert_response_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")

    def test_create_user_with_incorrect_email(self):
        rnd = datetime.now().strftime("%H%M%S")
        email = f"vintokot{rnd}2example.com"
        data = self.prepare_registration_data(email)
        url = "/user/"
        response = MyRequests.post(url, data=data)
        print(response.text)
        Assertion.assert_response_code_status(response, 400)
        assert response.text == "Invalid email format", f"Unexpected response text: {response.text}"

    def test_create_user_with_short_username(self):
        password = "1234"
        email = "vintokot@example.com"
        data = {
            "username": "K",
            "firstName": "Kot",
            "lastName": "Vint",
            "email": email,
            "password": password
        }
        uri = "/user/"
        response = MyRequests.post(uri, data=data)
        print(response.text)
        Assertion.assert_response_code_status(response, 400)
        assert response.text == "The value of 'username' field is too short", \
            f"Unexpected response text: {response.text}"

    def test_create_user_with_long_username(self):
        password = "1234"
        email = "vintokot@example.com"
        data = {
            "username": "The Postman JavaScript API functionality enables you to programmatically access and alter "
                        "request and response data and variables using the pm object. You can also dynamically alter "
                        "execution order to build request workflows for the Collection RunnerThe Postman JavaScript API"
                        " functionality enables you to programmatically access and alter "
                        "request and response data and variables using the pm object. You can also dynamically alter "
                        "execution order to build request workflows for the Collection Runner",
            "firstName": "Kot",
            "lastName": "Vint",
            "email": email,
            "password": password
        }
        uri = "/user/"
        response = MyRequests.post(uri, data=data)
        print(response.text)
        Assertion.assert_response_code_status(response, 400)
        assert response.text == "The value of 'username' field is too long", \
            f"Unexpected response text: {response.text}"

    def test_create_user_with_existing_email(self):
        login = "vintokot@example.com"
        password = "1234"
        data = {
            "username": "Kot",
            "firstName": "Kot",
            "lastName": "Vint",
            "email": login,
            "password": password
        }
        uri = "/user/"
        response = MyRequests.post(uri, data=data)

        print()
        print(response.status_code)
        print(response.text)
        Assertion.assert_response_code_status(response, 400)
        assert response.content.decode("utf-8") == "Users with email 'vintokot@example.com' already exists", (
            f"Unexpected response content: {response.content}")

    @pytest.mark.parametrize("cond", conds)
    def test_create_user_with_wrong_params(self, cond):
        password = "1234"
        email = "vintokot@example.com"
        data = {
            "username": "Kot",
            "firstName": "Kot",
            "lastName": "Vint",
            "email": email,
            "password": password
        }
        conditions_to_keys = {
            "no_username": "username",
            "no_firstName": "firstName",
            "no_lastName": "lastName",
            "no_email": "email",
            "no_password": "password"
            }
        key_to_clear = conditions_to_keys.get(cond)
        if key_to_clear:
            # data[key_to_clear] = ""
            del data[key_to_clear]
        uri = "/user/"
        response = MyRequests.post(uri, data=data)
        print(data)
        print(response.text)
        Assertion.assert_response_code_status(response, 400)
