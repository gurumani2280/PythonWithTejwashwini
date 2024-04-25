# import selenium module
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# using chrome driver
driver = webdriver.Chrome()

# web page url and open first window page
driver.get("http://demo.automationtesting.in/Windows.html")

# find xpath of button for child window page
# this page no. 2
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

# return all handles value of open browser window
handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)
    print(driver.title)
    time.sleep(1)
    driver.close()
time.sleep(1)
driver.quit()