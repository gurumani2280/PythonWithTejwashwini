import time

import pytest

from SauceDemoLatest.pagesLatest.addtocart import AddToCart
from SauceDemoLatest.pagesLatest.home_page import HomePage
from SauceDemoLatest.pagesLatest.login_page import LoginPage
from SauceDemoLatest.pagesLatest.your_cart_page import YourCartPage
from SauceDemoLatest.testLatest.test_base import TestBase


class TestLogin4(TestBase):

    @pytest.mark.loginlatest
    def test_login4(self):
        lp = LoginPage(self.driver)
        lp.wait_for_logo_to_display()
        lp.login("standard_user", "secret_sauce")

        hp = HomePage(self.driver)
        hp.click_backpack_addtocart()
        hp.click_cart_logo()
        ycp = YourCartPage(self.driver)
        ycp.click_checkout_btn()
        ycp.type_firstname('Tejaswini')

        time.sleep(2)
        ycp.type_lastname('Mohan')
        time.sleep(2)
        ycp.type_zipcode('560079')
        time.sleep(2)

        # atc = AddToCart(self.driver)
        # atc.element_required()
        # atc.add_to_cart_btn()
        # atc.cart_icon()
        # atc.checkout_bt()
        time.sleep(2)
