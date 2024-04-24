from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")    # for scrolling always use js methods
time.sleep(2)
#driver.execute_script("window.scrollBy(500,0)") # use for horizontal scroll https://www.google.com/search?gs_ssp=eJzj4tTP1TdISzOuKlNgNGB0YPDizC9KzEtPzSjKBQBfagem&q=orangehrm&rlz=1C1FKPE_enIN1104IN1104&oq=ora&gs_lcrp=EgZjaHJvbWUqEggCEC4YJxjHARjRAxiABBiKBTIGCAAQRRg5MgYIARBFGEAyEggCEC4YJxjHARjRAxiABBiKBTIMCAMQABhDGIAEGIoFMhgIBBAuGEMYgwEYxwEYsQMY0QMYgAQYigUyDAgFEAAYQxiABBiKBTIMCAYQABhDGIAEGIoFMgwIBxAAGEMYgAQYigXSAQgzMzc1ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8
driver.close()