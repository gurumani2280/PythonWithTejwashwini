from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# using chrome driver
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

iframe1 = driver.find_element(By.XPATH,"//iframe[@id='singleframe']")
# switch to 1st frame
driver.switch_to.frame(iframe1)

# get the header and print text
print(driver.find_element(By.TAG_NAME, "h5").text)
driver.find_element(By.TAG_NAME, "input").send_keys("some text")
time.sleep(2)
# back to default web page frame
driver.switch_to.default_content()

# print the text for single frame element
print(driver.find_element(By.CSS_SELECTOR, "li.active>a[href='#Single']").text)
time.sleep(2)

driver.quit()

