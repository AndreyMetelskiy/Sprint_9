import allure

from pages.register_page import RegisterPage
from helpers import get_unique_user


@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Успешное создание аккаунта")
    def test_create_account(self, driver):
        register_page = RegisterPage(driver)
        user = get_unique_user()

        with allure.step("Открыть страницу регистрации"):
            register_page.open()

        with allure.step("Заполнить все поля формы регистрации и нажать кнопку"):
            register_page.register(
                email=user["email"],
                username=user["username"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                password=user["password"]
            )
            register_page.accept_alert(timeout=3)

        with allure.step("Проверить переход на страницу авторизации и отображение формы"):
            assert register_page.is_login_page_opened(), "Переход на страницу /signin не произошел"
            assert register_page.is_login_form_visible(), "Форма авторизации не отображается"
