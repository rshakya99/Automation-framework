import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ShopPage(BasePage):
    URL = "https://practice.automationtesting.in/shop/"

    PRODUCT = (By.CSS_SELECTOR, ".products li a.button")  # first product add button
    VIEW_CART = (By.LINK_TEXT, "Cart")

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def add_first_product_to_cart(self):
        self.click(self.PRODUCT)
        time.sleep(2)

    def go_to_cart(self):
        self.click(self.VIEW_CART)
