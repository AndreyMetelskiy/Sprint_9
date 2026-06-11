from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class RegisterLocators(BaseLocators):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
