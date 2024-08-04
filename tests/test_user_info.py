from lib.base_case import BaseCase
from lib.assertion import Assertion
from lib.my_requests import MyRequests


class TestUserInfo(BaseCase):
    def test_user_info_no_auth(self):
        id = 102659
        uri = f"/user/{id}"
        response = MyRequests.get(uri)
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
        url1 = "/user/login"

        response1 = MyRequests.post(url1, data=data)
        Assertion.assert_response_code_status(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_login = self.get_json_value(response1, "user_id")

        uri2 = f"/user/{user_id_from_login}"
        response2 = MyRequests.get(uri2,
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        print(response2.text)
        Assertion.assert_response_code_status(response2, 200)
        expected_keys = ["username", "firstName", "lastName", "email"]
        Assertion.assert_json_has_keys(response2, expected_keys)

    def test_user_info_auth_another_user(self):
        login = "vintokot@example.com"
        password = "1234"

        data = {
            "email": login,
            "password": password
        }
        uri1 = "/user/login"

        response1 = MyRequests.post(uri1, data=data)
        Assertion.assert_response_code_status(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = 2

        uri2 = f"/user/{user_id}"
        response2 = MyRequests.get(uri2,
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        print(response2.text)
        Assertion.assert_response_code_status(response2, 200)
        Assertion.assert_json_has_key(response2, "username")
        not_expected_keys = ["firstName", "lastName", "email"]
        Assertion.assert_json_has_not_keys(response2, not_expected_keys)
