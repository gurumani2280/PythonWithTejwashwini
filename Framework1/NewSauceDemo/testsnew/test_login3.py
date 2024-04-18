import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from saucedemo.pages.login_page import LoginPage


@pytest.mark.usefixtures("initialisation")
class TestLogin3:
    @pytest.mark.loginparam
    def test_login3(self):
        lp = LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")




