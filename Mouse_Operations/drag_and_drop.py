import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

target_element = driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']")
source_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(target_element, source_element).perform()

time.sleep(2)
driver.quit()