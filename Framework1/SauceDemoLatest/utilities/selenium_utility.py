from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtility:
    @staticmethod
    def wait_for_elememt_to_be_displayed(driver,element,timeout=10):
        wait = WebDriverWait(driver, timeout)
        wait.until(expected_conditions.visibility_of(element))
        assert element.is_displayed(), "sauce logo is not displayed"