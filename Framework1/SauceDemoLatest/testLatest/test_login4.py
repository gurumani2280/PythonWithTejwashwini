import pytest


from SauceDemoLatest.testLatest.test_base import TestBase
from SauceDemoLatest.pagesLatest.login_page import LoginPage



class TestLogin4(TestBase):
    @pytest.mark.loginlatest
    def test_login4(self):
        lp = LoginPage(self.driver)
        lp.wait_for_logo_to_display()
        lp.login("standard_user","secret_sauce")




