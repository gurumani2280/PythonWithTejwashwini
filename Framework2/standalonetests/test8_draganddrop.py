import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#launch URL
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)
#object of ActionChains
action = ActionChains(driver)
#identify element
a = driver.find_element(By.ID,"column-a")
b = driver.find_element(By.ID,"column-b")
#hover over element
action.drag_and_drop(a,b).perform()
time.sleep(2)


print("Page title: " + driver.title)
#close browser
driver.quit()

