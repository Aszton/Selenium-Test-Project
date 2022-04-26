import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_input = "loginname"
        self.password_input = "password"
        self.login_button = "button.btn:nth-child(7)"
        self.error_incorrect_login = "alert-danger"
        self.logged_user = "maintext"

    def enter_user_name(self, user_name):
        self.driver.find_element(By.NAME, self.login_input).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_input).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

    def login_error_message(self):
        assert self.driver.find_element(By.CLASS_NAME, self.error_incorrect_login)

    def is_user_login_correctly(self):
        assert self.driver.find_element(By.CLASS_NAME, self.logged_user)
