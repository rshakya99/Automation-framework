import allure
from pages.account_page import AccountPage
from pages.login_page import LoginPage

@allure.feature("User Account")
@allure.story("Add Billing Address")
def test_add_billing_address(driver):
    login_page = LoginPage(driver)
    account_page = AccountPage(driver)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid credentials"):
        login_page.login("test46@yopmail.com", "V9!mQ7$rLp2@tX")

    with allure.step("Open account billing address page"):
        account_page.open()

    with allure.step("Add billing address"):
        account_page.add_billing_address(
            first_name="John",
            last_name="Doe",
            company="Test Pvt Ltd",
            address="123 Test Street",
            apartment="Apt 101",
            city="Hyderabad",
            state="Telangana",
            postcode="500081",
            phone="9876543210"
        )

    with allure.step("Verify billing address is saved"):
        assert account_page.is_address_saved(), "Billing address was not saved successfully"
