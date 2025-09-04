import time

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator, retries=3):
        """Click element with retry if intercepted"""
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except ElementClickInterceptedException:
                time.sleep(1)
        raise TimeoutException(f"Could not click element {locator}")

    def type(self, locator, text):
        """Type into input field after clearing"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element_text = element.text.strip()
            message = f"[PASS] Element {locator} is visible with text: '{element_text}'"
            print(message)
            allure.attach(message, name="Visibility Check", attachment_type=allure.attachment_type.TEXT)
            return True
        except TimeoutException:
            message = f"[FAIL] Element {locator} is NOT visible within {timeout} seconds."
            print(message)
            allure.attach(message, name="Visibility Check", attachment_type=allure.attachment_type.TEXT)
            return False