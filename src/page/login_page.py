from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class LoginPage(BasePage):
    email_input = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    password_input = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    login_button = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    invalid_login_message = (By.XPATH, '//p[contains(text(), "Your email or password is incorrect")]')

    def fill_email(self, email):
        self.write(self.email_input, text=email)
        return self

    def fill_password(self, password):
        self.write(self.password_input, text=password)
        return self

    def perform_login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click(self.login_button)
        return self

    def invalid_login_is_displayed(self):
        return self.driver.find_element(*self.invalid_login_message).is_displayed()
