from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from test_data import BASE_URL
class LoginPage(BasePage):
    URL = f"{BASE_URL}/signin"

    EMAIL_INPUT = (By.XPATH, "//input[@name='email']") 
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//form//button")
    SUBMIT_BUTTON_DISABLED = (By.XPATH, "//form//button[@disabled]")
    LOGIN_FORM = (By.XPATH, "//h1[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(@href, '/signup')]")

    def open(self):
        self.driver.get(self.URL)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception:
            pass
        self.find_visible(self.LOGIN_FORM)

    def fill_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def login(self, username, password):
        self.find_visible(self.LOGIN_FORM)
        self.fill_email(username)
        self._trigger_react_input(self.find(self.EMAIL_INPUT))
        self.fill_password(password)
        self._trigger_react_input(self.find(self.PASSWORD_INPUT))
        self.submit()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception:
            return     
        self.fill_email(username)
        self._trigger_react_input(self.find(self.EMAIL_INPUT))
        self.fill_password(password)
        self._trigger_react_input(self.find(self.PASSWORD_INPUT))
        self.submit()

    def is_login_form_visible(self):
        return self.is_element_visible(self.LOGIN_FORM)

    def go_to_register(self):
        self.click(self.REGISTER_LINK)
