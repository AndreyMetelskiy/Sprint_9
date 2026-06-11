import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.main_page import MainPage
from helpers import get_unique_user


@pytest.fixture(scope="function")
def driver():
    if os.getenv('CI') == 'true' or os.path.exists('/.dockerenv'):
        selenoid_options = Options()
        selenoid_options.add_argument("--window-size=1920,1080")
        selenoid_options.add_argument("--log-level=3")
        selenoid_options.set_capability("browserName", "chrome")
        selenoid_options.set_capability("browserVersion", "128.0")
        selenoid_options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        browser = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            options=selenoid_options
        )
    else:
        local_options = Options()
        local_options.add_argument("--window-size=1920,1080")
        local_options.add_argument("--log-level=3")
        local_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=local_options)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def registered_user(driver):
    user = get_unique_user()
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register(
        user["email"],
        user["username"],
        user["first_name"],
        user["last_name"],
        user["password"],
    )
    return user


@pytest.fixture(scope="function")
def authorized_driver(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(registered_user["username"], registered_user["password"])
    assert MainPage(driver).is_logout_button_visible(), "Авторизация не прошла: кнопка 'Выход' не отображается"
    yield driver
