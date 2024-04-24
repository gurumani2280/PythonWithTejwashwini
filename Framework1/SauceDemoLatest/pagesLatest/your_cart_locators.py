from selenium.webdriver.common.by import By


class YourCartLocators :
    checkout_btn = (By.XPATH,"//a[text()='CHECKOUT']")
    first_name = (By.ID,"first-name")
    last_name = (By.ID,"last-name")
    zip_code = (By.ID,"postal-code")
    cancel_btn = (By.XPATH,"//a[text()='CANCEL']")
    continue_btn = (By.CLASS_NAME,"btn_primary cart_button")