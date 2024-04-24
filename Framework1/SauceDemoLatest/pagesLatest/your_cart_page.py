from SauceDemoLatest.pagesLatest.your_cart_locators import YourCartLocators


class YourCartPage(YourCartLocators) :
    def __init__(self,driver):
        self.driver = driver

    def get_checkout_btn(self):
        return self.driver.find_element(*YourCartLocators.checkout_btn)

    def get_cancel_btn(self):
        return self.driver.find_element(*YourCartLocators.cancel_btn)

    def get_firstname(self):
        return self.driver.find_element(*YourCartLocators.first_name)

    def get_lastname(self):
        return self.driver.find_element(*YourCartLocators.last_name)

    def get_zipcode(self):
        return self.driver.find_element(*YourCartLocators.zip_code)

    def click_checkout_btn(self):
        self.get_checkout_btn().click()

    def click_cancel_btn(self):
        self.get_cancel_btn().click()

    def type_firstname(self,firstname):
        self.get_firstname().send_keys(firstname)

    def type_lastname(self,lastname):
        self.get_lastname().send_keys(lastname)

    def type_zipcode(self,zip):
        self.get_zipcode().send_keys(zip)



