# import webdriver
import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
time.sleep(3)

# get element
element = driver.find_element(By.XPATH,"//span[text()='Courses']")


# create action chain object
action = ActionChains(driver)

# click the item
#action.click(element)
action.move_to_element(element)

# perform the operation
action.perform()
time.sleep(2)
driver.quit()
