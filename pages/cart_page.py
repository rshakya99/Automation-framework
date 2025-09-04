from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    URL = "https://practice.automationtesting.in/basket/"

    CART_ITEM = (By.CSS_SELECTOR, "td.product-name")
    REMOVE_BTN = (By.CSS_SELECTOR, "a.remove")
    EMPTY_MSG = (By.CSS_SELECTOR, "p.cart-empty")

    def open(self):
        self.driver.get(self.URL)

    def get_cart_items(self):
        """Return list of product names in the cart."""
        return [e.text for e in self.driver.find_elements(*self.CART_ITEM)]

    def remove_item(self):
        """Remove first item from cart and wait until removed."""
        self.click(self.REMOVE_BTN)
        # Wait until cart shows empty message
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMPTY_MSG)
        )

    def is_cart_empty(self):
        """Return True if cart is empty."""
        return self.is_visible(self.EMPTY_MSG)

    def is_product_in_cart(self, product_name=None):
        """Return True if cart has at least one product or a specific product."""
        items = self.get_cart_items()
        if product_name:
            return product_name in items
        return len(items) > 0
