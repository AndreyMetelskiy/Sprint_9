from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    NAME_INPUT = (By.XPATH, "(//input[contains(@class,'inputField') and not(contains(@class,'ingredi'))])[1]")
    COOKING_TIME_INPUT = (By.XPATH, "(//input[contains(@class,'inputField') and not(contains(@class,'ingredi'))])[2]")
    DESCRIPTION_INPUT = (By.XPATH, "//*[contains(text(), 'Описание рецепта')]/following-sibling::textarea | //textarea")
    INGREDIENT_NAME_INPUT = (By.XPATH, "(//input[contains(@class,'ingredi')])[1]")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "(//input[contains(@class,'ingredi')])[2]")
    INGREDIENT_ADD_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    IMAGE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    ORANGE_BUTTON = (By.XPATH, "//button[@type='button' and @style='background-color: orange;']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'dark-blue') or contains(text(), 'Создать')]")
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Создание')]")

    @staticmethod
    def ingredient_dropdown_item(ingredient_name):
        return (By.XPATH, f"//div[contains(text(),'{ingredient_name}')]")

    @staticmethod
    def recipe_title(recipe_name):
        return (By.XPATH, f"//h1[contains(@class, 'styles_single-card__title') and contains(text(), '{recipe_name}')]")
