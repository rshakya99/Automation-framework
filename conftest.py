# conftest.py
import datetime
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture(scope="function")
def driver():
    # Setup ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot if test fails and attach to Allure report."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Create local screenshot folder
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Build filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = "{}_{}.png".format(item.name, timestamp)
            destination = os.path.join(screenshots_dir, file_name)

            # Save screenshot locally
            driver.save_screenshot(destination)
            print("Screenshot saved to {}".format(destination))

            # Attach screenshot to Allure report
            with open(destination, "rb") as f:
                allure.attach(f.read(),
                              name="Screenshot_{}".format(item.name),
                              attachment_type=allure.attachment_type.PNG)
