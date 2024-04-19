from selenium.webdriver.common.by import By


class HomePageLocators:
    openmenu = (By.CSS_SELECTOR, "div.bm-burger-button")
    logout_menu = (By.XPATH, "//a[text()='Logout']")