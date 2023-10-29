import allure
from allure_commons.types import Severity

import config
from demoblaze_test_project import utils


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('API')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем статус-код при запросе токена')
def test_login_status_code():
    payload = {
        "username": config.settings.USER_LOGIN,
        "password": config.settings.API_PASSWORD
    }
    with allure.step('Отправляем запрос'):
        response = utils.base_request.post('/login', json=payload)

    with allure.step('Проверяем статус-код'):
        assert response.status_code == 200


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('API')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем что вернулся токен')
def test_login_token():
    payload = {
        "username": config.settings.USER_LOGIN,
        "password": config.settings.API_PASSWORD
    }
    with allure.step('Отправляем запрос'):
        response = utils.base_request.post('/login', json=payload)

    with allure.step('Проверяем, что вернулся токен'):
        assert 'Auth_token:' in response.text
