import allure
from allure_commons.types import Severity
from selene import browser

from config import settings
from demoblaze_test_project.pages.index import Index
from demoblaze_test_project.pages.login_form import LoginForm

index = Index()
login_form = LoginForm()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя')
def test_login():
    index.open_main_page()

    index.open_login_window()
    with allure.step('Заполняем данные пользователя'):
        login_form.fill_user(settings.USER_LOGIN, settings.USER_PASSWORD)
    with allure.step('Нажимаем кнопку "Log in"'):
        login_form.click_login()

    index.should_have_registered(settings.USER_LOGIN)


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.tag('API')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя через API')
def test_login_through_api(api_token):
    index.open_main_page()
    with allure.step('Добавляем токен авторизации в cookie браузера'):
        browser.driver.add_cookie(
            {'name': 'tokenp_', 'value': api_token}
        )
    index.open_main_page()

    index.should_have_registered(settings.USER_LOGIN)
