import time

from selenium.webdriver.common.by import By


class NavigationPage:

    def __init__(self, driver):
        self.driver = driver
        self.loginRegister = "customernav"
        self.login_input = "loginname"

    def open_homepage(self):
        self.driver.get('https://automationteststore.com/')
        assert "A place to practice your automation skills!" in self.driver.title

    def click_login_or_register_button(self):
        self.driver.find_element(By.ID, self.loginRegister).click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.NAME, self.login_input)
