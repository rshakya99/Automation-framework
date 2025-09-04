import time, random
import allure
from pages.register_page import RegisterPage

@allure.feature("User Registration")
@allure.story("Register with new user")
def test_register_new_user(driver):
    page = RegisterPage(driver)
    with allure.step("Open registration page"):
        page.open()
    with allure.step("Register with unique email"):
        unique_email = f"user_{random.randint(1,1000)}@yopmail.com"
        page.register(unique_email, "V9!mQ7$rLp2@tX")
    with allure.step("Verify registration success"):
        assert page.is_registration_successful()

@allure.feature("User Registration")
@allure.story("Register with existing email")
def test_register_with_existing_email(driver):
    page = RegisterPage(driver)
    with allure.step("Open registration page"):
        page.open()
    with allure.step("Try to register with existing email"):
        page.register("test45@yopmail.com", "V9!mQ7$rLp2@tX")
    with allure.step("Verify error message is displayed"):
        assert page.is_error_displayed()
