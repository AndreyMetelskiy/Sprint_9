
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.find_clickable(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def wait_for_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    def wait_for_url_changes(self, current_url):
        self.wait.until(EC.url_changes(current_url))

    def get_current_url(self):
        return self.driver.current_url

    def is_element_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False
        
    def _trigger_react_input(self, element):
        """Базовый метод для уведомления React об изменении текстового поля"""
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", 
            element
        )
