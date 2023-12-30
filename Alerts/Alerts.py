import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# opens alert window
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()

alert_window = driver.switch_to.alert

print(alert_window.text)

alert_window.send_keys("Shuvo")
# alert_window.accept() # ok
alert_window.dismiss() # cancel

time.sleep(10)
driver.quit()