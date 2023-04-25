import pytest
from src.page.home_page import HomePage


@pytest.mark.usefixtures('driver')
class TestLogin:
    def test_invalid_login(self, driver):
        home_page = HomePage(driver).access_page()
        login_page = home_page.access_login()
        invalid_login_message = login_page.perform_login("a@a.com", "testing").invalid_login_is_displayed()
        assert invalid_login_message is True
