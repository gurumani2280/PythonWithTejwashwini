from selenium.webdriver.common.by import By


class HomePageLocators:
    openmenu = (By.CSS_SELECTOR, "div.bm-burger-button")
    logout_menu = (By.XPATH, "//a[text()='Logout']")
    backpack_addtocart = (By.XPATH,"//div[text()='Sauce Labs Backpack']/../../..//button[text()='ADD TO CART']")
    cart_logo = (By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']")
