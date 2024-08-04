import pytest
from lib.base_case import BaseCase
from lib.assertion import Assertion as A
from lib.my_requests import MyRequests
import allure


@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    @allure.description("Setup method")
    def setup_method(self):
        print("Setup method executed")
        login = "vintokot@example.com"
        password = "1234"

        data = {
            "email": login,
            "password": password
        }
        uri1 = "/user/login"

        response1 = MyRequests.post(uri1, data=data)
        print()
        A.assert_response_code_status(response1, 200)
        print(response1.text)
        print(response1.cookies)
        print(response1.headers)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_login = self.get_json_value(response1, "user_id")

    @allure.description("Teardown method")
    def teardown_method(self):
        # Этот метод будет вызываться после каждого теста
        print()
        print("Teardown method executed")
        # Здесь можно выполнять любую очистку или освобождение ресурсов
        self.auth_sid = None
        self.token = None
        self.user_id_from_login = None

    @allure.description("Test positive auth")
    def test_user_auth(self):

        uri2 = "/user/auth"
        response2 = MyRequests.get(uri2,
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid}
                                   )
        A.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_login,
            "The user id is not equal"
        )

    @allure.description("Test negative auth")
    @pytest.mark.parametrize("cond", exclude_params)
    def test_negative_auth(self, cond):

        uri2 = "/user/auth"
        if cond == "no_cookie":
            response2 = MyRequests.get(uri2,
                                       headers={"x-csrf-token": self.token},
                                       cookies={}
                                       )
        else:
            response2 = MyRequests.get(uri2,
                                       headers={"x-csrf-token": ""},
                                       cookies={"auth_sid": self.auth_sid}
                                       )
        A.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"The user is authorized with conditions: {cond}"
        )
        print(self.get_json_value(response2, "user_id"))
