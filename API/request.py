import allure
import requests
from requests.auth import HTTPBasicAuth
from Data.first_test_data import payload, headers

from Utils.attach import response_logging, response_attaching, request_attaching

auth = {
       "login": "test_backend",
       "password": "test_backend"
        }

def post_request(url):
    with allure.step('Отправить POST запрос'):
        response = requests.post(
            url=url,
            verify=False,
            auth=HTTPBasicAuth(auth["login"], auth["password"]),
            headers=headers,
            json=payload
        )
    with allure.step('Добавляем request'):
        request_attaching(response)
    with allure.step('Логируем response'):
        response_logging(response)
    with allure.step('Добавляем вложения'):
        response_attaching(response)

    return response