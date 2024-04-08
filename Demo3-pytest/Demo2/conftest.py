import pytest
from selenium import webdriver
import time
@pytest.fixture()
def driver_init():
    print("First program")
    global driver
    driver = webdriver.Chrome()
    yield                           # yield will run after the execution of test method
    print("closing the chrome browser")
    driver.quit()

@pytest.fixture(scope="package")
def driver():
    print("First program")
    driver = webdriver.Chrome()
    yield driver                           # yield will run after the execution of test method
    print("closing the chrome browser")
    driver.quit()