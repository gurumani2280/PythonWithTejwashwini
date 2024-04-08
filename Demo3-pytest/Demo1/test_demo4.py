import pytest
from selenium import webdriver
import time
@pytest.fixture()
def driver():
    print("First program")
    driver = webdriver.Chrome()
    yield driver                           # yield will run after the execution of test method
    print("closing the chrome browser")
    driver.quit()


@pytest.mark.smoke
def test_demo1(driver):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)
    