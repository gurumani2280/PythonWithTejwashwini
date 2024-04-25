from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://the-internet.herokuapp.com/windows")
#to refresh the browser

driver.find_element(By.LINK_TEXT,"Click Here").click()
#prints the window handle in focus
print(driver.current_window_handle)
#to fetch the first child window handle
chwnd = driver.window_handles[1]
#to switch focus the first child window handle
driver.switch_to.window(chwnd)
print(driver.find_element(By.TAG_NAME,"h3").text)
#to close the browser
driver.quit()