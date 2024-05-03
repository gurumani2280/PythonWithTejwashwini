from SauceDemoLatest.pagesLatest.checkout_overview_locators import CheckoutOverviewLocators


class CheckoutOverviewPage(CheckoutOverviewLocators) :
    def __init__(self, driver):
        self.driver = driver

    def get_cancel_btn(self):
            return self.driver.find_element(*CheckoutOverviewLocators.cancel_btn)

    def get_finish_btn(self):
        return self.driver.find_element(*CheckoutOverviewLocators.finish_btn)

    def click_cancel_btn(self):
        self.get_cancel_btn().click()

    def click_finish_btn(self):
        self.get_finish_btn().click()
