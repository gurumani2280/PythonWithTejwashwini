from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///F:/EmexoPython/PythonWithTejwashwini/BasicHtmlElement.html")
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("Tejaswini")
driver.find_element(By.NAME,"password").send_keys("password")
time.sleep(3)
firstname = driver.find_element(By.NAME,"firstName")
if firstname.is_enabled():
    firstname.send_keys("Tejaswini")
else:
    print("firstname is not enabled hence cant enter any values")
driver.find_element(By.ID,"lastname").send_keys("Mohankumar")
driver.find_element(By.ID,"address").send_keys("Prashanthnagar,Bangalore")
time.sleep(3)

driver.quit()