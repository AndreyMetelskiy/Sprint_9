import allure
from pages.create_recipe_page import CreateRecipePage
from test_data import RECIPE


@allure.feature("Создание рецепта")
class TestCreateRecipe:

    @allure.title("Успешное создание рецепта")
    @allure.description("Авторизованный пользователь заполняет форму и создаёт рецепт")
    def test_create_recipe_card_is_displayed(self, authorized_driver):
        create_page = CreateRecipePage(authorized_driver)

        with allure.step("Перейти на страницу создания рецепта"):
            create_page.open()

        with allure.step("Заполнить форму и отправить рецепт"):
            create_page.create_new_recipe(
                filename="test_image.jpg",
                name=RECIPE["name"],
                description=RECIPE.get("description", "Смешать ингредиенты и запекать."),
                ingredient=RECIPE["ingredient"],
                amount=RECIPE["ingredient_amount"],
                cooking_time=RECIPE["cooking_time"]
            )
        with allure.step("Проверить отображение карточки рецепта с названием"):
            assert create_page.is_recipe_title_visible(RECIPE["name"])
