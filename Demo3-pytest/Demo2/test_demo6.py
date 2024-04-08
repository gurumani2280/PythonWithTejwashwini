import pytest
from selenium import webdriver
import time



@pytest.mark.smoke
def test_demo6(driver):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)

@pytest.mark.smoke
def test_demo6A(driver):
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)
    