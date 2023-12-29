from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver. maximize_window()
driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/")

driver.quit()