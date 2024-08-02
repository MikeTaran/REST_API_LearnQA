from requests import Response
import json


class Assertion:

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"

        assert name in response_dict, f"The key: {name} is not in response JSON"
        assert response_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"
        assert name in response_dict, f"The key: {name} is not in response JSON"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"
        for name in names:
            assert name in response_dict, f"The key: {name} is not in response JSON"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"
        for name in names:
            assert name not in response_dict, f"The key: {name} shouldn't in response JSON, but it is present"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"
        assert name not in response_dict, f"The key: {name} shouldn't  in response JSON, but it is present"

    @staticmethod
    def assert_response_code_status(response: Response,expected_code):
        assert response.status_code == expected_code, (f"Unexpected status code! Expected: {expected_code}, "
                                                       f"actual: {response.status_code}")
