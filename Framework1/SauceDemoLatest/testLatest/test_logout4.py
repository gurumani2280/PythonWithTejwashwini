import pytest



from SauceDemoLatest.pagesLatest.home_page import HomePage
from SauceDemoLatest.pagesLatest.login_page import LoginPage
from SauceDemoLatest.testLatest.test_base import TestBase


class TestLogout4(TestBase):
    @pytest.mark.loginlatest
    def test_logout4(self):
        lp = LoginPage(self.driver)
        lp.wait_for_logo_to_display()
        lp.login("standard_user", "secret_sauce")
        hp = HomePage(self.driver)
        hp.logout()
        lp.wait_for_logo_to_display()

