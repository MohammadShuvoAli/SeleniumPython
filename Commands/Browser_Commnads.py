import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(1)
driver.close()

time.sleep(1)
driver.quit()