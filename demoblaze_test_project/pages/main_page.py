import allure
from selene import be, browser, have


class MainPage:
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('/')

    @allure.step('Открываем окно авторизации')
    def open_login_window(self):
        browser.element('#login2').with_(click_by_js=True).click()

    @allure.step('Кликаем на кнопку Phones')
    def click_phones(self):
        browser.all('.list-group>a').element_by(have.text('Phone')).click()

    @allure.step('Кликаем на кнопку Laptops')
    def click_laptops(self):
        browser.all('.list-group>a').element_by(have.text('Laptops')).click()

    @allure.step('Кликаем на кнопку Monitors')
    def click_monitors(self):
        browser.all('.list-group>a').element_by(have.text('Monitors')).click()

    @allure.step('Добавляем токен авторизации в cookie браузера')
    def token_to_cookie(self, token):
        browser.driver.add_cookie(
            {'name': 'tokenp_', 'value': token}
        )

    @allure.step('Проверяем регистрацию пользователя')
    def should_have_registered(self, username):
        browser.element('#nameofuser').should(
            have.exact_text(f'Welcome {username}')
        )

    @allure.step('Проверяем лейбл')
    def should_label_be_clickable_and_have_text(self):
        browser.element('nav #nava').should(be.clickable)
        browser.element('nav #nava').should(have.text('PRODUCT STORE'))

    @allure.step('Проверяем панель навигации')
    def should_be_navbar_example(self):
        browser.all('[id=navbarExample] li').should(
            have.exact_texts(
                'Home\n(current)',
                'Contact',
                'About us',
                'Cart',
                'Log in',
                '',
                '',
                'Sign up'
            )
        )

    @allure.step('Проверяем надпись CATEGORIES')
    def should_categories_be_clickable(self):
        browser.element('.list-group #cat').should(
            have.exact_text('CATEGORIES')
        )
        browser.element('.list-group #cat').should(be.clickable)

    @allure.step('Проверяем что "{value}" есть в списке')
    def should_have_gadget(self, value):
        browser.element('#tbodyid').should(have.text(value))

    @allure.step('Проверяем подвал сайта')
    def should_footer_have_text(self):
        browser.all('div#footc h4').should(
            have.exact_texts(
                'About Us',
                'Get in Touch',
                'PRODUCT STORE'
            )
        )
        browser.all('div#footc p').should(
            have.exact_texts(
                ('We believe performance needs to be validated'
                 ' at every stage of the software development cycle'
                 ' and our open source compatible, massively scalable'
                 ' platform makes that a reality.'),
                'Address: 2390 El Camino Real',
                'Phone: +440 123456',
                'Email: demo@blazemeter.com'
            )
        )
