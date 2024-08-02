import json.decoder

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookies with name:{cookie_name} in the last request"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find cookies with name:{header_name} in the last request"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"

        assert name in response_dict, f"The key: {name} is not in response JSON"
        return response_dict[name]