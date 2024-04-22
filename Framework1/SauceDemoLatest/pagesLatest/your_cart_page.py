from SauceDemoLatest.pagesLatest.your_cart_locators import YourCartLocators


class YourCartPage(YourCartLocators) :
    def __init__(self,driver):
        self.driver = driver

    def get_checkout_btn(self):
        return self.driver.find_element(*YourCartLocators.checkout_btn)

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
