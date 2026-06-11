from pages.base_page import BasePage
from locators.main_page import MainPageLocators
from config import MAIN_URL


class MainPage(BasePage):
    URL = MAIN_URL

    def open(self):
        self.open_url(self.URL)

    def is_logout_button_visible(self):
        return self.is_element_visible(MainPageLocators.LOGOUT_BUTTON)

    def go_to_create_recipe(self):
        self.click(MainPageLocators.CREATE_RECIPE_LINK)

    def get_recipe_card_title(self, title):
        return self.is_element_visible(MainPageLocators.recipe_card_title(title))

    def is_main_page_opened(self):
        return "signin" not in self.get_current_url()
