import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")



time.sleep(2)
driver.quit()