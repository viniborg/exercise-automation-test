from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_presence_of_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(expected_conditions.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_presence_of_element(locator)
        element.click()

    def write(self, locator, text):
        element = self.wait_presence_of_element(locator)
        element.send_keys(text)
