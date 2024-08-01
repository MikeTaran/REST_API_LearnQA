import pytest
import requests


class TestApiRequest:
    user_agents = [
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 '
        '(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 '
        'Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
        'Safari/537.36 Edg/91.0.100.0',
        'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
        'Version/13.0.3 Mobile/15E148 Safari/604.1'
    ]

    expected_values = [
        {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    # @pytest.mark.skip
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        cookie = response.cookies.get("HomeWork")
        print()
        print(cookie)
        assert cookie == "hw_value", "not correct"

    # @pytest.mark.skip
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        header = response.headers.get("Content-Type")
        print()
        print(header)
        assert header == "application/json"

    @pytest.mark.parametrize("user_agent, expected", list(zip(user_agents, expected_values)))
    def test_agent(self, user_agent, expected):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

        response = requests.get(url, headers={"User-Agent": user_agent}).json()
        print()
        print(response)
        device = response["device"]
        platform = response["platform"]
        browser = response["browser"]

        exp_device = expected["device"]
        exp_platform = expected["platform"]
        exp_browser = expected["browser"]

        print(f"Device: {device}, expected: {exp_device}")
        print(f"Browser: {browser}, expected: {exp_browser}")
        print(f"Platform: {platform}, expected: {exp_platform}")

        assert device == exp_device, f"Device: {device}, expected: {exp_device}"
        assert browser == exp_browser, f"Browser: {browser}, expected: {exp_browser}"
        assert platform == exp_platform, f"Platform: {platform}, expected: {exp_platform}"
