from SauceDemoLatest.pagesLatest.add_to_cart_locators import AddToCartLocators


class AddToCart(AddToCartLocators):
    def __init__(self,driver):
        self.driver = driver

        def get_requireditem(self):
            return self.driver.find_element(*AddToCartLocators.element_required)

        def get_addtocart(self):
            return self.driver.find_element(*AddToCartLocators.add_to_cart_btn)

        def get_backbutton(self):
            return self.driver.find_element(*AddToCartLocators.back_btn)

        def get_cart(self):
            return self.driver.find_element(*AddToCartLocators.cart_icon)

        def get_checkout(self):
            return self.driver.find_element(*AddToCartLocators.checkout_bt)