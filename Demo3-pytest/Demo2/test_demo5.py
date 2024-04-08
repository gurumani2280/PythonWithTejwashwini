import pytest
from selenium import webdriver
import time



@pytest.mark.smoke
def test_demo5(driver):
    driver.get("https://drive.google.com/drive/folders/1_n6sPEMPd5I_wP4PYxuJxCwO7YmJR2qO")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)

@pytest.mark.smoke
def test_demo5A(driver):
    driver.get("https://www.orangehrm.com/")
    driver.maximize_window()
    print("Launching the URL and maximised the browser")
    time.sleep(1)
