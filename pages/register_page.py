from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    URL = "https://practice.automationtesting.in/my-account/"

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_MSG = (By.CSS_SELECTOR, "ul.woocommerce-error")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def open(self):
        super().open(self.URL)

    def register(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.REGISTER_BTN)

    def is_registration_successful(self):
        return self.is_visible(self.LOGOUT_LINK)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MSG)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return "⚠️ No error message found"
