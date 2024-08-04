from lib.base_case import BaseCase
from lib.assertion import Assertion
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        # register
        uri = "/user/"
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(uri, data=register_data)
        print(response1.text)
        Assertion.assert_response_code_status(response1, 200)
        Assertion.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        first_name = register_data["firstName"]
        user_id = self.get_json_value(response1, "id")

        # edit no login
        uri3 = f"/user/{user_id}"
        new_name = "Sabaka"
        response5 = MyRequests.put(uri3,
                                 data={"firstName": new_name}
                                 )
        print("edit no login", response5.text)
        Assertion.assert_response_code_status(response5, 400)

        # login
        data = {
            "email": email,
            "password": password
        }
        uri2 = "/user/login"
        response2 = MyRequests.post(uri2, data=data)
        Assertion.assert_response_code_status(response2, 200)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # edit
        uri3 = f"/user/{user_id}"
        new_name = "Sabaka"
        response3 = MyRequests.put(uri3,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        print(response3.text)
        Assertion.assert_response_code_status(response3,200)

        # get
        uri3 = f"/user/{user_id}"
        new_name = "Sabaka"
        response4 = MyRequests.get(uri3,
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
