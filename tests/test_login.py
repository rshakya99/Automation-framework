import allure
from pages.login_page import LoginPage

@allure.feature("User Login")
@allure.story("Valid Login")
def test_valid_login(driver):
    page = LoginPage(driver)
    with allure.step("Open login page"):
        page.open()
    with allure.step("Login with valid credentials"):
        page.login("test45@yopmail.com", "V9!mQ7$rLp2@tX")
    with allure.step("Verify login success"):
        assert page.is_login_successful()

@allure.feature("User Login")
@allure.story("Invalid Login")
def test_invalid_login(driver):
    page = LoginPage(driver)
    with allure.step("Open login page"):
        page.open()
    with allure.step("Login with invalid credentials"):
        page.login("wrong@yopmail.com", "WrongPass")
    with allure.step("Verify error message is displayed"):
        assert page.is_error_displayed()
