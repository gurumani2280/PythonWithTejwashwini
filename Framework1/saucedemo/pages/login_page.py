from selenium.webdriver.common.by import By


class LoginPage :
    # self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    # self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    # self.driver.find_element(By.ID, "login-button").click()
    def __init__(self,driver):
        self.driver = driver

    username_field = (By.NAME, "user-name")
    password_field = (By.NAME, "password")
    login_button = (By.ID, "login-button")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username_field)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password_field)

    def get_login(self):
        return self.driver.find_element(*LoginPage.login_button)

    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()
