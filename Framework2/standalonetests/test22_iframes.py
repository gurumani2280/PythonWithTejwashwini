from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# using chrome driver
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()

nested_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
# switch to 1st frame
driver.switch_to.frame(nested_frame)

# get the header and print text
print(driver.find_element(By.TAG_NAME, "h5").text)
time.sleep(2)
inner_iframe = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_iframe)
print(driver.find_element(By.TAG_NAME, "h5").text)
driver.find_element(By.TAG_NAME, "input").send_keys("some text")
time.sleep(2)

# back to default web page frame
driver.switch_to.default_content()
time.sleep(2)
# print the text for single frame element
single_frame_btn=driver.find_element(By.CSS_SELECTOR, "a[href='#Single']")
print(single_frame_btn.text)
single_frame_btn.click()
time.sleep(2)

driver.quit()

