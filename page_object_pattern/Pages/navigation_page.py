import time


class NavigationPage:

    def __init__(self, driver):
        self.driver = driver
        self.loginRegister = "customernav"

    def open_homepage(self):
        self.driver.get('https://automationteststore.com/')
        time.sleep(1)

    def click_login_or_register_button(self):
        self.driver.find_element_by_id(self.loginRegister).click()