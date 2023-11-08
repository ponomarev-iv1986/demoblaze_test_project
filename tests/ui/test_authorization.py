import allure
from allure_commons.types import Severity
from selene import browser

from config import settings
from demoblaze_test_project.pages.login_form import LoginForm
from demoblaze_test_project.pages.main_page import MainPage

main_page = MainPage()
login_form = LoginForm()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя')
def test_login():
    main_page.open_main_page()

    main_page.open_login_window()
    login_form.fill_user()
    login_form.click_login()

    main_page.should_have_registered(settings.USER_LOGIN)


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.tag('API')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя через API')
def test_login_through_api(api_token):
    main_page.open_main_page()
    main_page.token_to_cookie(api_token)
    main_page.open_main_page()

    main_page.should_have_registered(settings.USER_LOGIN)
