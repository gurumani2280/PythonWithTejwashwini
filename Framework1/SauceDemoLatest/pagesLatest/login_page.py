from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SauceDemoLatest.pagesLatest.login_page_locators import LoginPageLocators
from SauceDemoLatest.utilities.selenium_utility import SeleniumUtility


class LoginPage(LoginPageLocators) :

    def __init__(self,driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(*LoginPage.username_field)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password_field)

    def get_login(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_saucelogo(self):
        return  self.driver.find_element(*LoginPage.sauce_logo)

    # def waitforlogtobedisplayed(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.visibility_of(self.get_saucelogo()))
    #     assert self.get_saucelogo().is_displayed(), "sauce logo is not displayed"

    def wait_for_logo_to_display(self):
        SeleniumUtility.wait_for_elememt_to_be_displayed(self.driver,self.get_saucelogo(),15)


    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()
