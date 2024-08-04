# Автоматизация тестирования REST API на Python

[LearnQA API](https://playground.learnqa.ru/api/map) : [framework](https://github.com/MikeTaran/REST_API_LearnQA)

### run pytest
`python -m pytest -s .\test_example.py -k "test_check"`
### run pytest + allure
`python -m pytest -s --alluredir=test_results .\tests\test_user_auth.py`
### run allure report
`allure serve .\test_results\`
### setup environment for PowerShell
`$env:ENV = "prod"`
### setup environment for CMD
`set ENV=prod`

### Docker
`docker pull python` /скачать образ
`docker build -t pytest_runner .`  / coздать образ с тестами
`docker run --rm --mount type=bind, src=F:\IT\REST_API_LearnQA, target=/tests_project/ pytest_runner` / запуск

### Docker compose
`docker-compose up --build`








