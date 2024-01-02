import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

cookie = driver.get_cookie()
print(cookie)

driver.quit()