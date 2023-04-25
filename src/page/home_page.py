from selenium.webdriver.common.by import By
from src.core.base_page import BasePage
from src.page.login_page import LoginPage


class HomePage(BasePage):
    login_button = (By.CSS_SELECTOR, 'a[href="/login"]')

    def access_page(self):
        self.driver.get('https://automationexercise.com/')
        return self

    def access_login(self):
        self.click(self.login_button)
        return LoginPage(self.driver)
