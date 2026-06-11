from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[contains(@href, '/recipes/create')]")

    @staticmethod
    def recipe_card_title(title):
        return (By.XPATH, f"//h2[contains(@class, 'recipe-card__title') and contains(text(), '{title}')]")
