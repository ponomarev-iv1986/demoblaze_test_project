import allure

from config import settings
from demoblaze_test_project.pages.index import Index
from demoblaze_test_project.pages.login_form import LoginForm

index = Index()
login_form = LoginForm()


def test_login():
    index.open()

    index.open_login_window()
    with allure.step('Заполняем данные пользователя'):
        login_form.fill_user(settings.USER_LOGIN, settings.USER_PASSWORD)
    with allure.step('Нажимаем кнопку "Log in"'):
        login_form.click_login()

    index.should_have_registered(settings.USER_LOGIN)
