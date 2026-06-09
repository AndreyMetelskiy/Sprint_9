from pathlib import Path
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from test_data import BASE_URL

APP_DIR = Path(__file__).parent.parent
class CreateRecipePage(BasePage):
    URL = f"{BASE_URL}/recipes/create"

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

    def open(self):
        self.driver.get(self.URL)
        self.find_visible(self.PAGE_TITLE)

    def fill_name(self, name):
        self.type_text(self.NAME_INPUT, name)
        self._trigger_react_input(self.find(self.NAME_INPUT))

    def fill_description(self, description_text):
        self.type_text(self.DESCRIPTION_INPUT, description_text)
        self._trigger_react_input(self.find(self.DESCRIPTION_INPUT))

    def fill_cooking_time(self, time_val):
        self.type_text(self.COOKING_TIME_INPUT, str(time_val))
        self._trigger_react_input(self.find(self.COOKING_TIME_INPUT))

    def add_ingredient(self, ingredient_name, amount="100"):
        self.type_text(self.INGREDIENT_NAME_INPUT, ingredient_name)
        self._trigger_react_input(self.find(self.INGREDIENT_NAME_INPUT))
        dropdown_item = (By.XPATH, f"//div[contains(text(),'{ingredient_name}')]")
        self.click(dropdown_item)
        self.type_text(self.INGREDIENT_AMOUNT_INPUT, str(amount))
        self._trigger_react_input(self.find(self.INGREDIENT_AMOUNT_INPUT))
        self.click(self.INGREDIENT_ADD_BUTTON)

    def upload_image(self, filename):
        image_path = str(APP_DIR / "assets" / filename)
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Тестовый файл не найден: {image_path}")    
        input_element = self.find(self.IMAGE_INPUT)
        input_element.send_keys(image_path)
        self._trigger_react_input(input_element)

    def submit(self):
        submit_btn = self.find(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        self.click(self.SUBMIT_BUTTON)

    def create_new_recipe(self, filename, name, description, ingredient, amount, cooking_time):
        self.fill_name(name)
        self.click(self.ORANGE_BUTTON)
        self.add_ingredient(ingredient, amount)
        self.fill_cooking_time(cooking_time)
        self.fill_description(description)
        self.upload_image(filename)
        self.submit()

    def is_recipe_title_visible(self, recipe_name):
        recipe_title_locator = (By.XPATH, f"//h1[contains(@class, 'styles_single-card__title') and contains(text(), '{recipe_name}')]")
        return self.is_element_visible(recipe_title_locator)