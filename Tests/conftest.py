import allure
import pytest

from API import request
from Data.first_test_data import payload, headers


@pytest.fixture
def base_url():
    return 'http://testbackend.local/wp-json/wp/v2'


@pytest.fixture
def post_request(base_url):
    with allure.step('Отправить запрос'):
        response = request.post_request(base_url + '/posts')
        assert response.status_code == 201
        return response.status_code

