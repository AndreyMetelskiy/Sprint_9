from pages.base_page import BasePage
from locators.register_page import RegisterLocators
from config import REGISTER_URL


class RegisterPage(BasePage):
    URL = REGISTER_URL

    def open(self):
        self.open_url(self.URL)

    def fill_email(self, email):
        self.type_text(RegisterLocators.EMAIL_INPUT, email)

    def fill_username(self, username):
        self.type_text(RegisterLocators.USERNAME_INPUT, username)

    def fill_first_name(self, first_name):
        self.type_text(RegisterLocators.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name):
        self.type_text(RegisterLocators.LAST_NAME_INPUT, last_name)

    def fill_password(self, password):
        self.type_text(RegisterLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(RegisterLocators.SUBMIT_BUTTON)

    def register(self, email, username, first_name, last_name, password):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_username(username)
        self.fill_email(email)
        self.fill_password(password)
        self.submit()

    def is_login_page_opened(self):
        self.wait_for_url_contains("signin")
        return "signin" in self.get_current_url()

    def is_login_form_visible(self):
        try:
            element = self.find(RegisterLocators.PASSWORD_INPUT)
            return element.is_displayed()
        except Exception:
            return False
