from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class LoginLocators(BaseLocators):
    SUBMIT_BUTTON_DISABLED = (By.XPATH, "//form//button[@disabled]")
    LOGIN_FORM = (By.XPATH, "//h1[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(@href, '/signup')]")
