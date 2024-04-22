import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(20)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
# Click the button to activate(generate) the alert
alert_button_locator = (By.XPATH, "//button[text()='Click for JS Alert']")
driver.find_element(*alert_button_locator).click()
# get the alert object
alert =driver.switch_to.alert
# Store the alert text in a variable
alert_text = alert.text
print("alert text == ", alert_text)
# Press the OK button
alert.accept()
result_locator = (By.CSS_SELECTOR, 'p#result')
result_element =driver.find_element(*result_locator)
result_text = result_element.text.strip()
print("result_text == ", result_text)
expected_text = 'You successfully clicked an alert'
failure_message = f"result text {result_text} not matching {expected_text}"
assert result_text == expected_text, failure_message
time.sleep(2)
driver.quit()
