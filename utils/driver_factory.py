from selenium import webdriver

def get_driver():
    # For now only Chrome, but can extend later
    return webdriver.Chrome()
