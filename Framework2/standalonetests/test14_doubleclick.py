import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#from standalonetests.test6_actionchains import action

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//span[text()='Courses']")
action = ActionChains(driver)
action.double_click(element).perform()
time.sleep(2)