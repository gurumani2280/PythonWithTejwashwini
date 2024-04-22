from selenium.webdriver.common.by import By


class AddToCartLocators :
    element_required = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    add_to_cart_btn = (By.XPATH,"//button[text()='ADD TO CART']")
    back_btn = (By.XPATH,"//button[text()='REMOVE']")
    cart_icon = (By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']")
    checkout_bt = (By.XPATH,"//a[text()='CHECKOUT']")
