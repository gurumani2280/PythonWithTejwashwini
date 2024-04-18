from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage :

    def __init__(self,driver):
        self.driver = driver

    username_field = (By.NAME, "user-name")
    password_field = (By.NAME, "password")
    login_button = (By.ID, "login-button")
    sauce_logo = (By.XPATH, "//img[@src='img/Login_Bot_graphic.png']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username_field)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password_field)

    def get_login(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_saucelogo(self):
        return  self.driver.find_element(*LoginPage.sauce_logo)

    def waitforlogtobedisplayed(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(self.get_saucelogo()))
        assert self.get_saucelogo().is_displayed(), "sauce logo is not displayed"

    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()
