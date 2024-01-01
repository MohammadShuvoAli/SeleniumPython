import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

input = driver.find_element(By.XPATH, '//*[@id="field1"]')
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

input.click()
input.clear()
input.send_keys("Shuvo")

act = ActionChains(driver)
act.double_click(button).perform()

time.sleep(2)
driver.quit()