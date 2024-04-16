import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from saucedemo.pages.login_page import LoginPage


@pytest.mark.usefixtures("initialisation")
class TestLogin3:
    @pytest.mark.login1
    def test_login3(self):
        lp = LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")

        # self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        # self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        # self.driver.find_element(By.ID, "login-button").click()


