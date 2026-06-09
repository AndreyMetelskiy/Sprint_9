import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешная авторизация пользователя")
    def test_successful_login(self, driver, registered_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        with allure.step("Открыть страницу авторизации"):
            login_page.open()

        with allure.step("Заполнитель все поля формы авторизации и нажать кнопку 'Войти'"):
            login_page.login(registered_user["username"], registered_user["password"])

        with allure.step("Проверить переход на главную страницу"):
            assert "signin" not in driver.current_url, "Пользователь остался на странице авторизации"

        with allure.step("Проверить отображение кнопки 'Выход'"):
            assert main_page.is_logout_button_visible(), "Кнопка 'Выход' не отображается"