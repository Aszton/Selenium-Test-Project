import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_input = "loginname"
        self.password_input = "password"
        self.login_button = "button.btn:nth-child(7)"
        self.error_incorrect_login = "alert-danger"
        self.logged_user = "maintext"

    def enter_user_name(self, user_name):
        self.driver.find_element_by_name(self.login_input).send_keys(user_name)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_input).send_keys(password)
        time.sleep(1)

    def click_on_login_button(self):
        self.driver.find_element_by_css_selector(self.login_button).click()
        time.sleep(1)

    def login_error_message(self):
        assert self.driver.find_element_by_class_name(self.error_incorrect_login)

    def is_user_login_correctly(self):
        assert self.driver.find_element_by_class_name(self.logged_user)