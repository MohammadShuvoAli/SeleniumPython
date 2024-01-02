from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bangladesh.gov.bd/index.php")

driver.save_screenshot(os.getcwd()+"\\screenshot.png")

driver.quit()