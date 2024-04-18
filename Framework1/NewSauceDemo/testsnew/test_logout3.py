import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from NewSauceDemo.pagesnew.home_page import HomePage
from NewSauceDemo.pagesnew.login_page import LoginPage


@pytest.mark.usefixtures("initialisation")
class TestLogout3:
    @pytest.mark.loginparam
    def test_logout3(self):
        lp = LoginPage(self.driver)
        lp.login("standard_user", "secret_sauce")
        hp = HomePage(self.driver)
        hp.logout()
        lp.waitforlogtobedisplayed()

