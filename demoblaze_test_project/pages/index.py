import allure
from selene import browser, have


class Index:
    @allure.step('Открываем главную страницу')
    def open(self):
        browser.open('/')

    @allure.step('Открываем окно авторизации')
    def open_login_window(self):
        browser.element('#login2').click()

    @allure.step('Проверяем регистрацию пользователя')
    def should_have_registered(self, username):
        browser.element('#nameofuser').should(
            have.exact_text(f'Welcome {username}')
        )
