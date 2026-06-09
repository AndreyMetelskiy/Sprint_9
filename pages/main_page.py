from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from test_data import BASE_URL
class MainPage(BasePage):
    URL = BASE_URL

    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[contains(@href, '/recipes/create')]")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'recipe-card')]")
    RECIPE_TITLE = (By.XPATH, "//h2[contains(@class, 'recipe-card__title')]")

    def open(self):
        self.driver.get(self.URL)

    def is_logout_button_visible(self):
        return self.is_element_visible(self.LOGOUT_BUTTON)

    def go_to_create_recipe(self):
        self.click(self.CREATE_RECIPE_LINK)

    def get_recipe_card_title(self, title):
        locator = (By.XPATH, f"//h2[contains(@class, 'recipe-card__title') and contains(text(), '{title}')]")
        return self.is_element_visible(locator)
    
    def is_main_page_opened(self):
        try:
            self.wait_for_url_contains("/")
        except Exception:
            pass
        return "signin" not in self.get_current_url()
