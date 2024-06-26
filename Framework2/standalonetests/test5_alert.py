import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(20)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
# Click the button to activate(generate) the alert
alert_button_locator = (By.XPATH, "//button[text()='Click for JS Prompt']")

activate_button = wait.until(expected_conditions.visibility_of_element_located(alert_button_locator))
activate_button.click()
# get the alert object
# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())
# Store the alert text in a variable
alert_text = alert.text
print("alert text == ", alert_text)
# Press the OK button
alert.send_keys("test")
time.sleep(2)
alert.accept()
result_locator = (By.CSS_SELECTOR, 'p#result')

result_element = wait.until(expected_conditions.visibility_of_element_located(result_locator))
result_text = result_element.text.strip()
print("result_text == ", result_text)
expected_text = 'You entered: test'
failure_message = f"result text {result_text} not matching {expected_text}"
assert result_text == expected_text, failure_message
time.sleep(2)
driver.quit()
