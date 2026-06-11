from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def action_click(self, locator):
        """Клик через ActionChains — двигает мышь к элементу и кликает,
        максимально близко к реальному пользователю."""
        element = self.find_visible(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def action_click_element(self, element):
        """ActionChains-клик по уже найденному WebElement, без повторного поиска."""
        ActionChains(self.driver).move_to_element(element).click().perform()

    def type_text(self, locator, text):
        element = self.find_clickable(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def accept_alert(self, timeout=3):
        """Принимает алерт, если он появился. Возвращает True если алерт был, False если нет."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            return True
        except Exception:
            return False

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
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));",
            element
        )
