from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://reddit.com")
cookies = driver.get_cookies()
print(cookies)
print(type(cookies))
for cookie in cookies:
    print(cookie)

driver.quit()