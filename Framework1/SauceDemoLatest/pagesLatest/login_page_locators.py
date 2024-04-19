from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.NAME, "user-name")
    password_field = (By.NAME, "password")
    login_button = (By.ID, "login-button")
    sauce_logo = (By.XPATH, "//img[@src='img/Login_Bot_graphic.png']")