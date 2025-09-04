from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    URL = "https://practice.automationtesting.in/my-account/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "login")
    ERROR_MSG = (By.CSS_SELECTOR, "ul.woocommerce-error li")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_login_successful(self):
        return self.is_visible(self.LOGOUT_LINK)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MSG)
