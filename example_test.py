from selenium import webdriver
from selenium.webdriver.common.by import By

def test_run_example():
    browser = webdriver.Firefox()
    browser.get("https://browserstack.com")