import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)

action = ActionChains(driver)
hotspot = driver.find_element(By.ID,"hot-spot")
#hotspot.context_click().perform()
action.context_click(hotspot).perform()
time.sleep(2)
alert =driver.switch_to.alert
alert_text = alert.text
print("alert text == ", alert_text)

alert.accept()
time.sleep(3)
driver.quit()