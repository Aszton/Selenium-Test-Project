import time
import pytest
from page_object_pattern.Pages.login_page import LoginPage
from page_object_pattern.Pages.navigation_page import NavigationPage


@pytest.mark.usefixtures('setup')
class TestPageFeature:


    def test_login_with_valid_creditentials(self):
        navigation_page = NavigationPage(self.driver)
        correct_login = LoginPage(self.driver)

        navigation_page.open_homepage()
        navigation_page.click_login_or_register_button()
        correct_login.enter_user_name("AshtonScalac")
        correct_login.enter_password("test1234")
        correct_login.click_on_login_button()
        correct_login.is_user_login_correctly()

    def test_login_with_invalid_creditentials(self):
        navigation_page = NavigationPage(self.driver)
        incorrect_login = LoginPage(self.driver)

        navigation_page.open_homepage()
        navigation_page.click_login_or_register_button()
        incorrect_login.enter_user_name("Ashton")
        incorrect_login.enter_password("password")
        incorrect_login.click_on_login_button()
        incorrect_login.login_error_message()