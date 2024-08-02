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
