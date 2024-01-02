import time
from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bangladesh.gov.bd/index.php")

driver.save_screenshot(os.getcwd()+"\\screenshot1.png")
time.sleep(2)
driver.get_screenshot_as_file(os.getcwd()+"\\screenshot2.png")

driver.quit()