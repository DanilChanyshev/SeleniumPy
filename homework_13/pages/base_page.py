from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def open(self, endpoint = "/"):
        self.driver.get(f"{self.BASE_URL}{endpoint}")

    def css(self, locator) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def lcss(self, locator) -> WebElement:
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def xpath(self, locator) -> WebElement:
        return self.driver.find_element(By.XPATH, locator)

    def lxpath(self, locator) -> WebElement:
        return self.driver.find_elements(By.XPATH, locator)

    def refresh(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()
        self.driver.set_page_load_timeout(5)

    def wait_until(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )
