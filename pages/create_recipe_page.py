from pathlib import Path

from pages.base_page import BasePage
from locators.create_recipe_page import CreateRecipeLocators
from config import CREATE_RECIPE_URL

APP_DIR = Path(__file__).parent.parent


class CreateRecipePage(BasePage):
    URL = CREATE_RECIPE_URL

    def open(self):
        self.open_url(self.URL)
        self.find_visible(CreateRecipeLocators.PAGE_TITLE)

    def fill_name(self, name):
        self.type_text(CreateRecipeLocators.NAME_INPUT, name)
        self._trigger_react_input(self.find(CreateRecipeLocators.NAME_INPUT))

    def fill_description(self, description_text):
        self.type_text(CreateRecipeLocators.DESCRIPTION_INPUT, description_text)
        self._trigger_react_input(self.find(CreateRecipeLocators.DESCRIPTION_INPUT))

    def fill_cooking_time(self, time_val):
        self.type_text(CreateRecipeLocators.COOKING_TIME_INPUT, str(time_val))
        self._trigger_react_input(self.find(CreateRecipeLocators.COOKING_TIME_INPUT))

    def add_ingredient(self, ingredient_name, amount="100"):
        self.type_text(CreateRecipeLocators.INGREDIENT_NAME_INPUT, ingredient_name)
        self._trigger_react_input(self.find(CreateRecipeLocators.INGREDIENT_NAME_INPUT))
        self.click(CreateRecipeLocators.ingredient_dropdown_item(ingredient_name))
        self.type_text(CreateRecipeLocators.INGREDIENT_AMOUNT_INPUT, str(amount))
        self._trigger_react_input(self.find(CreateRecipeLocators.INGREDIENT_AMOUNT_INPUT))
        self.click(CreateRecipeLocators.INGREDIENT_ADD_BUTTON)

    def upload_image(self, filename):
        image_path = str(APP_DIR / "assets" / filename)
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Тестовый файл не найден: {image_path}")
        input_element = self.find(CreateRecipeLocators.IMAGE_INPUT)
        input_element.send_keys(image_path)
        self._trigger_react_input(input_element)

    def submit(self):
        submit_btn = self.find_visible(CreateRecipeLocators.SUBMIT_BUTTON)
        self.scroll_into_view(submit_btn)
        self.action_click_element(submit_btn)

    def create_new_recipe(self, filename, name, description, ingredient, amount, cooking_time):
        self.fill_name(name)
        self.click(CreateRecipeLocators.ORANGE_BUTTON)
        self.add_ingredient(ingredient, amount)
        self.fill_cooking_time(cooking_time)
        self.fill_description(description)
        self.upload_image(filename)
        self.submit()

    def is_recipe_title_visible(self, recipe_name):
        return self.is_element_visible(CreateRecipeLocators.recipe_title(recipe_name))
