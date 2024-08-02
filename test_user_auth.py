import pytest
import requests


class TestUserAuth:

    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    def setup_method(self):
        print("Setup method executed")
        login = "vintokot@example.com"
        password = "1234"

        data = {
            "email": login,
            "password": password
        }
        url1 = "https://playground.learnqa.ru/api/user/login"

        response1 = requests.post(url1, data=data)
        print(response1.status_code)
        print(response1.text)
        print(response1.cookies)
        print(response1.headers)

        assert "auth_sid" in response1.cookies, "There is no auth_sid in response cookies"
        assert "x-csrf-token" in response1.headers, "There is no x-csrf-token in response headers"
        assert "user_id" in response1.json(), "There is no user id in response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_login = response1.json()["user_id"]

    def teardown_method(self):
        # Этот метод будет вызываться после каждого теста
        print("Teardown method executed")
        # Здесь можно выполнять любую очистку или освобождение ресурсов
        self.auth_sid = None
        self.token = None
        self.user_id_from_login = None

    def test_user_auth(self):

        url2 = "https://playground.learnqa.ru/api/user/auth"
        response2 = requests.get(url2,
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid}
                                 )
        assert "user_id" in response2.json(), "There is no user id in auth response"
        user_id_from_auth = response2.json()["user_id"]
        print(user_id_from_auth)
        assert self.user_id_from_login == user_id_from_auth, "The user id is not equal"

    @pytest.mark.parametrize("cond", exclude_params)
    def test_negative_auth(self, cond):

        url2 = "https://playground.learnqa.ru/api/user/auth"
        if cond == "no_cookie":
            response2 = requests.get(url2,
                                     headers={"x-csrf-token": self.token},
                                     cookies={}
                                     )
            assert "user_id" in response2.json(), "There is no user id in auth response"
            user_id = response2.json()["user_id"]
            assert user_id == 0, ""

        elif cond == "no_token":
            response2 = requests.get(url2,
                                     headers={"x-csrf-token": ""},
                                     cookies={"auth_sid": self.auth_sid}
                                     )
            assert "user_id" in response2.json(), "There is no user id in auth response"
            user_id = response2.json()["user_id"]
            assert user_id == 0, f"The user is authorized with conditions: {cond}"
