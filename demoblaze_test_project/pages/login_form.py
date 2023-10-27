from selene import browser


class LoginForm:
    def fill_user(self, username, password):
        browser.element('#loginusername').type(username)
        browser.element('#loginpassword').type(password)

    def click_login(self):
        browser.element('[onclick="logIn()"]').click()
