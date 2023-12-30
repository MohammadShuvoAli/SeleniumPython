import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://mypage.rediff.com/login/dologin/")

# opens alert window
driver.find_element(By.XPATH, "//input[@value='Login']").click()

alert_window = driver.switch_to.alert
print(alert_window.text)

alert_window.accept() # ok

time.sleep(10)
driver.quit()