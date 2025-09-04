from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    URL = "https://practice.automationtesting.in/"

    SHOP_LINK = (By.LINK_TEXT, "Shop")
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My Account")

    def open(self):
        self.driver.get(self.URL)

    def go_to_shop(self):
        self.click(self.SHOP_LINK)

    def go_to_my_account(self):
        self.click(self.MY_ACCOUNT_LINK)
