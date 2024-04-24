from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window();
driver.get('https://pythonspot.com')
driver.save_screenshot("screenshot.png")
#driver.get_screenshot_as_file("C:/Users/Admin/PycharmProjects/PythonTesting/Framework2/screenshot4.png")

element = driver.find_element(By.CSS_SELECTOR, 'div.head')
element.screenshot('C:/Users/Admin/PycharmProjects/PythonTesting/Framework2/just-the-header1.png')     # it will take the SS of only the header
driver.close()

