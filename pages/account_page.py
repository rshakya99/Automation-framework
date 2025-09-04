import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AccountPage(BasePage):
    URL = "https://practice.automationtesting.in/my-account/edit-address/billing/"

    # Billing locators using XPath
    BILLING_EDIT="// h3[text() = 'Billing Address'] / following - sibling::a[text() = 'Edit']"
    BILLING_FIRSTNAME = (By.XPATH, "//input[@id='billing_first_name']")
    BILLING_LASTNAME = (By.XPATH, "//input[@id='billing_last_name']")
    BILLING_COMPANY = (By.XPATH, "//input[@id='billing_company']")
    BILLING_ADDRESS = (By.XPATH, "//input[@id='billing_address_1']")
    BILLING_APARTMENT = (By.XPATH, "//input[@id='billing_address_2']")
    BILLING_CITY = (By.XPATH, "//input[@id='billing_city']")
    BILLING_STATE = (By.XPATH, "//select[@id='billing_state']")
    BILLING_POSTCODE = (By.XPATH, "//input[@id='billing_postcode']")
    BILLING_PHONE = (By.XPATH, "//input[@id='billing_phone']")
    SAVE_BTN = (By.XPATH, "//*[@name='save_address']")
    SUCCESS_MSG = (By.XPATH, "//div[@class='woocommerce-message']")

    def open(self):
        self.driver.get(self.URL)

    def add_billing_address(self, first_name, last_name, company, address, apartment, city, state, postcode, phone):
        """Fill billing form and save"""
        #self.click(self.BILLING_EDIT)
        self.type(self.BILLING_FIRSTNAME, first_name)
        self.type(self.BILLING_LASTNAME, last_name)
        self.type(self.BILLING_COMPANY, company)
        self.type(self.BILLING_PHONE, phone)
        self.type(self.BILLING_ADDRESS, address)
        self.type(self.BILLING_APARTMENT, apartment)
        self.type(self.BILLING_CITY, city)
        # Select state from dropdown
        time.sleep(5)
        Select(self.driver.find_element(*self.BILLING_STATE)).select_by_visible_text(state)
        self.type(self.BILLING_POSTCODE, postcode)
        self.click(self.SAVE_BTN)
        time.sleep(5)

    def is_address_saved(self):
        """Check if success message is visible after saving address"""
        return self.is_visible(self.SUCCESS_MSG)

