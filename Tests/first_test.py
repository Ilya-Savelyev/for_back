import allure
from API import request



@allure.feature("")
@allure.story("")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("")
def test_test(base_url):
    response = request.post_request(base_url + '/posts')
    assert response.status_code == 201, "Ожидается статус код 201"
