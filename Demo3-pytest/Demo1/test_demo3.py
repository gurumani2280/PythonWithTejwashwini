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


@pytest.mark.smoke
def test_demo1(driver_init):
    driver.get("https://drive.google.com/drive/folders/1_n6sPEMPd5I_wP4PYxuJxCwO7YmJR2qO")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)
