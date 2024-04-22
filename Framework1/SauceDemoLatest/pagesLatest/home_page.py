from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SauceDemoLatest.pagesLatest.home_page_locators import HomePageLocators


class HomePage(HomePageLocators):
    def __init__(self,driver):
        self.driver = driver

    def get_openmenu(self):
        return self.driver.find_element(*HomePage.openmenu)

    def getlogout_menu(self):
        return self.driver.find_element(*HomePage.logout_menu)

    def get_backpack_addtocart(self):
        return self.driver.find_element(*HomePageLocators.backpack_addtocart)

    def get_cart_logo(self):
        return self.driver.find_element(*HomePageLocators.cart_logo)

    def waitforopenmenutobevisible(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(self.get_openmenu()))
        assert self.get_openmenu().is_displayed() , "open menu is not displayed"

    def click_openmenu(self):
        self.waitforopenmenutobevisible()
        self.get_openmenu().click()

    def waitforlogoutmenutobevisible(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(self.getlogout_menu()))
        assert self.getlogout_menu().is_displayed() , "logout menu is not displayed"

    def click_backpack_addtocart(self):
        self.get_backpack_addtocart().click()

    def click_cart_logo(self):
        self.get_cart_logo().click()

    def click_logout(self):
        self.waitforlogoutmenutobevisible()
        self.getlogout_menu().click()

    def logout(self):
        self.click_openmenu()
        self.click_logout()




