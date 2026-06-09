from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from test_data import BASE_URL

class RegisterPage(BasePage):
    URL = f"{BASE_URL}/signup"

    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//form//button")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    def open(self):
        self.driver.get(self.URL)

    def fill_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def fill_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def fill_first_name(self, first_name):
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name):
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def fill_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def register(self, email, username, first_name, last_name, password):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_username(username)
        self.fill_email(email)
        self.fill_password(password)
        self.submit()

    def accept_registration_alert(self):
        try:
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

    def is_login_page_opened(self):
        self.wait_for_url_contains("signin")
        return "signin" in self.driver.current_url

    def is_login_form_visible(self):
        try:
            element = self.find(self.LOGIN_PASSWORD_INPUT)
            return element.is_displayed()
        except Exception:
            return False
