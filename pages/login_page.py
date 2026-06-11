from pages.base_page import BasePage
from locators.login_page import LoginLocators
from config import LOGIN_URL


class LoginPage(BasePage):
    URL = LOGIN_URL

    def open(self):
        self.open_url(self.URL)
        self.accept_alert(timeout=3)
        self.find_visible(LoginLocators.LOGIN_FORM)

    def fill_email(self, email):
        self.type_text(LoginLocators.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.type_text(LoginLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(LoginLocators.SUBMIT_BUTTON)

    def login(self, username, password):
        self.find_visible(LoginLocators.LOGIN_FORM)
        self.fill_email(username)
        self._trigger_react_input(self.find(LoginLocators.EMAIL_INPUT))
        self.fill_password(password)
        self._trigger_react_input(self.find(LoginLocators.PASSWORD_INPUT))
        self.submit()
        # Если после сабмита появился алерт — принимаем и повторяем логин
        if self.accept_alert(timeout=5):
            self.fill_email(username)
            self._trigger_react_input(self.find(LoginLocators.EMAIL_INPUT))
            self.fill_password(password)
            self._trigger_react_input(self.find(LoginLocators.PASSWORD_INPUT))
            self.submit()

    def is_login_form_visible(self):
        return self.is_element_visible(LoginLocators.LOGIN_FORM)

    def go_to_register(self):
        self.click(LoginLocators.REGISTER_LINK)
